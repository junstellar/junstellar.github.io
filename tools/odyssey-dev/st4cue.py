#!/usr/bin/env python
"""4편에서 규칙을 가르치는 두 박자가 실제로 화면에 뜨는지 눈으로 확인한다.
   "저어라"(초록 안전) -> "멈춰라"(붉은 위험) 순서로 잡아 스크린샷을 남긴다."""
import argparse, functools, http.server, os, socket, sys, threading

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


CUE = ("() => { var c=document.querySelector('.st4 .cue');"
       " return c ? (c.className+'|'+c.textContent) : 'none'; }")
HINT = ("() => { var h=document.querySelector('.st4 .hint');"
        " return h ? (h.className+'|'+h.textContent) : 'none'; }")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="cue_out")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width": 1100, "height": 820})
        pg.goto(url); pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
        pg.evaluate("() => __SHOT.stage(3)")
        pg.wait_for_function("() => __SHOT.state().engine==='st4'", timeout=20000)
        pg.wait_for_timeout(700)

        print("hint:", pg.evaluate(HINT))
        got_go = got_stop = False
        # 아무것도 누르지 않고 굴리기만 한다 — 안내가 저절로 나와야 한다
        for i in range(60):
            pg.evaluate("() => OD.St4.drive(0.18, false)")
            c = pg.evaluate(CUE)
            if 'on' in c and 'stop' not in c and not got_go:
                got_go = True
                pg.screenshot(path=os.path.join(a.out, "cue_go.png"))
                print(f"  [{i}] 저어라 떴다 -> {c}")
            if 'stop' in c and not got_stop:
                got_stop = True
                pg.wait_for_timeout(120)
                pg.screenshot(path=os.path.join(a.out, "cue_stop.png"))
                print(f"  [{i}] 멈춰라 떴다 -> {c}")
                break
        print("결과: 저어라", got_go, "/ 멈춰라", got_stop)
        b.close()
    httpd.shutdown()


if __name__ == "__main__":
    main()
