#!/usr/bin/env python
"""정적 파일 서버 — 캐시를 끈다.

`python -m http.server` 는 Cache-Control 을 안 보내서 브라우저가 js/css 를
그대로 캐시한다. 그래서 게임 파일을 고쳐도 새로고침하면 옛 빌드가 뜬다
(실제로 4편 HUD 를 고쳤는데 화면엔 예전 것이 계속 나왔다).
프리뷰용 서버는 항상 최신 파일을 줘야 한다.

    python tools/serve-nocache.py --port 8899 --dir static/games
"""
import argparse
import functools
import http.server
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stdout.write("%s %s\n" % (self.command, self.path))
        sys.stdout.flush()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8899)
    ap.add_argument("--dir", default=".")
    a = ap.parse_args()

    root = os.path.abspath(a.dir)
    if not os.path.isdir(root):
        sys.exit("no such directory: " + root)

    handler = functools.partial(NoCacheHandler, directory=root)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", a.port), handler)
    print("serving %s at http://127.0.0.1:%d  (no-store)" % (root, a.port))
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
