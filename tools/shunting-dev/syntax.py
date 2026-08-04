#!/usr/bin/env python
"""JS 로드/문법 검사 — node 없이 브라우저에 실제로 태워본다.

  python syntax.py --all
  python syntax.py js/30-render.js js/70-input.js --expect "SH.Render,SH.Input"
"""
import argparse, functools, glob, http.server, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"
GAMEDIR = os.path.join(ROOT, "shunting")


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
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--expect", default="")
    a = ap.parse_args()

    if a.all:
        files = ["js/" + os.path.basename(p)
                 for p in sorted(glob.glob(os.path.join(GAMEDIR, "js", "*.js")))]
    else:
        rest = [f.replace("\\", "/").split("shunting/")[-1] for f in a.files]
        if not rest:
            print("파일을 지정하세요"); return 2
        files = ["js/00-util.js"] + [f for f in rest if f != "js/00-util.js"]

    from playwright.sync_api import sync_playwright
    port, httpd = serve(ROOT)
    tags = "\n".join(f'<script src="/shunting/{f}"></script>' for f in files)
    html = (f'<!DOCTYPE html><meta charset="utf-8">'
            f'<div id="boot"></div><div id="bootBar"></div>'
            f'<div id="bootMsg"></div><div id="bootErr"></div>'
            f'<script src="/shunting/vendor/three.min.js"></script>{tags}'
            f'<script>window.__LOADED=true;</script>')

    errors = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist"])
        pg = b.new_page()
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[{m.type}] {m.text}")
              if m.type == "error" else None)
        pg.route("**/__check", lambda r: r.fulfill(body=html, content_type="text/html"))
        pg.goto(f"http://127.0.0.1:{port}/__check", wait_until="load", timeout=60000)
        pg.wait_for_timeout(400)
        loaded = pg.evaluate("() => !!window.__LOADED")
        globs = {}
        for g in [x.strip() for x in a.expect.split(",") if x.strip()]:
            try:
                globs[g] = pg.evaluate(f"() => typeof ({g}) !== 'undefined' && {g} !== null")
            except Exception as e:
                globs[g] = f"ERR {e}"
        b.close()
    httpd.shutdown()

    print("LOADED ALL SCRIPTS:", loaded)
    for g, v in globs.items():
        print(f"  {g}: {'OK' if v is True else 'MISSING'}")
    if errors:
        print(f"--- {len(errors)} ERROR(s) ---")
        for e in errors[:30]:
            print("  ", e[:700])
        return 1
    if not loaded:
        print("--- 스크립트가 끝까지 실행되지 않았습니다 (파싱 에러 가능) ---")
        return 1
    print("OK - 에러 없음")
    return 0


if __name__ == "__main__":
    sys.exit(main())
