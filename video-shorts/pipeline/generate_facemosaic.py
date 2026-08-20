# -*- coding: utf-8 -*-
"""Face-mosaic short (KO/EN). Reuses the ComfyUI/Redmine IDE-terminal design
system verbatim (generate_comfyui.py): BG #0C0D10 + dot grid, window tab bar
(traffic lights + filename), palette, panels, subtitle bar, fonts
(NotoSansKR-VF headlines/Korean, Consolas code/mono, seguisym for check/cross),
0.5s crossfades, narration at scene-start+0.3s. Only scene CONTENT is this topic.

Usage: py -3.12 generate_facemosaic.py ko|en
Also writes render_params_{lang}.sh (xfade offsets, narration delays, DUR/DFO).
Uses real demo assets from ../face-mosaic-assets (AI-generated sample faces).
"""
import os, sys, json
from PIL import Image, ImageDraw, ImageFont

LANG = sys.argv[1]
assert LANG in ("ko", "en")
KO = LANG == "ko"

ROOT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(ROOT, f"frames_facemosaic_{LANG}")
os.makedirs(FR, exist_ok=True)

W, H = 1080, 1920
FPS = 30.0

# ---------------- IDE theme v5 palette (verbatim) ----------------
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

X = 96  # left margin

# ---------------- assets (absolute paths) ----------------
ASSETS   = os.path.join(ROOT, os.pardir, "face-mosaic-assets")
MOSAIC   = os.path.join(ASSETS, "mosaic.png")
DETECTED = os.path.join(ASSETS, "detected.png")
BLUR     = os.path.join(ASSETS, "blur.png")
BOX      = os.path.join(ASSETS, "box.png")
EMOJI    = os.path.join(ASSETS, "emoji.png")

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

def thumb(img, path, x0, y0, size, zoom=0.60, yoff=0.28, radius=18):
    art = Image.open(path).convert("RGB")
    iw, ih = art.size
    cs = int(min(iw, ih) * zoom)
    left = (iw - cs) // 2
    top = int((ih - cs) * yoff)
    art = art.crop((left, top, left + cs, top + cs)).resize((size, size))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=radius, fill=255)
    img.paste(art, (x0, y0), mask)
    ImageDraw.Draw(img).rounded_rectangle(
        [x0, y0, x0 + size, y0 + size], radius=radius, outline=PBORD, width=2)


# ---------------- subtitles ----------------
FRAGS_KO = {
    1: ["사진 올릴 때 같이 찍힌 사람 얼굴, 가려야 할 때 있죠.",
        "서버에 안 올리고 브라우저 안에서만 가리는 도구를 만들었어요."],
    2: ["보통은 모르는 사이트에 얼굴 사진을 올려야 하는데,",
        "이건 사진이 브라우저 밖으로 아예 안 나갑니다."],
    3: ["비결은 온디바이스 AI.",
        "구글 MediaPipe로 얼굴 찾는 것부터 가리는 것까지 전부 내 컴퓨터 안에서 끝나요."],
    4: ["가리는 방식은 넷 — 모자이크, 블러, 검은 박스, 이모지.",
        "놓친 얼굴은 직접 드래그로 추가하면 됩니다."],
    5: ["이것도 Claude Code로 만들었어요.",
        "도구랑 자세한 설명은 설명란에."],
    6: ["보안은 직접 만드는 게 제일 확실하죠.",
        "귀찮으면 제가 만든 거 써보세요."],
}
FRAGS_EN = {
    1: ["When you post a photo, sometimes you need to hide a bystander's face.",
        "So I built a tool that does it entirely in your browser — nothing goes to a server."],
    2: ["Usually you'd upload the face to some random site.",
        "Here, the photo never leaves your browser at all."],
    3: ["The trick is on-device AI.",
        "Google's MediaPipe finds the faces and masks them, all on your own computer."],
    4: ["Four ways to hide: mosaic, blur, black box, or emoji.",
        "Missed a face? Just drag to add it."],
    5: ["I built this with Claude Code too.",
        "The tool and the full write-up are in the description."],
    6: ["For privacy, building your own is the surest bet.",
        "Too much hassle? Just use mine."],
}
FRAGS = FRAGS_KO if KO else FRAGS_EN
with open(os.path.join(ROOT, "subs_facemosaic.json"), encoding="utf-8") as f:
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
    S1_H1, S1_H2a, S1_H2b = "사진 속 얼굴,", "브라우저에서 ", "가린다"
    S2_HEAD = "사진은 브라우저 밖으로 안 나갑니다"
    S3_HEAD = "전부 내 컴퓨터 안에서"
    S4_FOOT = "* 예시 인물은 AI가 생성한 얼굴입니다"
    S4_LBL  = ["모자이크", "블러", "박스", "이모지"]
    S5_HEAD = "Claude Code로 만들었어요"
    S6_H1, S6_H2 = "보안은 직접 만드는 게", "제일 확실하죠"
    S6_SUB  = "귀찮으면 제 걸 쓰세요"
    HEAD2   = 54
    HEAD6   = 76
else:
    S1_H1, S1_H2a, S1_H2b = "Hide faces in photos,", "", "right in the browser"
    S2_HEAD = "Your photo never leaves the browser"
    S3_HEAD = "All on your own machine"
    S4_FOOT = "* The sample person is an AI-generated face"
    S4_LBL  = ["mosaic", "blur", "box", "emoji"]
    S5_HEAD = "Built with Claude Code"
    S6_H1, S6_H2 = "For privacy,", "build your own"
    S6_SUB  = "or just use mine"
    HEAD2   = 46
    HEAD6   = 82

# ASCII kickers/labels -> Consolas (identical for both langs)
S1_KICK = "# on-device privacy"
S2_KICK = "# your photo never leaves the browser"
S3_KICK = "# all on-device"

# ================================================================
# frame budgets  (scene_dur = 0.3 lead + narration + tail)
# ================================================================
if KO:
    TOT = {1: 325, 2: 253, 3: 325, 4: 328, 5: 223, 6: 230}
    S3REV = dict(base=30, r1=28, r2=28, r3=30)
else:
    TOT = {1: 287, 2: 208, 3: 237, 4: 241, 5: 178, 6: 185}
    S3REV = dict(base=26, r1=24, r2=24, r3=26)

def _split(scene):
    total = TOT[scene]
    a = SUB_START[scene][1] if len(SUB_START[scene]) > 1 else total // 2
    a = max(30, min(a, total - 50))
    return a, total - a

_s2a, _s2b = _split(2)
_s4a, _s4b = _split(4)
_s5a, _s5b = _split(5)
_s6a, _s6b = _split(6)
_s3rev = S3REV["base"] + S3REV["r1"] + S3REV["r2"] + S3REV["r3"]
B = dict(s1=TOT[1], s2a=_s2a, s2b=_s2b,
         s3base=S3REV["base"], s3r1=S3REV["r1"], s3r2=S3REV["r2"], s3r3=S3REV["r3"],
         s3fin=TOT[3] - _s3rev,
         s4a=_s4a, s4b=_s4b, s5a=_s5a, s5b=_s5b, s6a=_s6a, s6b=_s6b)


# ---------------- Scene 1 : hook (static cover card = mosaic result) ----------------
def scene1():
    img, d = base("face-mosaic")
    art_card(img, MOSAIC, X, 372, W - X, 952, yoff=0.30)
    d = ImageDraw.Draw(img)
    d.text((X, 1006), S1_KICK, font=fmono(32), fill=GREEN)
    fh = fnoto(71, 800)
    d.text((X, 1074), S1_H1, font=fh, fill=WHITE)
    if S1_H2a:
        d.text((X, 1176), S1_H2a, font=fh, fill=WHITE)
        xw = d.textlength(S1_H2a, font=fh)
        d.text((X + xw, 1176), S1_H2b, font=fh, fill=BLUE)
    else:
        d.text((X, 1176), S1_H2b, font=fh, fill=BLUE)
    return img

save(scene1(), 1, "a", B["s1"])


# ---------------- Scene 2 : privacy (compare panel, two-stage) ----------------
def scene2(full):
    img, d = base("privacy.md")
    d.text((X, 470), S2_KICK, font=fmono(32), fill=GREEN)
    panel(d, X, 560, W - X, 1000)
    fm = fmono(34)
    fsym = fother(SYM, 34)
    lx = X + 44
    def row(label, sym, sym_col, rest, rest_col, y):
        d.text((lx, y), label, font=fm, fill=MUT)
        d.text((lx + 190, y), "->", font=fm, fill=DIM)
        d.text((lx + 258, y - 2), sym, font=fsym, fill=sym_col)
        d.text((lx + 306, y), rest, font=fm, fill=rest_col)
    row("upload",  "✗", RED,   "no server", RED, 632)
    d.line([lx, 762, W - X - 44, 762], fill=PBORD, width=2)
    row("process", "✓", GREEN, "on-device", GREEN, 852)
    if full:
        d.text((X, 1110), S2_HEAD, font=fnoto(HEAD2, 700), fill=WHITE)
    return img

save(scene2(False), 2, "a", B["s2a"])
save(scene2(True),  2, "b", B["s2b"])


# ---------------- Scene 3 : how (steps panel, row reveal) ----------------
STEP_ROWS = [
    "1  load photo -> canvas",
    "2  detect faces (MediaPipe)",
    "3  apply effect",
]
STEP_COL = [BLUE, GREEN, STRING]

def scene3(nrows, final=False):
    img, d = base("how.js")
    d.text((X, 470), S3_KICK, font=fmono(33), fill=GREEN)
    panel(d, X, 560, W - X, 1030)
    fm = fmono(40)
    lx, ly = X + 46, 636
    for i in range(nrows):
        y = ly + i * 122
        d.text((lx, y), STEP_ROWS[i][:3], font=fmono(40, True), fill=STEP_COL[i])
        d.text((lx + 66, y), STEP_ROWS[i][3:], font=fm, fill=WHITE)
    if final:
        d.text((X, 1120), S3_HEAD, font=fnoto(58, 800), fill=WHITE)
    return img

save(scene3(0), 3, "base", B["s3base"])
save(scene3(1), 3, "r1", B["s3r1"])
save(scene3(2), 3, "r2", B["s3r2"])
save(scene3(3), 3, "r3", B["s3r3"])
save(scene3(3, final=True), 3, "fin", B["s3fin"])


# ---------------- Scene 4 : demo (big card detect->mask + 4 effect thumbs) ----------------
THUMB_PATHS = [MOSAIC, BLUR, BOX, EMOJI]

def scene4(stage):
    img, d = base("demo")
    big = DETECTED if stage == 0 else MOSAIC
    art_card(img, big, X, 372, W - X, 862, yoff=0.26)
    d = ImageDraw.Draw(img)
    # step badge top-left inside the big card
    if stage == 0:
        btxt, bcol = "1  detect", BLUE
    else:
        btxt, bcol = "2  mask", GREEN
    bf = fmono(30, True)
    bw = d.textlength(btxt, font=bf) + 44
    d.rounded_rectangle([X + 22, 394, X + 22 + bw, 450], radius=14,
                        fill=(0, 0, 0), outline=bcol, width=2)
    d.text((X + 44, 405), btxt, font=bf, fill=bcol)
    # four effect thumbnails
    size, gap = 200, 29
    yt = 908
    for i, p in enumerate(THUMB_PATHS):
        xx = X + i * (size + gap)
        thumb(img, p, xx, yt, size, zoom=0.58, yoff=0.24)
        lf = fnoto(31, 600)
        d.text((xx + size // 2, yt + size + 30), S4_LBL[i],
               font=lf, fill=WHITE, anchor="mm")
    d.text((X, 1210), S4_FOOT, font=fnoto(27, 400), fill=DIM)
    return img

save(scene4(0), 4, "a", B["s4a"])
save(scene4(1), 4, "b", B["s4b"])


# ---------------- Scene 5 : README + description CTA (two-stage) ----------------
def scene5(full):
    img, d = base("README.md")
    fh = fnoto(58, 800)
    d.text((X, 456), "## face-mosaic", font=fh, fill=WHITE)
    tx = X + d.textlength("## face-mosaic", font=fh) + 26
    bf = fmono(28, True)
    bw = d.textlength("Claude Code", font=bf) + 44
    d.rounded_rectangle([tx, 470, tx + bw, 522], radius=26, outline=GREEN, width=2)
    d.text((tx + 22, 480), "Claude Code", font=bf, fill=GREEN)
    panel(d, X, 566, W - X, 900)
    fm = fmono(30)
    fsym = fother(SYM, 30)
    lx = X + 40
    d.text((lx, 636), "tool", font=fm, fill=MUT)
    d.text((lx + 130, 636), "->", font=fm, fill=DIM)
    d.text((lx + 185, 636), "junstellar.github.io/tools/face-mosaic", font=fm, fill=BLUE)
    d.line([lx, 728, W - X - 40, 728], fill=PBORD, width=2)
    d.text((lx, 796), "more", font=fm, fill=MUT)
    d.text((lx + 130, 796), "->", font=fm, fill=DIM)
    d.text((lx + 185, 796), "see description ", font=fm, fill=GREEN)
    aw = d.textlength("see description ", font=fm)
    d.text((lx + 185 + aw, 794), "↓", font=fmono(30), fill=GREEN)
    if full:
        d.text((X, 990), S5_HEAD, font=fnoto(56, 700), fill=WHITE)
    return img

save(scene5(False), 5, "a", B["s5a"])
save(scene5(True),  5, "b", B["s5b"])


# ---------------- Scene 6 : CTA outro (two-stage + blinking cursor) ----------------
def scene6(full, cursor_on=True):
    img, d = base("$ mask")
    d.text((X, 600), "$", font=fmono(58), fill=GREEN)
    fh = fnoto(HEAD6, 800)
    d.text((X + 66, 604), S6_H1, font=fh, fill=WHITE)
    d.text((X, 604 + HEAD6 + 24), S6_H2, font=fh, fill=BLUE)
    if full:
        d.line([X, 900, W - X, 900], fill=PBORD, width=2)
        d.text((X, 950), S6_SUB, font=fnoto(50, 500), fill=MUT)
        d.text((X, 1060), "mask a face", font=fmono(46), fill=GREEN)
        if cursor_on:
            cx = X + d.textlength("mask a face", font=fmono(46)) + 14
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
    seq = os.path.join(ROOT, f"seq_facemosaic_{LANG}_{name}")
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
vid = total / FPS - 0.5 * (len(scenes) - 1)
print(f"total {total} frames, video = {vid:.4f}s")

# ---------------- write render params (xfade offsets, narration delays) ----------------
dur = [TOT[i] / FPS for i in range(1, 7)]
off = []
acc = 0.0
for i in range(5):
    acc += dur[i] - 0.5
    off.append(round(acc, 5))
adel = [300] + [int(round((off[k] + 0.3) * 1000)) for k in range(5)]
DUR = round(sum(dur) - 2.5, 5)
DFO = round(DUR - 2.53, 5)
with open(os.path.join(ROOT, f"render_params_{LANG}.sh"), "w", newline="\n") as f:
    f.write("OFF=(" + " ".join(f"{o:.5f}" for o in off) + ")\n")
    f.write("ADEL=(" + " ".join(str(a) for a in adel) + ")\n")
    f.write(f"DUR={DUR}\n")
    f.write(f"DFO={DFO}\n")
print(f"render_params_{LANG}.sh: OFF={off} DUR={DUR}")
print("done", LANG)
