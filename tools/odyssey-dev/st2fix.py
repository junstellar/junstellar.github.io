#!/usr/bin/env python
"""
2편 「바람 자루」 절정 검증.

  table  — 졸음 구간의 4가지 정책을 **실제 입력 경로**(OD.St2.auto)로 각각 돌려
           최종 도달(landed)·잃은 부하를 잰다. 시키는 대로 한 것이 최선이어야 한다.
  probe  — 실시간으로 절정까지 몰고 가며 붉은 배너/잠드는 문장/되밀림 문구를
           DOM 으로 찍고 스크린샷을 남긴다.

  python st2fix.py --mode table
  python st2fix.py --mode probe --drowse obey --out p_obey
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"

POLICIES = [
    ("let",   "손 뗌"),
    ("obey",  "시키는 대로 계속 누름"),
    ("avoid", "누르되 빨간 구간만 피함"),
    ("band",  "골드밴드 유지"),
]

# 화면에 실제로 보이는가 — opacity/visibility 를 조상까지 훑는다
VIS_JS = """(sel) => {
  var e = document.querySelector(sel);
  if (!e) return { there: false };
  var op = 1, n = e, hidden = false;
  while (n && n.nodeType === 1) {
    var cs = getComputedStyle(n);
    op *= parseFloat(cs.opacity);
    if (cs.visibility === 'hidden' || cs.display === 'none') hidden = true;
    n = n.parentElement;
  }
  var r = e.getBoundingClientRect();
  return { there: true, op: +op.toFixed(3), hidden: hidden,
           txt: (e.innerText || '').replace(/\\n/g, ' / ').trim(),
           top: Math.round(r.top), bot: Math.round(r.bottom),
           mid: Math.round((r.top + r.bottom) / 2) };
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


def boot(p, a, errors):
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"
    b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                "--hide-scrollbars", "--mute-audio"])
    ctx = b.new_context(viewport={"width": a.w, "height": a.h}, device_scale_factor=1)
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
    pg.on("console", lambda m: errors.append(f"[console] {m.text}")
          if m.type == "error" else None)
    pg.goto(url, wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true", timeout=60000)
    pg.wait_for_timeout(500)
    pg.evaluate("() => window.__SHOT.stage(1)")
    pg.wait_for_timeout(500)
    return b, httpd, pg


# ────────────────────────────────────────────────────────────── table
def run_table(pg, maxsec):
    rows = []
    for key, label in POLICIES:
        pg.evaluate("() => { window.__SHOT.retry(); }")
        pg.wait_for_timeout(120)
        r = pg.evaluate(
            "([p, m]) => { var st = window.OD.St2.auto('gold', m, true, {drowse: p});"
            " return JSON.parse(JSON.stringify(st.result || st)); }",
            [key, maxsec])
        rows.append((key, label, r))
    return rows


SWEEP_JS = """() => {
  var St2 = window.OD.St2;
  var POL = ['let', 'obey', 'avoid', 'band'];
  var seeds = [20260813, 4242, 777, 31337, 90210, 5150, 1123, 8888];
  var lats = [0.12, 0.16, 0.22];
  var agg = {}, runs = 0, obeyOk = 0, obeyTop = 0;
  POL.forEach(function (k) { agg[k] = { landed: 0, lost: 0, n: 0, win: 0 }; });
  seeds.forEach(function (s) { lats.forEach(function (lat) {
    var row = {};
    POL.forEach(function (k) {
      var r = St2.simulate({ policy: 'gold', drowse: k, seed: s, lat: lat,
                             crew: 600, maxSec: 400 });
      row[k] = r; agg[k].landed += r.landed; agg[k].lost += r.crewLost; agg[k].n++;
    });
    var best = POL.reduce(function (a, b) { return row[a].landed >= row[b].landed ? a : b; });
    agg[best].win++; runs++;
    if (row.obey.landed >= row['let'].landed && row.obey.crewLost <= row['let'].crewLost) obeyOk++;
    if (best === 'obey') obeyTop++;
  }); });
  return { agg: agg, runs: runs, obeyOk: obeyOk, obeyTop: obeyTop };
}"""


def run_sweep(pg):
    d = pg.evaluate(SWEEP_JS)
    names = dict(POLICIES)
    print(f"\n== 순수 규칙 스윕 (씨앗 8 x 반응지연 3 = {d['runs']}판) ==")
    print(f"{'정책':<26}{'landed 평균':>13}{'잃은 부하 평균':>15}{'최고 횟수':>10}")
    for key, label in POLICIES:
        a = d["agg"][key]
        print(f"{label:<24}{a['landed'] / a['n'] * 100:>11.1f}%"
              f"{a['lost'] / a['n']:>15.1f}{a['win']:>10}")
    print(f"  obey 가 let 보다 (더 멀리 && 덜 잃음): {d['obeyOk']}/{d['runs']}판")
    print(f"  obey 가 4정책 중 1위: {d['obeyTop']}/{d['runs']}판")
    return d


def run_endcard(p, a, errors):
    """단독 하네스(st2.html, endPanel:true)에서 두 결말의 결과 카드를 찍는다."""
    port, httpd = serve(ROOT)
    b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                "--hide-scrollbars", "--mute-audio"])
    pg = b.new_context(viewport={"width": a.w, "height": a.h},
                       device_scale_factor=1).new_page()
    pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
    pg.on("console", lambda m: errors.append(f"[console] {m.text}")
          if m.type == "error" else None)
    pg.goto(f"http://127.0.0.1:{port}/odyssey/st2.html", wait_until="domcontentloaded")
    pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true", timeout=60000)
    pg.wait_for_timeout(400)
    for pol, dz, tag in [("gold", "obey", "slept"), ("hold", "obey", "ranout"),
                         ("greedy", "obey", "greedy")]:
        r = pg.evaluate("([p, d]) => JSON.parse(JSON.stringify("
                        "window.__SHOT.auto(p, 320, {drowse: d}).result || {}))", [pol, dz])
        pg.wait_for_timeout(900)
        card = pg.evaluate("() => { var e = document.querySelector('.st2 .end');"
                           " return e ? e.innerText.replace(/\\n/g, ' | ') : null; }")
        fl = pg.evaluate(VIS_JS, ".st2 .flash")
        top = pg.evaluate("() => { var e = document.querySelector('.st2 .top');"
                          " return e ? e.innerText.replace(/\\n/g, ' ') : null; }")
        print(f"\n  [{tag}] ranOut={r.get('ranOut')} slept={r.get('slept')} "
              f"landed={r.get('landed')} remain={r.get('remain')} "
              f"crewLost={r.get('crewLost')} tears={r.get('tears')}")
        print(f"    TOPBAR {top}")
        print(f"    CARD   {card}")
        print(f"    flash op={fl.get('op')} (카드 위에 남으면 안 된다)")
        pg.screenshot(path=os.path.join(a.out, f"end-{tag}.png"))
        pg.evaluate("() => window.__SHOT.reset()")
        pg.wait_for_timeout(300)
    b.close(); httpd.shutdown()


def print_table(rows, title):
    print("\n== " + title + " ==")
    print(f"{'정책':<26}{'최종도달(landed)':>17}{'모닥불(reached)':>16}"
          f"{'잃은부하':>9}{'찢어짐':>7}{'자루':>7}{'금색':>6}")
    best = max(rows, key=lambda r: r[2].get("landed", 0))
    for key, label, r in rows:
        mark = "  ★" if r is best[2] else ""
        print(f"{label:<24}{r.get('landed', 0) * 100:>15.1f}%"
              f"{r.get('reached', 0) * 100:>15.1f}%"
              f"{r.get('crewLost', 0):>9}{r.get('tears', 0):>7}"
              f"{r.get('bag', 0):>7.2f}{r.get('golds', 0):>6}{mark}")
    return best


# ────────────────────────────────────────────────────────────── probe
def run_probe(pg, a, out):
    shots = [0]

    def st():
        return pg.evaluate("() => window.OD.St2.state()")

    def hold(sec, down):
        pg.evaluate("([s,d]) => window.__SHOT.hold(s,d)", [max(0.02, sec), bool(down)])

    def vis(sel):
        return pg.evaluate(VIS_JS, sel)

    def shot(tag, note=""):
        shots[0] += 1
        path = os.path.join(out, f"{shots[0]:02d}-{tag}.png")
        pg.screenshot(path=path)
        f, s2, c = vis(".st2 .flash"), vis(".st2 .slept"), vis(".od-scrim")
        print(f"  SHOT {path} {note}")
        print(f"       flash op={f.get('op')} mid={f.get('mid')} txt={f.get('txt')!r}")
        print(f"       slept op={s2.get('op')} mid={s2.get('mid')} txt={s2.get('txt')!r}")
        if c.get("there"):
            print(f"       card  op={c.get('op')}")
        return path

    # ── 1) 본편 바다 — 게이지를 보고 참았다 놓기 ────────────────────
    marks, cycles = set(), 0
    while True:
        s = st()
        if not s.get("ready") or s.get("phase") != "run":
            break
        if s["t"] > a.maxsec:
            print("  TIMEOUT t=", s["t"]); break
        if s["gphase"] != "run":
            break
        if s["fix"] > 0:
            hold(s["fix"] + 0.06, False); continue
        if s["bag"] <= 0:
            hold(0.5, False); continue
        lo, hi = s["band"]
        aim = lo + (hi - lo) * 0.55
        bump = 0.0
        if s["waveIn"] < 0.45 and s["waveAmp"] > 0:
            bump = s["waveAmp"] * (0.30 + 0.70 * s["fill"])
        if s["load"] > 0.07:
            hold(min(1.2, (s["load"] - 0.04) / 0.86), False)
        else:
            dt = (aim - bump - s["load"]) / max(0.05, s["up"])
            hold(max(0.06, min(3.0, dt)), True)
            cycles += 1

    s = st()
    print(f"  DROWSE START prog={s['prog']:.4f} bag={s['bag']:.3f} crew={s['crew']} "
          f"t={s['t']:.1f} cycles={cycles} tears={s['tears']}")

    # ── 2) 절정 — 실시간. CSS 전환은 벽시계로 돈다. ────────────────
    #    사람처럼 진짜로 누른다: 마우스를 눌러 둔 채 둔다.
    cx, cy = a.w / 2, a.h * 0.62
    holding = False
    banner_seen = []          # (phase, drowse/sleepT/pushT, flash txt, op)
    for i in range(700):
        s = st()
        if s.get("phase") != "run":
            break
        gp = s["gphase"]
        want = False
        if gp == "drowse":
            if a.drowse == "obey":
                want = True
            elif a.drowse == "avoid":
                want = s["load"] < s["danger"] - 0.05
            elif a.drowse == "band":
                want = s["load"] < (s["band"][0])
        if a.input == "poll":
            # 답답해서 계속 눌러 대는 손 — 원래 배너가 눌어붙던 경로
            pg.evaluate("(d) => window.__SHOT.press(d)", want)
        elif want and not holding:
            pg.mouse.move(cx, cy); pg.mouse.down(); holding = True
        elif not want and holding:
            pg.mouse.up(); holding = False
        pg.wait_for_timeout(90)

        s2 = st()
        f = vis(".st2 .flash")
        if f.get("op", 0) > 0.05:
            banner_seen.append((s2["gphase"],
                                round(s2.get("drowse", 0), 2),
                                round(s2.get("sleepT", 0), 2),
                                round(s2.get("pushT", 0), 2),
                                f.get("txt"), f.get("op")))
        gp2 = s2["gphase"]
        if gp2 == "drowse":
            if "d0" not in marks and s2["drowse"] > 0.12:
                marks.add("d0"); shot("drowse-enter", f"drowse={s2['drowse']:.2f}")
            if "d1" not in marks and s2["drowse"] > 0.55:
                marks.add("d1"); shot("drowse-half", f"drowse={s2['drowse']:.2f}")
            if "d2" not in marks and s2["drowse"] > 0.90:
                marks.add("d2"); shot("drowse-late", f"drowse={s2['drowse']:.2f}")
        elif gp2 == "sleep":
            if holding:
                pg.mouse.up(); holding = False
            if "s0" not in marks and s2["sleepT"] > 0.30:
                marks.add("s0"); shot("collapse", f"sleepT={s2['sleepT']:.2f}")
            if "s1" not in marks and s2["sleepT"] > 1.30:
                marks.add("s1"); shot("asleep-black", f"sleepT={s2['sleepT']:.2f}")
            if "s2" not in marks and s2["sleepT"] > 2.10:
                marks.add("s2"); shot("asleep-late", f"sleepT={s2['sleepT']:.2f}")
        elif gp2 == "push":
            if "p0" not in marks and s2["pushT"] > 0.25:
                marks.add("p0"); shot("push-early", f"pushT={s2['pushT']:.2f}")
            if "p1" not in marks and s2["pushT"] > 1.00:
                marks.add("p1"); shot("push-climax", f"pushT={s2['pushT']:.2f}")
            if "p2" not in marks and s2["pushT"] > 2.20:
                marks.add("p2"); shot("push-late", f"pushT={s2['pushT']:.2f}")
    if holding:
        pg.mouse.up()

    pg.wait_for_timeout(1600)
    shot("card-1s")
    pg.wait_for_timeout(4000)
    shot("card-5s")

    s = st()
    print("  FINAL " + json.dumps({k: s.get(k) for k in
          ("t", "prog", "reached", "landed", "remain", "crew", "swept",
           "tears", "golds", "bag", "drowse")}, ensure_ascii=False))
    r = pg.evaluate("() => (window.__SHOT.state()||{}).result || null")
    print("  RESULT " + json.dumps(r, ensure_ascii=False))
    card = pg.evaluate("() => window.__SHOT.card()")
    print("  CARD " + json.dumps(card.get("text", "").replace("\n", " | "),
                                 ensure_ascii=False))

    # 배너 타임라인 요약
    print("  ── 배너가 떠 있던 구간 ──")
    prev = None
    for row in banner_seen:
        key = (row[0], row[4])
        if key != prev:
            print(f"     {row[0]:<7} dz={row[1]:<5} sl={row[2]:<5} pu={row[3]:<5} "
                  f"op={row[5]} {row[4]!r}")
            prev = key
    if not banner_seen:
        print("     (없음)")
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="table",
                    choices=["table", "probe", "sweep", "endcard"])
    ap.add_argument("--drowse", default="obey", choices=[k for k, _ in POLICIES])
    ap.add_argument("--input", default="hold", choices=["hold", "poll"])
    ap.add_argument("--out", default="fix_out")
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    ap.add_argument("--maxsec", type=float, default=300)
    ap.add_argument("--title", default="실측")
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    from playwright.sync_api import sync_playwright
    errors = []
    with sync_playwright() as p:
        if a.mode == "endcard":
            run_endcard(p, a, errors)
            print(f"--- {len(errors)} console error(s) ---")
            for e in errors[:10]:
                print("  ", e[:300])
            return 0
        b, httpd, pg = boot(p, a, errors)
        try:
            if a.mode == "table":
                rows = run_table(pg, a.maxsec)
                print_table(rows, a.title)
            elif a.mode == "sweep":
                run_sweep(pg)
            else:
                print(f"== probe drowse={a.drowse} ==")
                run_probe(pg, a, a.out)
        finally:
            b.close(); httpd.shutdown()
    print(f"--- {len(errors)} console error(s) ---")
    for e in errors[:10]:
        print("  ", e[:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
