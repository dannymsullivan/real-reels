# I Do Cam — wedding camcorder rental + edited film

Astro 7 + Tailwind CSS v4 static marketing site.

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # static output in dist/
npm run preview
```

## Change brand, prices, contact, shipping, form
Everything lives in **`src/config/site.ts`**: brand name, tagline, URL, email/socials,
booking-form `action` (empty = opens a pre-filled email to `contact.email`), rental terms
(days, arrival window, return window, ship-to countries) and the **packages** (price, cameras,
batteries, hours, cards, film length, "most popular"). The package cards, comparison table,
booking form, FAQ and SEO JSON-LD all read from it.

## Media slots (`public/media/`)
All slots now hold the real Runway-generated media. (`npm run placeholders` can regenerate stand-ins for any missing file.)
Swap in real assets by **overwriting the file with the same name** and keeping the aspect ratio
(images are `object-fit: cover`, so close-enough ratios crop gracefully).

| File | Subject | Aspect / size |
|---|---|---|
| `hero.mp4` | Hero loop: warm, candid guest-POV wedding moments (muted, ~8–15 s, seamless loop, H.264, faststart, ideally < 6 MB) | 16:9, 1920×1080 |
| `hero.webm` | Same hero loop as WebM/VP9 (served first, mp4 fallback) | 16:9, 1920×1080 |
| `hero-poster.jpg` | First frame / still of the hero video (also reduced-motion fallback) | 16:9, 1920×1080 |
| `og-image.jpg` | Social share card: logo A + headline over the hero still (`python scripts/make_brand_assets.py`) | 1.91:1, 1200×630 |
| `kit-unboxing.jpg` | Couple on the floor opening the kit box | 4:5, 1200×1500 |
| `guests-filming-reception.jpg` | A guest filming the reception on the camcorder | 4:5, 1200×1500 |
| `getting-ready.jpg` | Bride laughing while a bridesmaid films her getting ready | 4:5, 1200×1500 |
| `ceremony.jpg` | Guest filming an outdoor ceremony from the rows | 3:2, 1800×1200 |
| `kids-filming.jpg` | Why collage: kid filming with the camcorder at an outdoor reception | 3:2, 1600×1067 |
| `hero-960.mp4/.webm` | Lighter hero for phones / data-saver (~1 MB) | 16:9, 960px |
| `band.webm/.mp4`, `band-960.mp4`, `band-poster.jpg` | Band-reel section video | 16:9 |
| `couple-watching-happy.jpg` | Couple laughing on the sofa watching their wedding film (Book section + About CTA bg) | 16:9, 1920×1080 |
| `couple-watching-happy-portrait.jpg` | Same scene, cropped to their faces (How it works step 6) | 4:5, 1200×1500 |
| `couple-watching-film.jpg` | Earlier tearful version, kept as a backup, unused on the site | 4:5, 1200×1500 |
| `kit-flatlay.jpg` | Top-down flat-lay on linen: camcorder, 2 batteries, SD card, instruction card, drawstring bag, charger + cable | 1:1, 1600×1600 |
| `booking.jpg` | Couple booking on a laptop (How it works step 1) | 4:5, 1200×1500 |
| `ship-back.jpg` | Hands packing the camcorder into the open box, blank label + tape beside it (step 4) | 4:5, 1200×1500 |
| `editing-suite.jpg` | Editor cutting the film (step 5) | 4:5, 1200×1500 |
| `gallery-01.jpg` | A groom and his husband cry-laughing during the best man's toast | 4:5, 1200×1500 |
| `gallery-02.jpg` | Golden-hour couple portrait in a field | 3:2, 1800×1200 |
| `gallery-03.jpg` | Sparkler exit at night | 3:2, 1800×1200 |
| `gallery-04.jpg` | Grandparents slow dancing | 4:5, 1200×1500 |
| `gallery-05.jpg` | First look in a garden | 4:5, 1200×1500 |
| `gallery-06.jpg` | Friends laughing at a candlelit vineyard dinner table | 3:2, 1800×1200 |
| `gallery-07.jpg` | Ring exchange close-up | 3:2, 1800×1200 |
| `gallery-08.jpg` | Dance floor at night, a guest filming | 4:5, 1200×1500 |

Gallery order alternates tall/wide so the masonry columns stay balanced; keep those ratios.
The numbered hotspots on the flat-lay are % positions in `src/components/InTheBox.astro`; nudge
them after the real photo lands. Gallery alt text/captions live in `src/components/Gallery.astro`.

## Brand (logo direction A, Editorial Romance)
- `public/brand/wordmark-light.svg` (over the hero video / dark backgrounds) and `public/brand/wordmark.svg` (light backgrounds), cropped from `/workspace/idocam-brand/svg/A-editorial-wordmark*.svg`.
- `public/favicon.svg` (icon A), `favicon-32.png`, `apple-touch-icon.png` (180, opaque), `icon-192.png`, `icon-512.png`, `site.webmanifest`. Regenerate the PNGs + OG image with `python scripts/make_brand_assets.py` (needs Playwright + Chrome).
- The rose/gold/sage tape stripes from direction B are used only as an accent in "What's in the box".

## Packages (3-tier anchored pricing)
Defined in `src/config/site.ts` → `packages`:
- **Essentials** $729: 1 camcorder, 3 batteries / 8 hrs, 1×256GB, 3–5 min film, 7-day rental.
- **Signature** $989 (`popular: true`, center, emphasized): 2 camcorders, 6 batteries / 16 hrs, 2×256GB, 5–7 min film, 7-day rental.
- **Heirloom** $1,995: 3 camcorders, 9 batteries / 24 hrs, 3×256GB, 10–12 min film, plus `extras`
  (60-sec social teaser, 2-week rush edit, keepsake USB in a linen box) and a `perk`
  ("Keep it for the honeymoon": `rentalDays: 14`, honeymoon clips added to the film, plane icon).
Cards, the comparison table, booking-form options, FAQ and JSON-LD all read from this list.

## About page (`/about`) photo slots
Founder story lives in `src/pages/about.astro`. Drop Danny's real photos into `public/media/about/`
with these names (neutral placeholders are there now; `python3 scripts/make_about_placeholders.py` regenerates them):
- `family.jpg`: Danny & family portrait, page hero (4:5 portrait, 1200×1500+)
- `wedding-1.jpg`, `wedding-4.jpg`: wedding photography (4:5 portrait)
- `wedding-2.jpg`, `wedding-3.jpg`: wedding photography (3:2 landscape, 1800×1200+)
- `booth-1.jpg` (4:5 portrait), `booth-2.jpg` (3:2 landscape): photo booth company
Have fewer photos? Delete the unused files and the grid adapts at build time. Update alt text in `about.astro`.

## Placeholders to replace before launch
- Press strip names (`PressStrip.astro`) are fictional placeholders.
- Testimonials (`Testimonials.astro`) are labeled samples.
- `site.url`, email, socials in `site.ts`; `public/robots.txt` sitemap URL.

## Review screenshots
With `npm run preview` running: `python scripts/screenshots.py` (Playwright + Chrome) writes to
`screenshots-review/` (git-ignored).
