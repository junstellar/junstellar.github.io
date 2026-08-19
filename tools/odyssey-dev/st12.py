#!/usr/bin/env python
"""
1편 -> 2편 연속 플레이 드라이버.

st1.py 와 같은 서버/부팅 절차를 쓰되, **누르고 있다가 놓는 입력**을 실제 이벤트로 낸다.

액션 (개행이 있으면 줄 단위):
  shot                    스크린샷 + 상태
  text                    #ui-root 텍스트 덤프
  wait MS
  key K                   한 번 누르기(press)
  keyhold MS              스페이스 keydown -> MS 대기 -> keyup
  click X,Y
  hold X,Y,MS             마우스 down -> MS 대기 -> up  (좌표 생략 시 화면 중앙)
  taphold MS              터치(포인터 touch) down -> MS 대기 -> up
  eval JS
옵션: --w --h --path --touch(모바일 에뮬레이션) --timeout
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"

STATE_JS = """() => {
  try {
    return (window.__SHOT && window.__SHOT.state) ? window.__SHOT.state()
                                                  : { err: 'no __SHOT' };
  } catch (e) { return { err: String(e) }; }
}"""


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
    ap.add_argument("--out", default="play_out")
    ap.add_argument("--actions", required=True)
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    ap.add_argument("--path", default="/odyssey/index.html")
    ap.add_argument("--touch", action="store_true")
    ap.add_argument("--timeout", type=int, default=60)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}{a.path}?debug=1&fresh=1"

    from playwright.sync_api import sync_playwright
    errors, n = [], 0
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--hide-scrollbars", "--mute-audio"])
        ctx_kw = dict(viewport={"width": a.w, "height": a.h}, device_scale_factor=1)
        if a.touch:
            ctx_kw.update(has_touch=True, is_mobile=True)
        ctx = b.new_context(**ctx_kw)
        pg = ctx.new_page()
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[console] {m.text}")
              if m.type == "error" else None)
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                                 timeout=a.timeout * 1000)
        except Exception as e:
            print("BOOT FAILED:", e)
            try:
                print("BOOTERR", pg.evaluate(
                    "() => (document.getElementById('bootErr')||{}).textContent || ''"))
            except Exception:
                pass
            pg.screenshot(path=os.path.join(a.out, "boot_failed.png"))
            b.close(); httpd.shutdown()
            for e2 in errors[:12]:
                print("  ", e2[:400])
            return 1
        pg.wait_for_timeout(700)

        cx, cy = a.w / 2, a.h * 0.55

        raw_actions = (a.actions.splitlines() if "\n" in a.actions.strip()
                       else a.actions.split(";"))
        for raw in raw_actions:
            act = raw.strip()
            if not act or act.startswith("#"):
                continue
            head = act.split()[0].lower()
            arg = act[len(head):].strip()
            try:
                if head == "shot":
                    n += 1
                    path = os.path.join(a.out, f"{n:02d}.png")
                    pg.screenshot(path=path)
                    print(f"SHOT {path}")
                    print("     " + json.dumps(pg.evaluate(STATE_JS), ensure_ascii=False))
                elif head == "click":
                    x, y = [float(v) for v in arg.split(",")]
                    pg.mouse.move(x, y); pg.mouse.down()
                    pg.wait_for_timeout(50); pg.mouse.up()
                    print(f"CLICK {x},{y}")
                elif head == "hold":
                    parts = [v for v in arg.split(",") if v.strip() != ""]
                    if len(parts) == 3:
                        x, y, ms = float(parts[0]), float(parts[1]), int(float(parts[2]))
                    else:
                        x, y, ms = cx, cy, int(float(parts[0]))
                    pg.mouse.move(x, y); pg.mouse.down()
                    pg.wait_for_timeout(ms); pg.mouse.up()
                    print(f"HOLD {x},{y} {ms}ms")
                elif head == "taphold":
                    parts = [v for v in arg.split(",") if v.strip() != ""]
                    if len(parts) == 3:
                        x, y, ms = float(parts[0]), float(parts[1]), int(float(parts[2]))
                    else:
                        x, y, ms = cx, cy, int(float(parts[0]))
                    pg.touchscreen.tap(x, y) if ms <= 0 else None
                    if ms > 0:
                        # Playwright 의 touchscreen 은 tap 만 준다 -> CDP 로 직접 누른다
                        cdp = pg.context.new_cdp_session(pg)
                        pt = [{"x": x, "y": y, "radiusX": 12, "radiusY": 12, "force": 1, "id": 1}]
                        cdp.send("Input.dispatchTouchEvent",
                                 {"type": "touchStart", "touchPoints": pt})
                        pg.wait_for_timeout(ms)
                        cdp.send("Input.dispatchTouchEvent",
                                 {"type": "touchEnd", "touchPoints": []})
                        cdp.detach()
                    print(f"TAPHOLD {x},{y} {ms}ms")
                elif head == "down":
                    x, y = ([float(v) for v in arg.split(",")] if arg else [cx, cy])
                    pg.mouse.move(x, y); pg.mouse.down(); print(f"DOWN {x},{y}")
                elif head == "up":
                    pg.mouse.up(); print("UP")
                elif head == "keydown":
                    pg.keyboard.down(" "); print("KEYDOWN space")
                elif head == "keyup":
                    pg.keyboard.up(" "); print("KEYUP space")
                elif head == "key":
                    pg.keyboard.press(arg); print(f"KEY {arg}")
                elif head == "keyhold":
                    ms = int(float(arg))
                    pg.keyboard.down(" ")
                    pg.wait_for_timeout(ms)
                    pg.keyboard.up(" ")
                    print(f"KEYHOLD {ms}ms")
                elif head == "resize":
                    w, h = [int(float(v)) for v in arg.split(",")]
                    pg.set_viewport_size({"width": w, "height": h})
                    pg.wait_for_timeout(400)
                    print(f"RESIZE {w}x{h}")
                elif head == "wait":
                    pg.wait_for_timeout(int(arg))
                elif head == "text":
                    t = pg.evaluate("() => (document.getElementById('ui-root')"
                                    "||document.body).innerText")
                    print("TEXT " + json.dumps(t, ensure_ascii=False))
                elif head == "eval":
                    print("EVAL " + json.dumps(pg.evaluate("() => (" + arg + ")"),
                                               ensure_ascii=False))
                else:
                    print("UNKNOWN ACTION:", act)
            except Exception as e:
                print(f"ACTION FAILED [{act}]: {type(e).__name__}: {e}")
        b.close()
    httpd.shutdown()

    if errors:
        print(f"--- {len(errors)} console error(s) ---")
        for e in errors[:12]:
            print("  ", e[:400])
    else:
        print("--- 0 console error(s) ---")
    return 0


if __name__ == "__main__":
    sys.exit(main())
