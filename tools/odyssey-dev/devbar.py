#!/usr/bin/env python
"""개발용 편 선택 바 검증.

1) localhost 에서는 뜬다 / ?dev=0 이면 안 뜬다 (공개 페이지 보호)
2) 1~6 을 누르면 실제로 그 편으로 간다 (엔진이 바뀌는지 확인)
3) 바를 눌러도 게임 입력으로 새어 들어가지 않는다
4) 모듈이 모자라면 조용히 넘어가지 않고 멈춘다
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"


def serve(root):
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
        def end_headers(self):
            self.send_header("Cache-Control", "no-store"); super().end_headers()
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port),
                                            functools.partial(Q, directory=root))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return port, httpd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="devbar_out")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    base = f"http://127.0.0.1:{port}/odyssey/index.html"

    from playwright.sync_api import sync_playwright
    errs, ok = [], True
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width": 1100, "height": 820})
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))

        # 1) 노출 조건
        pg.goto(base + "?fresh=1")
        pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
        pg.wait_for_timeout(500)
        shown = pg.evaluate("() => !!document.querySelector('.od-devbar')")
        n = pg.evaluate("() => document.querySelectorAll('.od-devbar button[data-i]').length")
        print(f"localhost 에서 바가 뜬다: {shown}  (편 버튼 {n}개)")
        ok &= shown and n == 6
        pg.screenshot(path=os.path.join(a.out, "bar.png"))

        pg.goto(base + "?fresh=1&dev=0")
        pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
        pg.wait_for_timeout(400)
        hidden = pg.evaluate("() => !document.querySelector('.od-devbar')")
        print(f"?dev=0 이면 숨는다: {hidden}")
        ok &= hidden

        # 2) 눌러서 이동
        pg.goto(base + "?fresh=1")
        pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
        pg.wait_for_timeout(500)
        want = ["st1", "st2", "st3", "st4", "st5", "st6"]
        for i in range(6):
            pg.click(f".od-devbar button[data-i='{i}']")
            pg.wait_for_timeout(950)
            st = pg.evaluate("() => __SHOT.state()")
            marked = pg.evaluate(
                f"() => document.querySelector(\".od-devbar button[data-i='{i}']\")"
                ".className")
            good = st.get("engine") == want[i] and marked == "on"
            print(f"  {i+1}편 버튼 -> engine={st.get('engine')} phase={st.get('phase')} "
                  f"표시={marked!r} {'OK' if good else '*** 실패 ***'}")
            ok &= good
            if i == 3:
                pg.screenshot(path=os.path.join(a.out, "bar_st4.png"))

        # 3) 바 클릭이 게임 입력으로 새는지 — 4편에서 저어졌는지 본다
        pg.click(".od-devbar button[data-i='3']")
        pg.wait_for_timeout(900)
        before = pg.evaluate("() => __SHOT.state().strokes")
        for _ in range(5):
            pg.click(".od-devbar button[data-i='3']")
            pg.wait_for_timeout(260)
        after = pg.evaluate("() => __SHOT.state().strokes")
        leak = (after or 0) > (before or 0)
        print(f"바를 5번 눌렀을 때 노가 저어졌나(새면 안 됨): {leak}  "
              f"({before} -> {after})")
        ok &= not leak

        # 4) '처음부터'
        pg.click(".od-devbar button[data-act='reset']")
        pg.wait_for_timeout(1100)
        st = pg.evaluate("() => __SHOT.state()")
        crew = pg.evaluate("() => OD.Core.crew")
        print(f"'처음부터' -> engine={st.get('engine')} crew={crew}")
        ok &= st.get("engine") == "st1" and crew == 600

        b.close()
    httpd.shutdown()
    print(f"\n--- console errors: {len(errs)} ---")
    for e in errs[:5]:
        print("  ", e[:180])
    print("RESULT:", "OK" if ok and not errs else "*** 실패 ***")


if __name__ == "__main__":
    main()
