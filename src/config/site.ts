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
    'I Do Cam ships a real HD camcorder kit to your wedding. Your guests film the candid moments all weekend, and our editors turn it into a highlight film you will watch forever.',
  url: 'https://idocam.com', // production URL (used for canonical, sitemap, OG)
  currency: 'USD',
  currencySymbol: '$',

  contact: {
    email: 'hello@idocam.com',
    instagram: 'https://instagram.com/idocam',
    instagramHandle: '@idocam',
    tiktok: 'https://tiktok.com/@idocam',
    pinterest: 'https://pinterest.com/idocam',
  },

  /** Booking form: handled by Netlify Forms (detected at deploy from the built HTML).
   *  Submissions show in Netlify → Site → Forms → `name`. Set email notifications there. */
  form: {
    name: 'booking',
    successMessage: "Thank you! Your inquiry is in. We'll check your date and reply within one business day.",
  },

  rental: {
    days: 7,
    arrivesDaysBefore: '3–4',
    returnWithinHours: 72,
    deliveryWeeks: '3–4',
    rushWeeks: 2,
    shipsTo: ['United States'],
    carrier: 'UPS',
  },

  /** Package data drives the cards, the comparison and the booking form. */
  packages: [
    {
      id: 'essentials',
      name: 'Essentials',
      price: 729,
      blurb: 'One camera, passed hand to hand.',
      cameras: 1,
      batteries: 3,
      hours: 8,
      cards: 1,
      cardSize: '256GB',
      filmMin: 3,
      filmMax: 5,
      bestFor: 'Intimate weddings, up to ~100 guests',
      popular: false,
      extras: [] as { icon: string; label: string }[],
    },
    {
      id: 'signature',
      name: 'Signature',
      price: 989,
      blurb: 'Two cameras, twice the angles.',
      cameras: 2,
      batteries: 6,
      hours: 16,
      cards: 2,
      cardSize: '256GB',
      filmMin: 5,
      filmMax: 7,
      bestFor: 'Most couples, 100+ guests',
      popular: true,
      extras: [] as { icon: string; label: string }[],
    },
    {
      id: 'heirloom',
      name: 'Heirloom',
      price: 1995,
      blurb: 'Every angle, then the honeymoon.',
      cameras: 3,
      batteries: 9,
      hours: 24,
      cards: 3,
      cardSize: '256GB',
      filmMin: 10,
      filmMax: 12,
      bestFor: 'Big weekends & couples jetting off after',
      popular: false,
      /** Overrides rental.days for this tier. */
      rentalDays: 14,
      /** Highlighted perk on the card. */
      perk: { icon: 'plane', title: 'Keep it for the honeymoon', text: '14-day rental so you can film the honeymoon too. We add your honeymoon clips to your film.' },
      /** Tier-only extras (icons on the card + rows in the comparison). */
      extras: [
        { icon: 'sparkle', label: '60-sec social teaser' },
        { icon: 'clock', label: 'Rush edit · 2 weeks' },
        { icon: 'usb', label: 'Keepsake USB in a linen box' },
      ],
    },
  ],

  /** TODO: Testimonials are STAND-INS so the page reads naturally. Replace them with
   *  real, permissioned reviews (names, cities, quotes) before promoting the site. */
  testimonials: [
    { quote: 'We watched it on the flight home and cried the whole way. Our friends caught the vow-reading nerves, the cake disaster, my dad dancing. Things we never saw.', names: 'Maya & Jordan', initials: 'M&J', city: 'Asheville, NC', tier: 'Signature' },
    { quote: 'My grandfather filmed the toasts from his chair at table four. It is the most precious five minutes we own, and the two cameras meant nothing got missed.', names: 'Priya & Sam', initials: 'P&S', city: 'Charleston, SC', tier: 'Signature' },
    { quote: 'We took the cameras to Maui afterwards. The highlight film ends on our honeymoon sunset, and the 60-second teaser got more likes than our engagement photos.', names: 'Lauren & Chris', initials: 'L&C', city: 'Hudson Valley, NY', tier: 'Heirloom' },
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
