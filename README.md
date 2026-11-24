# I Do Cam — wedding camcorder rental + edited film

Astro 7 + Tailwind CSS v4 static marketing site.

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # static output in dist/
npm run preview
```

## Change brand, prices, contact, shipping, form
Everything lives in **`src/config/site.ts`**: brand name, tagline, URL, email/phone/socials,
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
| `dance-floor.jpg` | Packed dance floor, string lights | 3:2, 1800×1200 |
| `couple-watching-film.jpg` | Couple on the sofa watching their wedding film (also Book section bg) | 4:5, 1200×1500 |
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

## Optional honeymoon tier
`src/config/site.ts` has a commented-out third package (`heirloom`) with `rentalDays: 14` and a `perk`
("Keep it for the honeymoon"), shown with a plane icon on the card and in the comparison table. Set a price and uncomment to enable.

## Placeholders to replace before launch
- Press strip names (`PressStrip.astro`) are fictional placeholders.
- Testimonials (`Testimonials.astro`) are labeled samples.
- `site.url`, email, phone, socials in `site.ts`; `public/robots.txt` sitemap URL.

## Review screenshots
With `npm run preview` running: `python scripts/screenshots.py` (Playwright + Chrome) writes to
`screenshots-review/` (git-ignored).
