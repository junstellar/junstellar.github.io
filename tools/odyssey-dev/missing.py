#!/usr/bin/env python
"""st3 을 일부러 못 불러오게 막고, 게임이 '1편짜리 항해'로 조용히 굴러가는 대신
   멈추고 이유를 말하는지 본다. (사용자가 겪은 '1편 끝내니 에필로그'의 원인)"""
import functools, http.server, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
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
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?fresh=1"
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width": 900, "height": 700})
        # st3 만 못 오게 막는다 = 캐시가 꼬여 한 편을 못 읽은 상황
        pg.route("**/st3-sirens.js*", lambda r: r.abort())
        pg.goto(url)
        pg.wait_for_timeout(3500)

        ready = pg.evaluate("() => !!(window.__SHOT && __SHOT.ready)")
        err = pg.evaluate("() => { var e=document.getElementById('bootErr');"
                          " return e ? e.textContent : ''; }")
        msg = pg.evaluate("() => { var e=document.getElementById('bootMsg');"
                          " return e ? e.textContent : ''; }")
        nstage = pg.evaluate("() => (window.OD && OD.Core && OD.Core.stages)"
                             " ? OD.Core.stages.length : -1")
        print("부팅 성공했나(성공하면 안 됨):", ready)
        print("항로 길이 (조용히 5편짜리로 굴러가면 실패):", nstage)
        print("화면 문구:", msg)
        print("에러 문구:", err[:220])
        good = (not ready) and ("모자랍니다" in err) and ("st3" in err)
        print("RESULT:", "OK — 멈추고 이유를 말한다" if good else "*** 실패 ***")
        b.close()
    httpd.shutdown()


if __name__ == "__main__":
    main()
