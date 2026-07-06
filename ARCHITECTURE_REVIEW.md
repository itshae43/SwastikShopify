# Architecture Review — Swastik Jewels Theme

> A senior-architect assessment of the theme's structure, its strengths, and the systemic issues that limit scalability.
> Read-only. No code was modified.

---

## 1. Executive summary

Swastik Jewels is an **ambitious, visually rich custom theme** built on Shopify's Skeleton base, with ~40 sections, bespoke drawers, a WhatsApp/video-call service layer, and heavy custom interaction (coverflow carousels, tabbed grids, AJAX cart). The *product design* is strong. The *software architecture* has a consistent, correctable set of problems that trace back to **one root cause**:

> **Configuration lives in the wrong layer.** Content is hardcoded in Liquid (so merchants can't edit it), while design tokens are duplicated inline in every section (so they can't stay consistent). Meanwhile a **parallel client-side "mock" cart/wishlist** was built alongside the real Shopify cart, and the two now diverge.

Everything else — palette fragmentation, i18n gaps, duplication, mock data — is a symptom of these two decisions. The good news: the fixes are structural and mostly mechanical, not a rewrite.

**Overall grade: design A- / architecture C.** Scalable after the token layer and cart model are fixed; fragile until then.

---

## 2. What the theme gets right

Credit where due — these are genuinely well done and should be the model for the rest:

1. **Clean layer separation exists at the top.** `layout/theme.liquid` uses section groups (`header-group`, `footer-group`), renders global drawers once, and defers to templates. `content_for_index` is empty — the homepage is **template-driven JSON**, the modern OS 2.0 approach, not legacy.
2. **A real token layer exists.** `snippets/css-variables.liquid` maps settings → `:root` CSS variables correctly. The foundation for a design system is present (it's just under-used).
3. **The stock/boilerplate surface is correct.** `article`, `blog`, `search`, `page`, `404`, `password`, `cart`, `collection`, `collections`, `blocks/group`, `blocks/text`, `snippets/image`, `snippets/meta-tags` all use `| t`, `| money`, and real Shopify objects. `meta-tags` in particular is solid SEO/structured-data work.
4. **Several custom sections are well-architected.** `gold-collection-showcase` (full `t:` i18n + collection pickers + real placeholders), `main-collection-banner` (settings-driven with proper collection fallbacks), `brand-story` and `newsletter` (constrained `bg_color` select), and `footer` (structured brand/menu/contact settings) show the team *can* build sections the right way.
5. **Real Shopify commerce plumbing where it counts.** `main-collection-product-grid` implements genuine Storefront filtering/sorting/pagination; `product.liquid` parses real variant JSON; `video-call` uses a real `contact` form. The Shopify fundamentals are understood.
6. **Good block modeling.** Hero slides, testimonials, pillars, promo cards, highlights, occasions are all repeatable blocks — the correct editor pattern.

---

## 3. Systemic issues (ranked by architectural impact)

### Issue 1 — Inverted configuration boundaries (the root cause)
Content that should be merchant-editable is hardcoded in Liquid; design tokens that should be global are duplicated per-section. See `THEME_EDITOR_GUIDELINES.md` and `CODE_VS_EDITOR.md`. Symptoms:
- `product.liquid` has **zero schema settings** — no merchant control over the most important page.
- Copy hardcoded outside schemas: "SHOP NOW", "Subscribe", newsletter placeholder/success, product trust/shipping/care text, drawer labels.
- Every section re-hardcodes `#013F3E`/`#D4AF37`/`Montserrat` instead of consuming the existing CSS vars.

### Issue 2 — A parallel "mock" commerce system that diverges from Shopify
This is the most serious *correctness* risk. Three findings:
- **`theme-ajax-sync.liquid` fabricates cart state on failure.** It calls `handleAddToCartSuccess()` in **both** the `.then` and `.catch` of `/cart/add.js`, so a failed add still increments the badge and localStorage. The visible cart can diverge from the true server cart.
- **`cart-drawer.liquid` renders localStorage "mock" items when the real cart is empty** — showing a fabricated cart whose checkout (posting to real `routes.cart_url`) would be empty.
- **Prices are DOM-scraped** (`innerText.replace(/[^0-9.-]+/g,"") * 100`) rather than read from variants; **wishlist is localStorage-only** (no server persistence, lost across devices).
- **Three overlapping drawer implementations** (`cart-drawer`, `wishlist-drawer`, `snippets/sidebar-drawer`) with **`formatMoney` defined 3×** and many leaked globals.

### Issue 3 — Design-token fragmentation
One brand rendered as **three greens** (`#013F3E`/`#0a2a26`/`#0b2e27`), **three-plus golds** (`#D4AF37`/`#b38245`/`#c5a47e`/`#d8c3b1`), and **four font stacks**. `layout/theme.liquid` hardcodes four Google Font families, bypassing the theme's own font setting. Container widths hardcoded three different ways. (Full evidence in `GLOBAL_SETTINGS_GUIDE.md`.)

### Issue 4 — Mock/fake data shipped in the theme
Fabricated content that can render on a live store:
- `best-sellers-fallback-grid.liquid`: a full fake catalog with invented prices, fake "% OFF", and misleading **"BIS Hallmarked / 18K Gold"** trust claims, all linking to one product handle.
- `product.liquid`: fake "128 reviews", always-5-stars, "23% OFF" unrelated to price, fabricated spec table (3.45 g, SI-IJ color).
- Fake testimonials (Arjun/Priya/Rohan), fake reels view counts (12.6K…), placeholder contact data (`123 Mock Address Lane`, `whatsapp-request@placeholder.com`, `+1234567890`).
These are trust and potentially **legal/advertising** risks (fabricated reviews, unverifiable hallmark claims), not just cosmetic.

### Issue 5 — Duplication instead of reuse
- `new-arrivals` ≈ `best-sellers`: ~575 lines of card CSS and the card-carousel JS are near-identical (an in-code comment even says "Same behavior as best sellers").
- Section header/ornament markup duplicated across `why-choose-us`, `shop-by-occasion`, `testimonials-slider`.
- Fallback nav tree duplicated in header desktop + mobile.
- `collection.lab-grown.json` is an unedited copy of `collection.json`.
- Product-card markup partially reimplemented inside sections instead of always using `snippets/product-card.liquid`.

### Issue 6 — Incomplete internationalization
Only ~8 sections have locale entries; only a handful use `t:` schema keys. ~30 sections are raw English, several with strings hardcoded entirely outside their schema. The theme is *half* internationalized — the hardest state to finish from later.

### Issue 7 — Inline-everything performance profile
Sections carry 200–660 lines of inline CSS and up to ~290 lines of inline JS each. `hero-banner` uses raw `<script>` (per-page, not deduped); `instagram-reels` uses `{%- style -%}` instead of `{% stylesheet %}`. `theme.liquid` runs a permanent `MutationObserver` fighting Shopify's injected captcha node. This inflates page weight and defeats Shopify's CSS/JS de-duplication.

### Issue 8 — Dev artifacts in the production theme
`hello-text.liquid` + `index.page-1/2/3.json` ("Hello Page 1/2/3") are scaffolding stubs wired into live templates. `index.json` retains **six disabled sections** as dead weight. Header ships settings literally labeled "Mock Wishlist Count" and "Use mock cart count of 3".

### Issue 9 — Fragile, string-coupled logic
- Fallback images chosen by matching **English** title substrings ("Mother"/"Sister"/"Bride") — breaks on rename or translation.
- Behavior coupled by CSS class/ID across files (`.js-video-call-modal`, `.header__cart-trigger`, `.best-sellers__wishlist-btn`), so renaming a class silently breaks cart/wishlist/modals.
- `made-for-every-bond` outputs `custom_icon_svg` **unescaped**; `mobile-promo-cards`/`instagram-reels` output text unescaped — markup-injection surface via the editor.

---

## 4. Maintenance workflow risk

Git history shows **130 `shopify[bot]` "Update from Shopify for theme" commits interleaved with 100 manual "fix" commits.** This means the theme is **edited live in the Shopify admin and pulled back**, in parallel with local development. That workflow:
- makes `settings_data.json` and JSON templates authoritative from *two* directions (admin + git),
- explains the accumulation of mock data and disabled sections (experiments left in place),
- and risks the admin overwriting local work (or vice-versa).

This is an architectural/process concern as much as a code one — see `MAINTAINABILITY_REPORT.md`.

---

## 5. Target architecture (the direction of travel)

```
Global Settings (settings_schema.json)
  ├─ Color tokens ── consumed via ── css-variables.liquid → :root vars
  ├─ Typography (body + heading)         ▲
  ├─ Button system                       │  every section reads var(--token)
  ├─ Spacing / container                 │  (no inline hex, no local fonts)
  └─ Brand identity (name/logo/contact/social)
                                          │
Theme Editor (section + block settings)   │
  ├─ Per-section copy, media, links, pickers, toggles
  └─ Repeatable blocks (slides, testimonials, pillars…)
                                          │
Code (Liquid / shared snippets / assets)  │
  ├─ ONE cart/wishlist system on the real Shopify cart
  ├─ Shared card snippet + shared carousel asset (no dup)
  ├─ Layout, breakpoints, animation, icon set
  └─ Locale strings (| t) for all UI micro-copy
```

The pieces to *build* are small (a fuller token set, a brand-identity group, one consolidated cart). The larger effort is *consumption*: pointing existing sections at the shared layers and deleting their local copies.

---

## 6. Verdict

The theme is **one strong refactor away from being genuinely scalable**. The design work and Shopify fundamentals are there; the exemplary sections prove the team knows the right patterns. What's missing is **discipline enforced by structure**: a real global token layer that sections *must* consume, clean Editor/Code boundaries, and a single source of truth for the cart and for brand identity. Fix Issues 1 and 2 first — they are the root; Issues 3–9 largely dissolve as those are corrected.

See `TOP_IMPROVEMENTS.md` for the prioritized, sequenced plan and `MAINTAINABILITY_REPORT.md` for the day-to-day maintenance findings.
