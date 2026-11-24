"""Capture review screenshots of a running preview (default http://localhost:4321)."""
import sys, time
from playwright.sync_api import sync_playwright
URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4321/"
OUT = "screenshots-review"

def settle(page):
    # trigger all scroll reveals + lazy images, then return to top
    h = page.evaluate("document.body.scrollHeight")
    for y in range(0, h, 500):
        page.evaluate(f"window.scrollTo(0,{y})"); time.sleep(0.05)
    page.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('is-in'))")
    page.evaluate("window.scrollTo(0,0)"); time.sleep(1.2)
    # make the fixed film-grain overlay cover the full document so tall captures look like the live page
    page.add_style_tag(content="body{position:relative}.grain::after{position:absolute!important;inset:0!important;animation:none!important}#mobile-bar{display:none!important}")

def section(page, sel, path):
    page.add_style_tag(content="#top-nav{visibility:hidden}")
    page.locator(sel).screenshot(path=path)
    page.add_style_tag(content="#top-nav{visibility:visible}")

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--autoplay-policy=no-user-gesture-required"])
    d = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    d.goto(URL, wait_until="networkidle"); settle(d)
    d.screenshot(path=f"{OUT}/desktop-hero.png")
    d.screenshot(path=f"{OUT}/desktop-full.png", full_page=True)
    section(d, "#packages", f"{OUT}/packages-desktop.png")
    m = b.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    m.goto(URL, wait_until="networkidle"); settle(m)
    m.screenshot(path=f"{OUT}/mobile-hero.png")
    m.screenshot(path=f"{OUT}/mobile-full.png", full_page=True)
    section(m, "#packages", f"{OUT}/packages-mobile.png")
    d.evaluate("document.querySelector('#packages').scrollIntoView()"); time.sleep(0.8)
    d.screenshot(path=f"{OUT}/desktop-scrolled-nav.png")
    errs = []
    d.on("console", lambda msg: errs.append(msg.text) if msg.type == "error" else None)
    d.reload(wait_until="networkidle"); time.sleep(1)
    print("console errors:", errs)
    print("video playing:", d.evaluate("(()=>{const v=document.getElementById('hero-video');return v && !v.paused && v.readyState>=2})()"))
    b.close()
