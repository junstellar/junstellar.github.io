#!/usr/bin/env python
"""
조차장 플레이 드라이버 — 실제 사람처럼 화면을 보고 클릭한다.

  python play.py --out shots/try1 --actions "shot; text; click 400,300; wait 3500; shot"

액션 (세미콜론 구분):
  shot                  스크린샷 저장 (out/NN.png) + 그 시점 게임 상태 출력
  text                  화면 DOM 텍스트 덤프
  click X,Y             화면 좌표 클릭 (CSS px)
  key K                 키 입력 (key 1, key q, key z ...)
  wait MS               대기 (이동 애니메이션은 2~4초)
  drag X1,Y1,X2,Y2      드래그 (카메라 회전)
  wheel D               휠 (음수=확대). 예: wheel -300
  eval JS               페이지에서 JS 실행하고 결과 출력 (디버그용)

옵션: --w --h (기본 1100x820, 모바일은 430 932) --no-fresh --url --timeout
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"

STATE_JS = """() => {
  try {
    const i = (window.__SHOT && window.__SHOT.info) ? window.__SHOT.info() : {};
    const s = (window.SH && SH.Game && SH.Game.state) ? SH.Game.state : null;
    return { phase:i.phase, level:i.levelId, moves:i.moves, par:i.par, errors:i.errors,
             at:s?s.at:null, consist:s?s.consist:null, tracks:s?s.tracks:null,
             win:(s&&SH.Puzzle)?SH.Puzzle.isWin(s):null,
             busy:(SH.Motion?SH.Motion.isBusy:null),
             cam:(SH.Render&&SH.Render.getCam)?SH.Render.getCam():null };
  } catch (e) { return { err:String(e) }; }
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
    ap.add_argument("--url", default="")
    ap.add_argument("--no-fresh", action="store_true")
    ap.add_argument("--timeout", type=int, default=180)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    q = "?debug=1" + ("" if a.no_fresh else "&fresh=1")
    url = a.url or f"http://127.0.0.1:{port}/shunting/index.html{q}"

    from playwright.sync_api import sync_playwright
    errors, n = [], 0
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--hide-scrollbars", "--mute-audio"])
        pg = b.new_page(viewport={"width": a.w, "height": a.h}, device_scale_factor=1)
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[console] {m.text}")
              if m.type == "error" else None)
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                                 timeout=a.timeout * 1000)
        except Exception as e:
            print("BOOT FAILED:", e)
            pg.screenshot(path=os.path.join(a.out, "boot_failed.png"))
            b.close(); httpd.shutdown(); return 1
        pg.wait_for_timeout(800)

        for raw in a.actions.split(";"):
            act = raw.strip()
            if not act:
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
                elif head == "key":
                    pg.keyboard.press(arg); print(f"KEY {arg}")
                elif head == "wait":
                    pg.wait_for_timeout(int(arg))
                elif head == "wheel":
                    pg.mouse.move(a.w / 2, a.h / 2)
                    pg.mouse.wheel(0, float(arg)); print(f"WHEEL {arg}")
                elif head == "drag":
                    x1, y1, x2, y2 = [float(v) for v in arg.split(",")]
                    pg.mouse.move(x1, y1); pg.mouse.down()
                    pg.mouse.move(x2, y2, steps=12); pg.mouse.up()
                    print(f"DRAG {x1},{y1} -> {x2},{y2}")
                elif head == "text":
                    t = pg.evaluate("() => (document.getElementById('ui-root')"
                                    "||document.body).innerText")
                    print("TEXT " + json.dumps(t, ensure_ascii=False))
                elif head == "eval":
                    print("EVAL " + json.dumps(pg.evaluate(arg), ensure_ascii=False))
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
