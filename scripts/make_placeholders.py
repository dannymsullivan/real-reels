"""Generate tasteful warm 'film still' placeholders for every media slot.
Re-run safely: existing files are skipped unless --force is passed.
Real photos/video simply overwrite these files (same names)."""
import os, random, sys, subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

ROOT = os.path.join(os.path.dirname(__file__), "..", "public", "media")
FORCE = "--force" in sys.argv
SERIF = "/usr/share/fonts/truetype/sand-box/google/Cormorant Garamond/CormorantGaramond-VariableFont_wght.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

PALETTES = [
    [(236, 222, 204), (196, 160, 132), (122, 88, 74)],    # blush/cocoa
    [(232, 226, 210), (170, 168, 140), (88, 92, 74)],     # sage
    [(240, 228, 206), (214, 170, 120), (110, 70, 50)],    # golden hour
    [(226, 218, 214), (176, 146, 150), (92, 66, 74)],     # dusty rose
    [(30, 26, 30), (120, 80, 60), (230, 180, 120)],       # night / dance floor
]

# filename, width, height, label, palette index
SLOTS = [
    ("hero-poster.jpg", 1920, 1080, "Hero poster · 16:9", 2),
    ("og-image.jpg", 1200, 630, "Social share · 1.91:1", 2),
    ("kit-unboxing.jpg", 1200, 1500, "Unboxing the kit · 4:5", 0),
    ("guests-filming-reception.jpg", 1200, 1500, "Guests filming at reception · 4:5", 4),
    ("getting-ready.jpg", 1200, 1500, "Getting ready · 4:5", 3),
    ("ceremony.jpg", 1800, 1200, "Ceremony · 3:2", 1),
    ("dance-floor.jpg", 1800, 1200, "Dance floor · 3:2", 4),
    ("couple-watching-film.jpg", 1200, 1500, "Couple watching their film · 4:5", 2),
    ("kit-flatlay.jpg", 1600, 1600, "Camcorder kit flat-lay · 1:1", 0),
    ("booking.jpg", 1200, 1500, "Booking online · 4:5", 1),
    ("ship-back.jpg", 1200, 1500, "Shipping the box back · 4:5", 0),
    ("editing-suite.jpg", 1200, 1500, "Editor at work · 4:5", 3),
    ("gallery-01.jpg", 1200, 1500, "Gallery 01 · 4:5", 3),
    ("gallery-02.jpg", 1800, 1200, "Gallery 02 · 3:2", 2),
    ("gallery-03.jpg", 1800, 1200, "Gallery 03 · 3:2", 4),
    ("gallery-04.jpg", 1200, 1500, "Gallery 04 · 4:5", 1),
    ("gallery-05.jpg", 1200, 1500, "Gallery 05 · 4:5", 0),
    ("gallery-06.jpg", 1800, 1200, "Gallery 06 · 3:2", 2),
    ("gallery-07.jpg", 1800, 1200, "Gallery 07 · 3:2", 3),
    ("gallery-08.jpg", 1200, 1500, "Gallery 08 · 4:5", 4),
]

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def film_still(w, h, pal, seed, label=None):
    rnd = random.Random(seed)
    base = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(base)
    for y in range(h):
        t = y / h
        c = lerp(pal[0], pal[1], t * 1.2) if t < 0.8 else lerp(pal[1], pal[2], (t - 0.8) * 5)
        d.line([(0, y), (w, y)], fill=c)
    # bokeh
    bok = Image.new("RGB", (w, h), (0, 0, 0))
    bd = ImageDraw.Draw(bok)
    for _ in range(38):
        r = rnd.randint(int(w * .02), int(w * .11))
        x, y = rnd.randint(-r, w + r), rnd.randint(-r, int(h * .75))
        warm = (255, rnd.randint(200, 235), rnd.randint(150, 200))
        a = rnd.uniform(.15, .55)
        bd.ellipse([x - r, y - r, x + r, y + r], fill=tuple(int(c * a) for c in warm))
    bok = bok.filter(ImageFilter.GaussianBlur(w / 90))
    img = ImageChops.screen(base, bok)
    # soft silhouettes (abstract figures) for depth
    sil = Image.new("L", (w, h), 0)
    sd = ImageDraw.Draw(sil)
    for _ in range(rnd.randint(2, 4)):
        cx = rnd.randint(int(w * .15), int(w * .85)); bw = rnd.randint(int(w * .08), int(w * .16))
        top = rnd.randint(int(h * .35), int(h * .55))
        sd.ellipse([cx - bw * .45, top - bw * .9, cx + bw * .45, top], fill=150)
        sd.rounded_rectangle([cx - bw, top, cx + bw, h + 50], radius=int(bw * .8), fill=150)
    sil = sil.filter(ImageFilter.GaussianBlur(w / 60))
    dark = Image.new("RGB", (w, h), pal[2])
    img = Image.composite(dark, img, sil.point(lambda v: int(v * .55)))
    # light leak
    leak = Image.new("RGB", (w, h), (0, 0, 0))
    ld = ImageDraw.Draw(leak)
    ld.ellipse([w * .55, -h * .4, w * 1.4, h * .5], fill=(255, 150, 80))
    leak = leak.filter(ImageFilter.GaussianBlur(w / 8))
    img = ImageChops.screen(img, Image.eval(leak, lambda v: int(v * .45)))
    # vignette
    vig = Image.new("L", (w, h), 0)
    ImageDraw.Draw(vig).ellipse([-w * .15, -h * .15, w * 1.15, h * 1.15], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(w / 7))
    img = Image.composite(img, Image.new("RGB", (w, h), (20, 14, 12)), vig)
    # grain
    noise = Image.effect_noise((w, h), 28).convert("RGB")
    img = Image.blend(img, ImageChops.overlay(img, noise), .35)
    if label:
        dr = ImageDraw.Draw(img)
        f = ImageFont.truetype(MONO, max(14, w // 70))
        dr.text((w * .04, h - w * .06), "PLACEHOLDER — " + label.upper(), font=f, fill=(255, 248, 238))
    return img

def main():
    os.makedirs(ROOT, exist_ok=True)
    for i, (name, w, h, label, p) in enumerate(SLOTS):
        path = os.path.join(ROOT, name)
        if os.path.exists(path) and not FORCE:
            continue
        lbl = None if name in ("hero-poster.jpg",) else label
        film_still(w, h, PALETTES[p], i * 7 + 3, lbl).save(path, quality=82, optimize=True, progressive=True)
        print("wrote", name)
    # hero video placeholder: slow push-in over a wide film still + grain
    vid = os.path.join(ROOT, "hero.mp4")
    if FORCE or not os.path.exists(vid):
        src = "/tmp/hero-src.jpg"
        film_still(2560, 1440, PALETTES[2], 99).save(src, quality=90)
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", src, "-t", "10",
            "-vf", "scale=3840:-1,zoompan=z='1+0.0006*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=250:s=1920x1080:fps=25,"
                   "noise=alls=14:allf=t,eq=brightness='0.02*sin(2*PI*t/5)',fade=in:0:20,fade=out:230:20",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "30", "-preset", "slow",
            "-movflags", "+faststart", "-an", vid], check=True)
        print("wrote hero.mp4")

if __name__ == "__main__":
    main()
