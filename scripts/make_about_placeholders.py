"""Neutral placeholders for the About page photo slots (public/media/about/).
Deliberately abstract (no people): drop real photos in with the same filenames.
Re-run safely: existing files are skipped unless --force is passed."""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageChops

ROOT = os.path.join(os.path.dirname(__file__), "..", "public", "media", "about")
FORCE = "--force" in sys.argv
SERIF = "/usr/share/fonts/truetype/sand-box/google/Cormorant Garamond/CormorantGaramond-VariableFont_wght.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

# filename, w, h, label, (top colour, bottom colour)
SLOTS = [
    ("family.jpg", 1200, 1500, "Danny & family portrait", ((241, 232, 220), (221, 196, 184))),
    ("wedding-1.jpg", 1200, 1500, "Wedding photography 1", ((238, 231, 220), (214, 205, 186))),
    ("wedding-2.jpg", 1800, 1200, "Wedding photography 2", ((241, 233, 222), (226, 204, 196))),
    ("wedding-3.jpg", 1800, 1200, "Wedding photography 3", ((236, 230, 218), (205, 207, 188))),
    ("wedding-4.jpg", 1200, 1500, "Wedding photography 4", ((242, 232, 218), (225, 200, 170))),
    ("booth-1.jpg", 1200, 1500, "Photo booth 1", ((240, 230, 222), (219, 190, 190))),
    ("booth-2.jpg", 1800, 1200, "Photo booth 2", ((238, 232, 220), (214, 196, 170))),
]

def slot(w, h, label, name, top, bottom):
    img = Image.new("RGB", (w, h)); d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        d.line([(0, y), (w, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    noise = Image.effect_noise((w, h), 22).convert("RGB")
    img = Image.blend(img, ImageChops.overlay(img, noise), .22)
    d = ImageDraw.Draw(img)
    ink = (122, 92, 80)
    m = int(min(w, h) * .05)
    # dashed inset frame
    dash, gap = 18, 14
    for x in range(m, w - m, dash + gap):
        d.line([(x, m), (min(x + dash, w - m), m)], fill=ink, width=2)
        d.line([(x, h - m), (min(x + dash, w - m), h - m)], fill=ink, width=2)
    for y in range(m, h - m, dash + gap):
        d.line([(m, y), (m, min(y + dash, h - m))], fill=ink, width=2)
        d.line([(w - m, y), (w - m, min(y + dash, h - m))], fill=ink, width=2)
    # simple photo glyph
    cx, cy, s = w / 2, h / 2 - min(w, h) * .12, min(w, h) * .09
    d.rounded_rectangle([cx - s, cy - s * .7, cx + s, cy + s * .7], radius=int(s * .18), outline=ink, width=4)
    d.ellipse([cx - s * .35, cy - s * .35, cx + s * .35, cy + s * .35], outline=ink, width=4)
    d.rectangle([cx - s * .45, cy - s * .92, cx - s * .05, cy - s * .7], fill=ink)
    serif = ImageFont.truetype(SERIF, int(min(w, h) * .07)); serif.set_variation_by_axes([400])
    mono = ImageFont.truetype(MONO, int(min(w, h) * .028))
    d.text((cx, h / 2 + min(w, h) * .06), label, font=serif, fill=(60, 44, 38), anchor="mm")
    d.text((cx, h / 2 + min(w, h) * .15), f"public/media/about/{name}", font=mono, fill=ink, anchor="mm")
    d.text((cx, h / 2 + min(w, h) * .2), f"{w}×{h} or larger · same ratio", font=mono, fill=ink, anchor="mm")
    return img

os.makedirs(ROOT, exist_ok=True)
for name, w, h, label, (top, bottom) in SLOTS:
    p = os.path.join(ROOT, name)
    if os.path.exists(p) and not FORCE: continue
    slot(w, h, label, name, top, bottom).save(p, quality=82, optimize=True, progressive=True)
    print("wrote", name)
