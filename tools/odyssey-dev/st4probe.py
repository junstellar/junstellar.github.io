#!/usr/bin/env python
"""4편(스킬라) — 사람처럼 연타했을 때 무슨 일이 벌어지는지 계측한다.

auto()는 '완벽한 봇'이라 안전할 때만 젓는다 — 사용자의 경험을 재현하지 못한다.
여기서는 drive(tap=True) 로 **계속 연타**해서 실제 실패를 재현하고,
그 순간 화면(게이지)이 무엇을 보여주고 있었는지 스크린샷으로 남긴다.

2편/3편 길이도 함께 잰다.
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
    ap.add_argument("--out", default="st4probe_out")
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width": a.w, "height": a.h})
        pg.goto(url); pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)

        # ── 4편으로 바로 간다 ──────────────────────────────────────────────
        pg.evaluate("() => __SHOT.stage(3)")
        pg.wait_for_function("() => __SHOT.state().engine==='st4'", timeout=20000)
        pg.wait_for_timeout(600)

        print("=== 4편: 사람처럼 계속 연타 (drive tap=true) ===")
        # 2초씩 끊어 굴리며 상태를 찍는다
        shots = 0
        for step in range(40):
            st = pg.evaluate(
                "() => { var s=OD.St4.drive(2.0, true); return JSON.parse(JSON.stringify(s)); }")
            g = st
            print(f"  t={g['t']:6.2f} prog={g['prog']:.3f} alive={g['alive']} "
                  f"taken={g['taken']} nRow={g['nRow']} strokes={g['strokes']} "
                  f"safe={g['safe']} gauge_len={g['gauge']['len']} "
                  f"danger={g['gauge']['danger']} alpha={g['gauge']['alpha']} "
                  f"phase={g['phase']}")
            if shots < 4 and g["phase"] == "run":
                pg.screenshot(path=os.path.join(a.out, f"mash_{shots}.png"))
                shots += 1
            if g["phase"] != "run":
                print(f"  >>> 끝: {json.dumps(g.get('result'), ensure_ascii=False)}")
                break

        # ── 결과 카드 ──
        pg.wait_for_timeout(900)
        pg.screenshot(path=os.path.join(a.out, "mash_card.png"))
        txt = pg.evaluate("() => { var e=document.querySelector('.od-card,.st4-end,#ui-root');"
                          " return e? e.innerText.replace(/\\n+/g,' | ') : ''; }")
        print("  CARD", json.dumps(txt, ensure_ascii=False)[:400])

        # ── 완벽한 봇은 몇 초 걸리나 (길이 측정) ────────────────────────────
        print("\n=== 길이 측정 (완벽한 봇) ===")
        for sid, idx, eng, arg in [("scylla", 3, "st4", "6"), ("windbag", 1, "st2", "'gold'"),
                                   ("sirens", 2, "st3", "'smart'")]:
            pg.evaluate(f"() => __SHOT.stage({idx})")
            pg.wait_for_function(f"() => __SHOT.state().engine==='{eng}'", timeout=20000)
            pg.wait_for_timeout(400)
            r = pg.evaluate(
                f"() => {{ var s=OD.{eng.capitalize()}.auto({arg}, 400);"
                " return JSON.parse(JSON.stringify(s)); }")
            print(f"  {sid:8s} 게임내 경과 t={r.get('t')}초  phase={r.get('phase')}")

        b.close()
    httpd.shutdown()


if __name__ == "__main__":
    main()
