"""Render favicons (from public/favicon.svg) and the OG image (logo A over the hero still)."""
import base64, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent / "public"
icon = (ROOT / "favicon.svg").read_text()
wm = base64.b64encode((ROOT / "brand/wordmark-light.svg").read_bytes()).decode()
poster = base64.b64encode((ROOT / "media/hero-poster.jpg").read_bytes()).decode()
fonts = pathlib.Path("/workspace/idocam-brand/fonts")
inter = base64.b64encode((fonts / "Inter-Regular.ttf").read_bytes()).decode() if (fonts / "Inter-Regular.ttf").exists() else ""
frau = base64.b64encode((fonts / "Fraunces-Italic.ttf").read_bytes()).decode() if (fonts / "Fraunces-Italic.ttf").exists() else ""
og = f"""<html><head><style>
@font-face{{font-family:I;src:url(data:font/ttf;base64,{inter})}}
@font-face{{font-family:F;src:url(data:font/ttf;base64,{frau})}}
body{{margin:0;width:1200px;height:630px;overflow:hidden;font-family:I,sans-serif}}
.bg{{position:absolute;inset:0;background:url(data:image/jpeg;base64,{poster}) center/cover}}
.sh{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(42,33,29,.92) 0%,rgba(42,33,29,.72) 45%,rgba(42,33,29,.1) 100%)}}
.c{{position:absolute;left:72px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;color:#f8f3ea}}
img{{width:420px}} h1{{font-family:F,serif;font-style:italic;font-weight:400;font-size:58px;line-height:1.05;margin:36px 0 18px;color:#e9cfc4}}
p{{font-size:22px;opacity:.85;margin:0}} .u{{position:absolute;right:40px;bottom:30px;color:#f8f3ea;font:600 16px I;letter-spacing:.25em}}
</style></head><body><div class=bg></div><div class=sh></div><div class=c><img src="data:image/svg+xml;base64,{wm}">
<h1>Say “I do.”<br>Let everyone else film it.</h1><p>A 4K camcorder kit for your guests + a beautifully edited film.</p></div>
<div class=u>IDOCAM.COM</div></body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    pg.set_content(og); pg.wait_for_timeout(500)
    pg.screenshot(path="/tmp/og.png")
    for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
        pg = b.new_page(viewport={"width": size, "height": size})
        bg = '#f8f3ea' if name == 'apple-touch-icon.png' else 'transparent'
        pg.set_content(f"<html><body style='margin:0;background:{bg}'>{icon.replace('<svg ', f'<svg style=\"width:{size}px;height:{size}px;display:block\" ', 1)}</body></html>")
        pg.screenshot(path=str(ROOT / name), omit_background=(name != 'apple-touch-icon.png'))
    b.close()
from PIL import Image
Image.open("/tmp/og.png").convert("RGB").save(ROOT / "media/og-image.jpg", quality=88, optimize=True, progressive=True)
print("done")
