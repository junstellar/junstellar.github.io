#!/usr/bin/env python
"""새로고침으로 항해가 이어지는가 (Core.save/load) — ?fresh=1 없이."""
import functools, http.server, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"
ST = "() => JSON.parse(JSON.stringify(window.__SHOT.state()))"


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
    os.makedirs("resume_out", exist_ok=True)
    port, httpd = serve(ROOT)
    base = f"http://127.0.0.1:{port}/odyssey/index.html"
    from playwright.sync_api import sync_playwright
    errors = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--hide-scrollbars", "--mute-audio"])
        pg = b.new_context(viewport={"width": 1100, "height": 820},
                           device_scale_factor=1).new_page()
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[console] {m.text}")
              if m.type == "error" else None)

        pg.goto(base + "?fresh=1", wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                             timeout=90000)
        pg.wait_for_timeout(600)
        pg.evaluate("() => window.__SHOT.auto(['big','mid'], 95)")
        pg.wait_for_timeout(900)
        pg.evaluate("() => window.__SHOT.next()")     # 2편으로
        pg.wait_for_timeout(1200)
        a = pg.evaluate(ST)
        print(f"저장 직전: {a.get('index')+1}편 {a.get('id')} crew={a.get('crew')}")

        pg.goto(base, wait_until="domcontentloaded", timeout=60000)   # 새로고침
        pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                             timeout=90000)
        pg.wait_for_timeout(1200)
        c = pg.evaluate(ST)
        print(f"새로고침 뒤: {c.get('index')+1}편 {c.get('id')} crew={c.get('crew')} "
              f"engine={c.get('engine')} phase={c.get('phase')} stCrew={c.get('stCrew')}")
        pg.screenshot(path=os.path.join("resume_out", "resumed.png"))
        ok = (c.get("id") == a.get("id") and c.get("crew") == a.get("crew")
              and c.get("phase") == "run")
        print("이어짐:", "OK" if ok else "실패")
        b.close()
    httpd.shutdown()
    print(f"--- {len(errors)} console error(s) ---")
    for e in errors[:10]:
        print("  ", e[:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
