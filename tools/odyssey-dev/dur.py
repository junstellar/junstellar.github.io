#!/usr/bin/env python
"""여섯 편 각각의 길이(완벽한 봇 기준)를 잰다 — 블로그에 쓸 실제 숫자."""
import functools, http.server, socket, sys, threading
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
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

CASES = [
    (0, "st1", "키클롭스의 동굴", "['big','mid','sml']"),
    (1, "st2", "바람 자루",       "'gold'"),
    (2, "st3", "세이렌의 노래",   "'smart'"),
    (3, "st4", "스킬라",          "6"),
    (4, "st5", "헬리오스의 소",   "'band'"),
    (5, "st6", "이타카의 활",     "null"),
]

def main():
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"
    from playwright.sync_api import sync_playwright
    total = 0.0
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11","--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width":1100,"height":820})
        pg.goto(url); pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
        for idx, eng, name, arg in CASES:
            pg.evaluate(f"() => __SHOT.stage({idx})")
            pg.wait_for_function(f"() => __SHOT.state().engine==='{eng}'", timeout=20000)
            pg.wait_for_timeout(350)
            r = pg.evaluate(f"() => {{ var s=__SHOT.auto({arg}, 400); return s && (s.t != null ? s.t : s.gt); }}")
            t = float(r or 0); total += t
            print(f"  {idx+1}편 {name:16s} {t:6.1f}초")
        b.close()
    httpd.shutdown()
    print(f"\n  합계 {total:.0f}초 = 약 {total/60:.1f}분 (한 번에 클리어했을 때)")

main()
