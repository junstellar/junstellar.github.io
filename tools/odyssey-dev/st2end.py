#!/usr/bin/env python
"""
2편 「바람 자루」 절정 검증 드라이버.

index.html 을 띄우고 __SHOT.stage(1) 로 2편에 들어간 뒤, 게이지를 보고
'참았다 놓기'를 반복해 엔딩까지 간다. 졸음 구간에서 **버틸지 말지**를 골라
결과 차이를 잰다.

  python st2end.py --drowse hold   # 끝까지 붙잡는다
  python st2end.py --drowse let    # 손을 뗀다

--out 에 절정 구간 스크린샷을 남긴다.
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
    ap.add_argument("--out", default="end_out")
    ap.add_argument("--drowse", default="hold", choices=["hold", "let"])
    ap.add_argument("--aim", type=float, default=0.55)   # 금색 띠 안에서 노리는 지점
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    ap.add_argument("--maxsec", type=float, default=260)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"

    from playwright.sync_api import sync_playwright
    errors, shots = [], 0
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--hide-scrollbars", "--mute-audio"])
        ctx = b.new_context(viewport={"width": a.w, "height": a.h}, device_scale_factor=1)
        pg = ctx.new_page()
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[console] {m.text}")
              if m.type == "error" else None)
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                             timeout=60000)
        pg.wait_for_timeout(500)

        def st():
            return pg.evaluate("() => window.OD.St2.state()")

        def hold(sec, down):
            pg.evaluate("([s,d]) => window.__SHOT.hold(s,d)", [max(0.02, sec), bool(down)])

        def shot(tag):
            nonlocal shots
            shots += 1
            path = os.path.join(a.out, f"{shots:02d}-{tag}.png")
            pg.screenshot(path=path)
            print(f"SHOT {path}")
            return path

        pg.evaluate("() => window.__SHOT.stage(1)")
        pg.wait_for_timeout(600)
        s = st()
        print("ENTER st2:", json.dumps({k: s.get(k) for k in
              ("phase", "gphase", "prog", "crew", "bag")}, ensure_ascii=False))
        shot("open")

        marks = set()
        cycles = 0
        while True:
            s = st()
            if not s.get("ready") or s.get("phase") != "run":
                break
            if s["t"] > a.maxsec:
                print("TIMEOUT at t=", s["t"]); break
            gp = s["gphase"]

            if gp == "run":
                if s["prog"] >= 0.60 and "mid" not in marks:
                    marks.add("mid"); shot("mid-sea")
                if s["fix"] > 0:
                    hold(s["fix"] + 0.06, False); continue
                if s["bag"] <= 0:
                    hold(0.5, False); continue
                lo, hi = s["band"]
                aim = lo + (hi - lo) * a.aim
                # 곧 파도가 온다면 그만큼 미리 본다 (게이지의 유령 막대가 보여 주는 값)
                bump = 0.0
                if s["waveIn"] < 0.45 and s["waveAmp"] > 0:
                    bump = s["waveAmp"] * (0.30 + 0.70 * s["fill"])
                if s["load"] > 0.07:
                    hold(min(1.2, (s["load"] - 0.04) / 0.86), False)
                else:
                    dt = (aim - bump - s["load"]) / max(0.05, s["up"])
                    hold(max(0.06, min(3.0, dt)), True)
                    cycles += 1
                continue

            # ── 절정부터는 **실시간**으로 논다.
            #    CSS 전환(페이드)은 벽시계로 돌아가므로 손으로 밀면 안 된다.
            if gp in ("drowse", "sleep", "push"):
                if "dz0" not in marks:
                    marks.add("dz0")
                    print("DROWSE START prog=%.4f bag=%.3f crew=%d t=%.1f cycles=%d"
                          % (s["prog"], s["bag"], s["crew"], s["t"], cycles))
                if gp == "drowse":
                    want = (a.drowse == "hold" and s["load"] < s["danger"] - 0.03)
                else:
                    want = False
                pg.evaluate("(d) => window.__SHOT.press(d)", want)
                pg.wait_for_timeout(120)
                s2 = st()
                if s2["gphase"] == "drowse":
                    if "dz0s" not in marks and s2["drowse"] > 0.10:
                        marks.add("dz0s"); shot("drowse-enter")
                    if "dz1" not in marks and s2["drowse"] > 0.50:
                        marks.add("dz1"); shot("drowse-half")
                    if "dz2" not in marks and s2["drowse"] > 0.88:
                        marks.add("dz2"); shot("drowse-late")
                elif s2["gphase"] == "sleep":
                    if "sl0" not in marks and s2["sleepT"] > 0.25:
                        marks.add("sl0"); shot("collapse")
                    if "sl" not in marks and s2["sleepT"] > 1.25:
                        marks.add("sl"); shot("asleep-black")
                elif s2["gphase"] == "push":
                    if "pu" not in marks and s2["pushT"] > 1.2:
                        marks.add("pu"); shot("pushed-back")
                continue

            hold(0.2, False)

        pg.wait_for_timeout(1400)
        s = st()
        print("FINAL " + json.dumps({k: s.get(k) for k in
              ("t", "prog", "reached", "landed", "remain", "crew", "swept",
               "tears", "golds", "cycles", "flaps", "bag", "drowse")},
              ensure_ascii=False))
        r = pg.evaluate("() => (window.__SHOT.state()||{}).result || null")
        print("RESULT " + json.dumps(r, ensure_ascii=False))
        card = pg.evaluate("() => window.__SHOT.card()")
        print("CARD " + json.dumps(card, ensure_ascii=False))
        top = pg.evaluate("() => { var e=document.querySelector('.st2 .top');"
                          " return e ? e.innerText.replace(/\\n/g,' | ') : null; }")
        print("TOPBAR " + json.dumps(top, ensure_ascii=False))
        shot("card")
        b.close()
    httpd.shutdown()

    print(f"--- {len(errors)} console error(s) ---")
    for e in errors[:10]:
        print("  ", e[:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
