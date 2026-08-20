# -*- coding: utf-8 -*-
"""ComfyUI + SDXL local-install short (KO/EN). Same IDE/terminal design system
as the Redmine edition (generate_lang.py, IDE theme v5.2): background #0C0D10 +
dot grid, window tab bar (traffic lights + filename), palette, panels, subtitle
bar, fonts (NotoSansKR-VF for headlines/Korean, Consolas for code/mono,
seguisym for symbols), 0.5s crossfades, narration at scene-start+0.3s.

ONLY the scene content is this topic; every design constant is reused verbatim.
Usage: py -3.12 generate_comfyui.py ko|en

Timeline (30fps, xfade 0.5s x5), from actual narration durations:
  KO narr = 14.736 / 12.048 / 15.288 / 10.152 / 12.000 / 6.744
  EN narr =  9.696 /  9.864 / 11.112 /  9.288 /  9.240 / 4.656
  budgets KO = 468/387/485/331/386/225 (total 2282f, video 73.5667s)
  budgets EN = 317/322/359/305/303/163 (total 1769f, video 56.4667s)
Assembly: render_comfyui.sh (clone of render_v6.sh with these offsets).
"""
import os, sys, json
from PIL import Image, ImageDraw, ImageFont

LANG = sys.argv[1]
assert LANG in ("ko", "en")
KO = LANG == "ko"

ROOT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(ROOT, f"frames_comfy_{LANG}")
os.makedirs(FR, exist_ok=True)

W, H = 1080, 1920
FPS = 30.0

# ---------------- IDE theme v5 palette (from generate_lang.py) ----------------
BG      = (12, 13, 16)
GRID    = (24, 26, 32)
PANEL   = (18, 20, 27)
PBORD   = (34, 39, 52)
TABBAR  = (17, 19, 24)
WHITE   = (233, 237, 243)
MUT     = (122, 132, 147)
DIM     = (90, 99, 112)
GREEN   = (63, 185, 80)
BLUE    = (88, 166, 255)
STRING  = (226, 178, 120)
RED     = (240, 92, 97)
PURPLE  = (188, 140, 255)

NOTO  = "C:/Windows/Fonts/NotoSansKR-VF.ttf"
MONO  = "C:/Windows/Fonts/consola.ttf"
MONOB = "C:/Windows/Fonts/consolab.ttf"
SYM   = "C:/Windows/Fonts/seguisym.ttf"
EMOJI = "C:/Windows/Fonts/seguiemj.ttf"

X = 96  # left margin

# ---------------- assets (absolute paths) ----------------
ASSETS = os.path.join(ROOT, os.pardir, "comfyui-assets")
COVER  = os.path.join(ROOT, os.pardir, "cover-art", "comfy-cover-a.png")
SEOUL  = os.path.join(ASSETS, "seoul.png")
CAT    = os.path.join(ASSETS, "cat.png")

_nc = {}
def fnoto(size, wght=700):
    k = (size, wght)
    if k not in _nc:
        f = ImageFont.truetype(NOTO, size)
        try:
            f.set_variation_by_axes([wght])
        except Exception:
            pass
        _nc[k] = f
    return _nc[k]

_mc = {}
def fmono(size, bold=False):
    k = (size, bold)
    if k not in _mc:
        _mc[k] = ImageFont.truetype(MONOB if bold else MONO, size)
    return _mc[k]

_sc = {}
def fother(path, size):
    k = (path, size)
    if k not in _sc:
        _sc[k] = ImageFont.truetype(path, size)
    return _sc[k]


def base(label):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for gy in range(260, 1650, 46):
        for gx in range(24, W, 46):
            d.point((gx, gy), fill=GRID)
    d.rectangle([0, 250, W, 338], fill=TABBAR)
    d.line([0, 338, W, 338], fill=(28, 31, 40), width=2)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([70 + i * 46, 281, 70 + i * 46 + 26, 307], fill=c)
    d.text((232, 279), label, font=fmono(30), fill=DIM)
    return img, d


def panel(d, x0, y0, x1, y1):
    d.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=PANEL, outline=PBORD, width=2)


def distribute(total, weights):
    """Split `total` frames across states proportional to weights, summing exact."""
    s = float(sum(weights))
    raw = [total * w / s for w in weights]
    fl = [int(x) for x in raw]
    rem = total - sum(fl)
    order = sorted(range(len(weights)), key=lambda i: raw[i] - fl[i], reverse=True)
    for i in range(rem):
        fl[order[i]] += 1
    return fl


# ---------------- cover-art helpers ----------------
def _cover_crop(im, tw, th, yoff_frac=0.42):
    iw, ih = im.size
    s = max(tw / iw, th / ih)
    nw, nh = int(iw * s), int(ih * s)
    im = im.resize((nw, nh))
    left = (nw - tw) // 2
    top = int((nh - th) * yoff_frac)
    return im.crop((left, top, left + tw, top + th))

def art_card(img, path, x0, y0, x1, y1, radius=26, yoff=0.42):
    cw, ch = x1 - x0, y1 - y0
    art = Image.open(path).convert("RGB")
    art = _cover_crop(art, cw, ch, yoff)
    mask = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, cw, ch], radius=radius, fill=255)
    img.paste(art, (x0, y0), mask)
    ImageDraw.Draw(img).rounded_rectangle(
        [x0, y0, x1, y1], radius=radius, outline=PBORD, width=2)


# ---------------- subtitles (full narration text; timing from WordBoundary) ----------------
FRAGS_KO = {
    1: ["클로드의 유일한 아쉬움, 그림을 못 그린다는 거였죠.",
        "노트북 GPU로 도는 오픈웨이트 모델을 붙였더니, 퀄리티가 기대 이상이었어요."],
    2: ["클라우드 API는 돈 들고 워터마크도 박혀요.",
        "그래서 무료에 무제한, 오프라인인 ComfyUI를 골랐습니다."],
    3: ["필요한 건 GPU 메모리 8기가.",
        "요즘 웬만한 그래픽카드면 충분하고, 한 장에 약 30초면 나와요."],
    4: ["받고, 깔고, 모델 내려받아 서버 켜면 끝.",
        "클로드가 호출할 스크립트만 붙이면 됩니다."],
    5: ["스킬 하나 등록하면, '고양이 그려줘' 한마디로 생성까지 알아서.",
        "설치법은 설명란에 있어요."],
    6: ["무료로, 내 PC에서.",
        "여러분도 직접 붙여보세요."],
}
FRAGS_EN = {
    1: ["The one thing Claude couldn't do was draw.",
        "So I ran an open-weight model on my laptop GPU — and the quality blew me away."],
    2: ["Cloud APIs cost money and add watermarks.",
        "So I picked ComfyUI: free, unlimited, offline."],
    3: ["You just need 8 GB of GPU memory.",
        "Most modern cards clear it, and it's about 30 seconds an image."],
    4: ["Clone it, install GPU PyTorch, grab the model, run the server.",
        "Then add a script for Claude to call."],
    5: ["Register one skill, say 'draw a cat', and Claude generates it.",
        "Full setup's in the description."],
    6: ["Free, on your own PC.",
        "Go wire it up yourself."],
}
FRAGS = FRAGS_KO if KO else FRAGS_EN
with open(os.path.join(ROOT, "subs_comfy.json"), encoding="utf-8") as f:
    SUB_START = {int(k): v for k, v in json.load(f)[LANG].items()}

SUB_CY = 1500
SUB_MAXW = 900

def wrap_sub(text, f):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= SUB_MAXW:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [text]

def draw_subtitle(img, text):
    f = fnoto(43, 500)
    lines = wrap_sub(text, f)
    lh = 57
    box_h = lh * len(lines) + 42
    by0 = SUB_CY - box_h // 2
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle(
        [88, by0, W - 88, by0 + box_h], radius=20, fill=(0, 0, 0, 165))
    img2 = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(img2)
    ty = by0 + 21 + lh // 2
    for ln in lines:
        d.text((W // 2, ty), ln, font=f, fill=WHITE, anchor="mm")
        ty += lh
    return img2

scenes = {}
def save(img, scene_no, name, frames):
    p = os.path.join(FR, f"s{scene_no}_{name}.png")
    img.save(p)
    scenes.setdefault(f"s{scene_no}", []).append((p, frames))


# ================================================================
# per-language text pieces
# ================================================================
if KO:
    S2_HEAD = "무료 · 무제한 · 오프라인"
    S3_BADGE = "RTX 4060 · 8GB"
    S3_HEAD = "한 장에 약 30초"
    S5_HEAD = "설치법은 설명란에"
    S6_SUB  = "AI 도구로 시작하세요"
    CAP4    = "받고 · 깔고 · 켜면 끝"
    FOOT4   = "* 설치 명령은 실제 절차, 생성 출력은 실제 캡처"
else:
    S2_HEAD = "Free · unlimited · offline"
    S3_BADGE = "RTX 4060 · 8GB"
    S3_HEAD = "~30s per image"
    S5_HEAD = "Setup guide in the description"
    S6_SUB  = "Start with an AI tool"
    CAP4    = "Clone, install, run"
    FOOT4   = "* Commands are the real steps; output is a real capture"

# ASCII comments/labels -> Consolas (identical for both langs)
S1_KICK = "# comfyui × sdxl"     # x = U+00D7 multiplication sign
S2_KICK = "# cloud vs local"
S3_KICK = "# will my PC run it?"

# ================================================================
# frame budgets
# ================================================================
# scene totals (frames) from actual narration durations, 30fps
if KO:
    TOT = {1: 362, 2: 309, 3: 283, 4: 245, 5: 270, 6: 191}
    S3REV = dict(base=35, r1=30, r2=30, r3=35)   # spec-row reveal cadence
else:
    TOT = {1: 243, 2: 237, 3: 220, 4: 225, 5: 202, 6: 125}
    S3REV = dict(base=28, r1=24, r2=24, r3=28)

def _split(scene):
    """Two-stage split: stage a = subtitle frag-2 start (clamped so stage b >= 50
    and stage a >= 30), stage b = remainder."""
    total = TOT[scene]
    a = SUB_START[scene][1] if len(SUB_START[scene]) > 1 else total // 2
    a = max(30, min(a, total - 50))
    return a, total - a

_s2a, _s2b = _split(2)
_s5a, _s5b = _split(5)
_s6a, _s6b = _split(6)
_s3rev = S3REV["base"] + S3REV["r1"] + S3REV["r2"] + S3REV["r3"]
B = dict(s1=TOT[1], s2a=_s2a, s2b=_s2b,
         s3base=S3REV["base"], s3r1=S3REV["r1"], s3r2=S3REV["r2"], s3r3=S3REV["r3"],
         s3fin=TOT[3] - _s3rev,
         s4=TOT[4], s5a=_s5a, s5b=_s5b, s6a=_s6a, s6b=_s6b)


# ---------------- Scene 1 : hook (static cover-art card) ----------------
def scene1():
    img, d = base("comfyui  —  local")
    art_card(img, COVER, X, 372, W - X, 952, yoff=0.30)
    d = ImageDraw.Draw(img)
    d.text((X, 1006), S1_KICK, font=fmono(32), fill=GREEN)
    fh = fnoto(71, 800)
    if KO:
        d.text((X, 1074), "노트북 GPU로,", font=fh, fill=WHITE)
        d.text((X, 1176), "Claude", font=fh, fill=BLUE)
        xw = d.textlength("Claude", font=fh)
        d.text((X + xw, 1176), "가 그린다", font=fh, fill=WHITE)
    else:
        d.text((X, 1074), "Claude couldn't draw.", font=fh, fill=WHITE)
        d.text((X, 1176), "Now it can — ", font=fh, fill=WHITE)
        xw = d.textlength("Now it can — ", font=fh)
        d.text((X + xw, 1176), "locally", font=fh, fill=BLUE)
    return img

save(scene1(), 1, "a", B["s1"])


# ---------------- Scene 2 : why local (compare panel, two-stage) ----------------
def scene2(full):
    img, d = base("why-local.md")
    d.text((X, 470), S2_KICK, font=fmono(34), fill=GREEN)
    panel(d, X, 560, W - X, 1000)
    fm = fmono(34)
    lx = X + 44
    def row(label, arrow_col, rest, rest_col, y):
        d.text((lx, y), label, font=fm, fill=MUT)
        d.text((lx + 178, y), "→", font=fm, fill=arrow_col)
        d.text((lx + 236, y), rest, font=fm, fill=rest_col)
    row("cloud", DIM, "$/image · watermark · online", MUT, 632)
    d.line([lx, 762, W - X - 44, 762], fill=PBORD, width=2)
    row("local", DIM, "free · unlimited · offline", GREEN, 852)
    if full:
        d.text((X, 1120), S2_HEAD, font=fnoto(56, 700), fill=WHITE)
    return img

save(scene2(False), 2, "a", B["s2a"])
save(scene2(True),  2, "b", B["s2b"])


# ---------------- Scene 3 : specs + speed (row reveal) ----------------
SPEC_ROWS = [
    ("GPU VRAM", "8GB"),
    ("RAM",      "16GB"),
    ("disk",     "~20GB"),
]

def scene3(nrows, final=False):
    img, d = base("specs")
    # RED rounded badge (Noto)
    ft = fnoto(32, 700)
    bw = d.textlength(S3_BADGE, font=ft) + 56
    d.rounded_rectangle([X, 398, X + bw, 462], radius=32, outline=RED, width=2)
    d.text((X + 28, 412), S3_BADGE, font=ft, fill=(240, 150, 150))
    d.text((X, 512), S3_KICK, font=fmono(33), fill=GREEN)
    panel(d, X, 590, W - X, 1030)
    fm = fmono(40)
    fsym = fother(SYM, 40)
    lx, ly = X + 46, 648
    for i in range(nrows):
        name, val = SPEC_ROWS[i]
        y = ly + i * 116
        d.text((lx, y), name, font=fm, fill=WHITE)
        d.text((lx + 300, y), val, font=fm, fill=STRING)
        d.text((lx + 560, y - 2), "✓", font=fsym, fill=GREEN)
    if final:
        d.text((X, 1120), S3_HEAD, font=fnoto(58, 800), fill=WHITE)
    return img

save(scene3(0), 3, "base", B["s3base"])
save(scene3(1), 3, "r1", B["s3r1"])
save(scene3(2), 3, "r2", B["s3r2"])
save(scene3(3), 3, "r3", B["s3r3"])
save(scene3(3, final=True), 3, "fin", B["s3fin"])


# ============ Scene 4 : install terminal (typing animation, real capture) ============
PROMPT = "PS C:\\> "
S4_SCRIPT = [
    ("cmd", "git clone --depth 1 https://github.com/comfyanonymous/ComfyUI C:\\ComfyUI"),
    ("out", ("Cloning into 'C:\\ComfyUI'... done.", MUT)),
    ("cmd", "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128"),
    ("out", ("Successfully installed torch-2.6.0+cu128 torchvision torchaudio", MUT)),
    ("cmd", "python -c \"import torch; print(torch.cuda.is_available())\""),
    ("out", ("True", GREEN)),
    ("cmd", "python generate.py \"Seoul city skyline at sunset ...\""),
    ("out", ("SAVED ...\\seoul.png  (seed 2026, 30s)", BLUE)),
]

TX0, TX1 = 60, W - 60
TY0 = 380
TPAD = 30
TLH = 44
MAXROWS = 16
tmono = fmono(30)
CHW = tmono.getlength("x")
COLS = int((TX1 - TX0 - 2 * TPAD) // CHW)
TBODY_H = MAXROWS * TLH + 2 * TPAD
TY1 = TY0 + TBODY_H

def wrapc(s):
    if not s:
        return [""]
    return [s[i:i + COLS] for i in range(0, len(s), COLS)]

def draw_terminal(lines, cursor=False, caption=False):
    """lines = list of (text, color). Each wraps to COLS. Optional block cursor
    at the end of the last visual row; optional caption/footnote below panel."""
    img, d = base("Windows PowerShell")
    panel(d, TX0, TY0, TX1, TY1)
    visual = []
    for text, color in lines:
        for ln in wrapc(text):
            visual.append((ln, color))
    cur_rc = None
    if cursor and visual:
        cur_rc = (len(visual) - 1, len(visual[-1][0]))
    scroll = max(0, len(visual) - MAXROWS)
    visual = visual[scroll:]
    if cur_rc is not None:
        cur_rc = (cur_rc[0] - scroll, cur_rc[1])
    x0 = TX0 + TPAD
    y = TY0 + TPAD + TLH // 2
    for ri, (text, color) in enumerate(visual):
        d.text((x0, y + ri * TLH), text, font=tmono, fill=color, anchor="lm")
    if cur_rc is not None and cur_rc[0] >= 0:
        ri, ci = cur_rc
        cx = x0 + CHW * ci
        d.rectangle([cx + 2, y + ri * TLH - 17, cx + 2 + CHW, y + ri * TLH + 17], fill=WHITE)
    if caption:
        d.text((W // 2, TY1 + 74), CAP4, font=fnoto(50, 700), fill=WHITE, anchor="mm")
        d.text((W // 2, TY1 + 148), FOOT4, font=fnoto(28, 400), fill=DIM, anchor="mm")
    return img

# --- build S4 animation as (image, weight) states, then distribute frames ---
s4_states = []   # (image, weight)
committed = []   # list of (text, color)
TYPE_STEPS = 4
saved_seen = [False]  # caption shows once the SAVED line is printed

def add_state(lines, cursor, weight):
    cap = saved_seen[0]
    s4_states.append((draw_terminal(lines, cursor=cursor, caption=cap), weight))

# opening prompt with blinking cursor
add_state([(PROMPT, WHITE)], True, 3)
for kind, payload in S4_SCRIPT:
    if kind == "cmd":
        cmd = payload
        for st in range(1, TYPE_STEPS + 1):
            n = round(len(cmd) * st / TYPE_STEPS)
            add_state(committed + [(PROMPT + cmd[:n], WHITE)], True, 2)
        committed.append((PROMPT + cmd, WHITE))
        add_state(list(committed), True, 3)     # brief hold on full command
    else:
        text, color = payload
        if "SAVED" in text:
            saved_seen[0] = True
        committed.append((text, color))
        add_state(list(committed), False, 8)    # hold on output
# final: fresh prompt + blinking cursor, caption visible
for i in range(6):
    add_state(committed + [(PROMPT, WHITE)], (i % 2 == 0), 5)

_w = [w for _, w in s4_states]
_fr = distribute(B["s4"], _w)
for i, (img, _) in enumerate(s4_states):
    save(img, 4, f"f{i:03d}", _fr[i])


# ---------------- Scene 5 : result gallery + description CTA (two-stage) ----------------
def scene5(full):
    img, d = base("output/")
    fh = fnoto(60, 800)
    d.text((X, 470), "## gallery", font=fh, fill=WHITE)
    tx = X + d.textlength("## gallery", font=fh) + 28
    bw = d.textlength("SDXL", font=fmono(30, True)) + 48
    d.rounded_rectangle([tx, 486, tx + bw, 540], radius=27, outline=GREEN, width=2)
    d.text((tx + 24, 496), "SDXL", font=fmono(30, True), fill=GREEN)
    # two thumbnails (square-ish cover crop, rounded)
    art_card(img, SEOUL, X, 606, 532, 966, radius=22, yoff=0.42)
    art_card(img, CAT,   548, 606, W - X, 966, radius=22, yoff=0.30)
    d = ImageDraw.Draw(img)
    d.text((X, 1030), "more  →  see description ↓", font=fmono(38, True), fill=GREEN)
    if full:
        d.text((X, 1130), S5_HEAD, font=fnoto(56, 700), fill=WHITE)
    return img

save(scene5(False), 5, "a", B["s5a"])
save(scene5(True),  5, "b", B["s5b"])


# ---------------- Scene 6 : CTA outro (two-stage + blinking cursor) ----------------
def scene6(full, cursor_on=True):
    img, d = base("$ draw")
    d.text((X, 600), "$", font=fmono(64), fill=GREEN)
    if KO:
        d.text((X + 70, 604), "무료로, 내 PC에서", font=fnoto(84, 800), fill=WHITE)
        d.text((X, 744), "직접 붙여보세요", font=fnoto(84, 800), fill=BLUE)
    else:
        d.text((X + 70, 604), "Free, on your PC", font=fnoto(84, 800), fill=WHITE)
        d.text((X, 744), "Wire it up yourself", font=fnoto(84, 800), fill=BLUE)
    if full:
        d.line([X, 900, W - X, 900], fill=PBORD, width=2)
        d.text((X, 950), S6_SUB, font=fnoto(50, 500), fill=MUT)
        d.text((X, 1060), "draw anything", font=fmono(46), fill=GREEN)
        if cursor_on:
            cx = X + d.textlength("draw anything", font=fmono(46)) + 14
            d.rectangle([cx, 1058, cx + 22, 1108], fill=GREEN)
    return img

save(scene6(False), 6, "a", B["s6a"])
def emit_s6b(total):
    chunks, per = [], 15
    t, on = total, True
    while t > 0:
        f = min(per, t)
        chunks.append((f, on))
        t -= f
        on = not on
    return chunks
for idx, (fr, on) in enumerate(emit_s6b(B["s6b"])):
    save(scene6(True, cursor_on=on), 6, f"b{idx:02d}", fr)


# ============ composite timed subtitles + hardlink frame sequences ============
total = 0
for name, items in scenes.items():
    sc = int(name[1:])
    starts, frags = SUB_START[sc], FRAGS[sc]
    seq = os.path.join(ROOT, f"seq_comfy_{LANG}_{name}")
    if os.path.isdir(seq):
        for fname in os.listdir(seq):
            os.remove(os.path.join(seq, fname))
    else:
        os.makedirs(seq)
    n = 0
    cache = {}
    for p, fr in items:
        for _ in range(fr):
            k = sum(1 for s in starts if n >= s) - 1
            key = (p, k)
            if key not in cache:
                sub_p = p[:-4] + f"_sub{k}.png"
                draw_subtitle(Image.open(p), frags[k]).save(sub_p)
                cache[key] = sub_p
            os.link(cache[key], os.path.join(seq, f"{n:05d}.png"))
            n += 1
    total += n
    print(f"{LANG} {name}: {n} frames = {n / FPS:.4f}s, subs at {starts}")
print(f"total {total} frames, video = {total / FPS - 0.5 * (len(scenes) - 1):.4f}s")
print("done", LANG)
