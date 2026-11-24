/**
 * ─────────────────────────────────────────────────────────────
 *  I DO CAM — single source of truth
 *  Change the brand name, prices, contact info, shipping regions
 *  and booking-form destination here. Everything on the site reads
 *  from this file.
 * ─────────────────────────────────────────────────────────────
 */

export const site = {
  brand: 'I Do Cam',
  tagline: 'Say “I do.” Let everyone else film it.',
  description:
    'I Do Cam ships a 4K camcorder kit to your wedding. Your guests film the candid moments all weekend, and our editors turn it into a highlight film you will watch forever.',
  url: 'https://idocam.com', // production URL (used for canonical, sitemap, OG)
  currency: 'USD',
  currencySymbol: '$',

  contact: {
    email: 'hello@idocam.com',
    phone: '(555) 010-2026',
    instagram: 'https://instagram.com/idocam',
    instagramHandle: '@idocam',
    tiktok: 'https://tiktok.com/@idocam',
    pinterest: 'https://pinterest.com/idocam',
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
    /* Optional third tier, e.g. a honeymoon tier. Uncomment and set a price to enable.
       `rentalDays` overrides rental.days; `perk` renders as a highlighted row on the card.
    {
      id: 'heirloom', name: 'Heirloom', price: 0, blurb: 'The wedding, then the honeymoon.',
      cameras: 2, batteries: 6, hours: 16, cards: 2, cardSize: '256GB', filmMin: 7, filmMax: 10,
      bestFor: 'Couples heading straight off on a honeymoon', popular: false,
      rentalDays: 14,
      perk: { icon: 'plane', title: 'Keep it for the honeymoon', text: '14-day rental so you can film the honeymoon too. Your honeymoon clips get added to your film.' },
    },
    */
  ],

  /** Included with every package (rendered as icons). */
  included: [
    { icon: 'raw', label: 'Every raw clip, organized' },
    { icon: 'list', label: 'Shot-list cards' },
    { icon: 'sticker', label: 'Guide stickers' },
    { icon: 'bag', label: 'Carry bag' },
    { icon: 'truck', label: 'Shipping both ways' },
    { icon: 'calendar', label: '7-day rental' },
  ],
} as const;

export type Package = (typeof site.packages)[number];
export const money = (n: number) => `${site.currencySymbol}${n.toLocaleString('en-US')}`;
export const fromPrice = Math.min(...site.packages.map((p) => p.price));
