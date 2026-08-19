#!/usr/bin/env python
"""실패 갈래 검증.

  · 3·4·6편 패배 -> 카드에 '다시' 만 (진행 불가) -> 재시도가 되는가
  · 5편 전멸(신화대로) -> '계속' 으로 진행 -> 부하 0 -> 6편은 혼자
  · 에필로그가 '당신도 혼자였습니다' 로 바뀌는가
"""
import functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"
ST = "() => JSON.parse(JSON.stringify(window.__SHOT.state()))"
CARD = "() => JSON.parse(JSON.stringify(window.__SHOT.card()))"
OUT = "fail_out"


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


def btns(pg):
    return pg.evaluate("() => Array.from(document.querySelectorAll('.od-scrim .od-btn'))"
                       ".map(b => b.textContent)")


def main():
    os.makedirs(OUT, exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"
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
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                             timeout=90000)
        pg.wait_for_timeout(800)

        # ── 패배해도 진행되면 안 되는 편들 ────────────────────────────────
        for i, name, js in [
            (2, "sirens", "window.__SHOT.auto('none', 120)"),
            (3, "scylla", "window.__SHOT.auto(0.25, 220)"),
            (5, "bow", "window.__SHOT.skipTo(40, "
                       "(s) => s.gp === 'string' ? s.bend < 0.55 : true)"),
        ]:
            pg.evaluate(f"() => window.__SHOT.stage({i})"); pg.wait_for_timeout(700)
            r = pg.evaluate(f"() => JSON.parse(JSON.stringify({js}))")
            pg.wait_for_timeout(900)
            c = pg.evaluate(CARD)
            pg.screenshot(path=os.path.join(OUT, f"lose_{name}.png"))
            print(f"[{name}] win={(r.get('result') or {}).get('win')} "
                  f"card={c.get('kind')} buttons={btns(pg)}")
            print("   ", json.dumps(c.get("text", "").replace("\n", " | "),
                                    ensure_ascii=False)[:220])
            # 재시도가 실제로 판을 다시 여는가
            pg.wait_for_timeout(450)
            pg.evaluate("() => window.__SHOT.next()")     # 진 판은 pri 가 '다시' 다
            pg.wait_for_timeout(900)
            st = pg.evaluate(ST)
            print(f"    retry -> engine={st.get('engine')} phase={st.get('phase')} "
                  f"card={st.get('card')} crew={st.get('crew')}")

        # ── 5편 전멸 -> 6편은 혼자 -> 에필로그 ────────────────────────────
        pg.evaluate("() => window.__SHOT.stage(4)"); pg.wait_for_timeout(700)
        pg.evaluate("() => window.__SHOT.crew(583)")     # 이월된 인원인 척
        pg.evaluate("() => window.__SHOT.stage(4)"); pg.wait_for_timeout(700)
        r = pg.evaluate("() => JSON.parse(JSON.stringify(window.__SHOT.auto('spam', 220)))")
        pg.wait_for_timeout(900)
        c = pg.evaluate(CARD)
        pg.screenshot(path=os.path.join(OUT, "lose_cattle.png"))
        st = pg.evaluate(ST)
        print(f"\n[cattle 전멸] win={(r.get('result') or {}).get('win')} "
              f"crew={st.get('crew')} buttons={btns(pg)}")
        print("   ", json.dumps(c.get("text", "").replace("\n", " | "),
                                ensure_ascii=False)[:260])

        pg.wait_for_timeout(450)
        pg.evaluate("() => window.__SHOT.next()"); pg.wait_for_timeout(1100)
        st = pg.evaluate(ST)
        print(f"[6편] engine={st.get('engine')} crew={st.get('crew')} "
              f"stCrew={st.get('stCrew')}")
        pg.screenshot(path=os.path.join(OUT, "bow_alone.png"))

        pg.evaluate("() => window.__SHOT.auto(null, 120)"); pg.wait_for_timeout(900)
        pg.wait_for_timeout(450)
        pg.evaluate("() => window.__SHOT.next()"); pg.wait_for_timeout(1100)
        c = pg.evaluate(CARD)
        pg.screenshot(path=os.path.join(OUT, "epilogue_alone.png"))
        print(f"[에필로그] kind={c.get('kind')}")
        print("   ", json.dumps(c.get("text", "").replace("\n", " | "),
                                ensure_ascii=False))
        b.close()
    httpd.shutdown()
    print(f"\n--- {len(errors)} console error(s) ---")
    for e in errors[:12]:
        print("  ", e[:400])
    return 0


if __name__ == "__main__":
    sys.exit(main())
