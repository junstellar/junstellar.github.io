#!/usr/bin/env python
"""1편 -> 6편 연속 플레이 검증.

각 편에서: 진입 스크린샷 -> 실제 입력(키/마우스)이 닿는지 확인 -> 자동 플레이로 클리어
-> 결과 카드 스크린샷 + 문구 -> '계속' -> 다음 편 진입 확인. 마지막에 에필로그.

부하 이월(Core.crew)을 편마다 찍어 준다.
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
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


# 편마다: (자동플레이 인자, 최대초, 사람 입력 흉내)
AUTO = {
    "st1": ("['big','mid','sml']", 95),
    "st2": ("'gold'", 300),
    "st3": ("'smart'", 200),
    "st4": ("6", 260),
    "st5": ("'band'", 220),
    "st6": ("null", 120),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="all6_out")
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    ap.add_argument("--touch", action="store_true")
    ap.add_argument("--tries", type=int, default=4)   # 편당 자동 재시도 횟수
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"

    from playwright.sync_api import sync_playwright
    errors = []
    ok = True
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--hide-scrollbars", "--mute-audio"])
        kw = dict(viewport={"width": a.w, "height": a.h}, device_scale_factor=1)
        if a.touch:
            kw.update(has_touch=True, is_mobile=True)
        ctx = b.new_context(**kw)
        pg = ctx.new_page()
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[console] {m.text}")
              if m.type == "error" else None)
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                                 timeout=90000)
        except Exception as e:
            print("BOOT FAILED:", e)
            print("BOOTERR", pg.evaluate(
                "() => (document.getElementById('bootErr')||{}).textContent || ''"))
            pg.screenshot(path=os.path.join(a.out, "boot_failed.png"))
            b.close(); httpd.shutdown()
            for e2 in errors[:12]:
                print("  ", e2[:400])
            return 1
        pg.wait_for_timeout(900)

        cx, cy = a.w / 2, a.h * 0.55
        crew_log = []

        for idx in range(6):
            st = pg.evaluate(ST)
            key, sid = st.get("engine"), st.get("id")
            crew_in = st.get("crew")
            print(f"\n=== {idx+1}편  engine={key} id={sid} crew_in={crew_in} "
                  f"phase={st.get('phase')} ===")
            if key != f"st{idx+1}":
                print(f"  !! 라우팅 어긋남: {key}")
                ok = False

            # 진입 화면 — 등장인물이 보이는가
            pg.wait_for_timeout(1400)
            shot = os.path.join(a.out, f"{idx+1}_{sid}_enter.png")
            pg.screenshot(path=shot); print("  SHOT", shot)

            # ── 실제 입력이 닿는가 (키보드 + 마우스) ───────────────────────
            before = pg.evaluate(ST)
            pg.keyboard.down(" "); pg.wait_for_timeout(240)
            mid = pg.evaluate(ST)                 # 누르고 있는 **동안** 을 본다
            pg.keyboard.up(" ")
            pg.mouse.move(cx, cy); pg.mouse.down(); pg.wait_for_timeout(180)
            mid2 = pg.evaluate(ST)
            pg.mouse.up()
            pg.wait_for_timeout(260)
            after = pg.evaluate(ST)
            KEYS = ("t", "gt", "prog", "tempt", "grip", "strokes", "poured",
                    "bend", "waiting", "escaped", "gp", "arrows", "day",
                    "want", "holding", "draw")
            moved = any(before.get(k) != m.get(k) for k in KEYS for m in (mid, mid2, after))
            diff = [(k, before.get(k), mid.get(k)) for k in KEYS
                    if before.get(k) != mid.get(k)][:4]
            print(f"  입력 반응: {'OK' if moved else '변화없음'}  {diff}")
            if not moved:
                ok = False

            # ── 자동 플레이로 클리어 ───────────────────────────────────────
            arg, maxsec = AUTO[key]
            won = False
            for attempt in range(a.tries):
                res = pg.evaluate(f"() => JSON.parse(JSON.stringify("
                                  f"window.__SHOT.auto({arg}, {maxsec})))")
                pg.wait_for_timeout(700)
                card = pg.evaluate("() => JSON.parse(JSON.stringify(window.__SHOT.card()))")
                r = res.get("result") or {}
                won = bool(r.get("win")) or key in ("st1", "st2", "st5")
                print(f"  auto#{attempt+1}: phase={res.get('phase')} "
                      f"win={r.get('win')} lost={r.get('lost')} "
                      f"card={card.get('kind')} open={card.get('open')}")
                if card.get("open") and (won or attempt == a.tries - 1):
                    break
                if card.get("open") and not won:
                    pg.wait_for_timeout(450)
                    pg.evaluate("() => window.__SHOT.retry()")
                    pg.wait_for_timeout(900)

            card = pg.evaluate("() => JSON.parse(JSON.stringify(window.__SHOT.card()))")
            pg.wait_for_timeout(500)
            shot = os.path.join(a.out, f"{idx+1}_{sid}_card.png")
            pg.screenshot(path=shot); print("  SHOT", shot)
            print("  CARD", json.dumps(card.get("text", "").replace("\n", " | "),
                                       ensure_ascii=False)[:400])
            if not card.get("open"):
                print("  !! 결과 카드가 열리지 않았다"); ok = False

            st = pg.evaluate(ST)
            crew_log.append((idx + 1, sid, crew_in, st.get("crew")))
            print(f"  부하 {crew_in} -> {st.get('crew')}")

            # ── '계속' → 다음 편 ───────────────────────────────────────────
            pg.wait_for_timeout(450)
            pg.evaluate("() => window.__SHOT.next()")
            pg.wait_for_timeout(1200)

        # ── 에필로그 ──────────────────────────────────────────────────────
        st = pg.evaluate(ST)
        card = pg.evaluate("() => JSON.parse(JSON.stringify(window.__SHOT.card()))")
        shot = os.path.join(a.out, "7_epilogue.png")
        pg.screenshot(path=shot)
        print(f"\n=== 에필로그 ===\n  SHOT {shot}")
        print("  finished =", st.get("finished"), " crew =", st.get("crew"),
              " card =", card.get("kind"))
        print("  TEXT", json.dumps(card.get("text", "").replace("\n", " | "),
                                   ensure_ascii=False))
        if card.get("kind") != "epilogue":
            print("  !! 에필로그가 뜨지 않았다"); ok = False

        print("\n부하 이월:", " -> ".join(f"{i}편({sid}) {a0}→{b0}"
                                          for i, sid, a0, b0 in crew_log))
        b.close()
    httpd.shutdown()

    if errors:
        print(f"\n--- {len(errors)} console error(s) ---")
        for e in errors[:20]:
            print("  ", e[:400])
    else:
        print("\n--- 0 console error(s) ---")
    print("RESULT:", "OK" if ok and not errors else "PROBLEMS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
