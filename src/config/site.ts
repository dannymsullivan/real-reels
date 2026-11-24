/**
 * ─────────────────────────────────────────────────────────────
 *  REAL REELS — single source of truth
 *  Change the brand name, prices, contact info, shipping regions
 *  and booking-form destination here. Everything on the site reads
 *  from this file.
 * ─────────────────────────────────────────────────────────────
 */

export const site = {
  brand: 'Real Reels',
  tagline: 'Your wedding, filmed by the people who love you.',
  description:
    'Real Reels ships a 4K camcorder kit to your wedding. Your guests film the candid moments all weekend, and our editors turn it into a highlight film you will watch forever.',
  url: 'https://realreels.example.com', // production URL (used for canonical, sitemap, OG)
  currency: 'USD',
  currencySymbol: '$',

  contact: {
    email: 'hello@realreels.example.com',
    phone: '(555) 010-2026',
    instagram: 'https://instagram.com/realreels',
    instagramHandle: '@realreels',
    tiktok: 'https://tiktok.com/@realreels',
    pinterest: 'https://pinterest.com/realreels',
  },

  /** Booking form: set `action` to a form endpoint (Formspree, Basin, Netlify, your API…).
   *  Leave it empty to fall back to a pre-filled email to contact.email. */
  form: {
    action: '',
    method: 'POST',
  },

  rental: {
    days: 7,
    arrivesDaysBefore: '3–4',
    returnWithinHours: 72,
    deliveryWeeks: '3–4',
    shipsTo: ['United States', 'Canada', 'United Kingdom'],
    carrier: 'UPS',
  },

  /** Package data drives the cards, the comparison and the booking form. */
  packages: [
    {
      id: 'core',
      name: 'Core',
      price: 729,
      blurb: 'One camera, passed hand to hand.',
      cameras: 1,
      batteries: 3,
      hours: 8,
      cards: 1,
      cardSize: '256GB',
      filmMin: 3,
      filmMax: 5,
      bestFor: 'Up to ~100 guests',
      popular: false,
    },
    {
      id: 'deluxe',
      name: 'Deluxe',
      price: 989,
      blurb: 'Two cameras, twice the angles.',
      cameras: 2,
      batteries: 6,
      hours: 16,
      cards: 2,
      cardSize: '256GB',
      filmMin: 5,
      filmMax: 7,
      bestFor: 'Big weekends & 100+ guests',
      popular: true,
    },
  ],

  /** Included with every package (rendered as icons). */
  included: [
    { icon: 'raw', label: 'Every raw clip, organized' },
    { icon: 'list', label: 'Shot-list cards' },
    { icon: 'sticker', label: 'Guide stickers' },
    { icon: 'bag', label: 'Padded carry bag' },
    { icon: 'truck', label: 'Shipping both ways' },
    { icon: 'calendar', label: '7-day rental' },
  ],
} as const;

export type Package = (typeof site.packages)[number];
export const money = (n: number) => `${site.currencySymbol}${n.toLocaleString('en-US')}`;
export const fromPrice = Math.min(...site.packages.map((p) => p.price));
