# Top Improvements — Swastik Jewels Theme

> The prioritized, sequenced plan. Each item uses the full template:
> **Recommendation · Why it matters · Benefits · Trade-offs · Difficulty · Long-term impact · Home (Editor / Global / Code)**.
> Read-only — this is the roadmap, not an implementation. Supporting detail lives in the other five documents.

**Sequencing logic**: fix the two root causes first (cart correctness, token layer). Most other issues shrink once those land. Ordered so each phase de-risks the next.

---

## Phase 1 — Stop the bleeding (correctness & trust)

### 1. Consolidate to a single cart/wishlist system on the real Shopify cart
- **Recommendation**: Replace the three overlapping drawers (`cart-drawer`, `wishlist-drawer`, `snippets/sidebar-drawer`) with one, reading/writing the real cart via `/cart.js`, `/cart/add.js`, `/cart/change.js`; remove the localStorage "mock" fallback and the both-branches (`.then`+`.catch`) success handler in `theme-ajax-sync.liquid`; stop DOM-scraping prices; make wishlist server-backed or explicitly device-local. Collapse the 3 `formatMoney` copies into one.
- **Why it matters**: Today the badge, the drawer, and the real checkout can disagree — a failed add still increments the count, and an empty cart can display fabricated items. This is the core purchase flow.
- **Benefits**: Badge = drawer = checkout, always; one code path; correct prices/currency via `| money`/`cart.currency`.
- **Trade-offs**: Real behavioral refactor; needs thorough QA of add/remove/qty/checkout across devices.
- **Difficulty**: High.
- **Long-term impact**: Very High.
- **Home**: **Code**.

### 2. Purge mock/fake data from the theme
- **Recommendation**: Empty the fake catalog (`best-sellers-fallback-grid.liquid`), the PDP's fake reviews/rating/"23% OFF"/spec table, fake reels view counts, fake testimonials, and placeholder contact data (`123 Mock Address Lane`, `whatsapp-request@placeholder.com`, `+1234567890`). Render real products or an honest empty state; source specs from **product metafields**; use a real review app or drop ratings.
- **Why it matters**: Fabricated reviews and unverifiable "BIS Hallmarked / 18K Gold" claims on fake items are trust and **advertising-law** risks in India; placeholder contact info can ship live.
- **Benefits**: No accidental fake launches; honest empty states that prompt real content; legal safety.
- **Trade-offs**: A fresh install looks emptier (correct — it signals "add real content").
- **Difficulty**: Low–Medium.
- **Long-term impact**: High.
- **Home**: **Code** (defaults) + **Editor** (real content).

---

## Phase 2 — Fix the foundation (consistency)

### 3. Build and enforce a real global design-token layer
- **Recommendation**: Expand `settings_schema.json` (surface/border/muted/button colors, heading font, button system, container width, spacing scale — see `GLOBAL_SETTINGS_GUIDE.md`), then refactor every section to consume `var(--token)` from `css-variables.liquid` instead of inline hex/fonts. Retire palette variants B/C onto the canonical tokens.
- **Why it matters**: One brand currently renders as 3 greens, 3+ golds, and 4 font stacks because the token layer, though present, is bypassed.
- **Benefits**: One-lever re-skin; brand consistency becomes structural; section CSS shrinks; future sections inherit the system.
- **Trade-offs**: Broad (but low-risk) find/replace; must choose canonical values where several compete; visual QA.
- **Difficulty**: Medium–High.
- **Long-term impact**: Very High.
- **Home**: **Global Settings** (values) + **Code** (consumption).

### 4. Create a Brand-Identity single source of truth
- **Recommendation**: One global group for name, logo, tagline, founding year, phone, email, address, WhatsApp number, and social links; point header, footer, contact page, whatsapp-widget, and expert-consultation at it. Register or remove the stranded `checkout_logo_image`.
- **Why it matters**: These facts are duplicated and already contradict each other (1985 vs 1997; three phone numbers; two emails) — a customer-facing failure.
- **Benefits**: One edit propagates; impossible to hold contradictory brand facts; correct contact info guaranteed.
- **Trade-offs**: ~5 sections refactored to read globals.
- **Difficulty**: Medium.
- **Long-term impact**: High.
- **Home**: **Global Settings**.

### 5. Move font loading into font settings; drop the hardcoded `<link>`
- **Recommendation**: Reconcile the four display fonts to a deliberate 1–2, load them via `type_primary_font` + a new `type_heading_font` (`font_url`/`font_face`), and remove the render-blocking Google Fonts `<link>` in `layout/theme.liquid`.
- **Why it matters**: The hardcoded link bypasses the theme's font system, blocks first paint, and lets sections drift onto off-brand stacks.
- **Benefits**: Faster first paint (Shopify-CDN fonts, fewer blocking requests); one typography lever; no off-brand fonts.
- **Trade-offs**: Must pick canonical fonts; visual QA.
- **Difficulty**: Medium.
- **Long-term impact**: High.
- **Home**: **Global Settings** + **Code**.

---

## Phase 3 — Unlock the merchant (editability & i18n)

### 6. Give `product.liquid` a real schema; move policy copy to Editor/Global
- **Recommendation**: Add settings/blocks for trust badges and shipping/returns/care copy (or make them global, since they repeat store-wide); render specs from metafields; compute discount % from real prices; render price with `| money`.
- **Why it matters**: The most important page has **zero** merchant control and hardcodes copy that will be wrong for every real product.
- **Benefits**: Merchants edit policies/badges without a developer; specs are correct per product; currency-safe.
- **Trade-offs**: PDP refactor; metafield definitions to set up.
- **Difficulty**: Medium–High.
- **Long-term impact**: High.
- **Home**: **Editor** (blocks) + **Global** (store-wide policy) + **Code** (metafield rendering).

### 7. Expose the hardcoded storefront copy that merchants should own
- **Recommendation**: Promote strings currently baked outside schemas — "SHOP NOW", "VIEW ALL COLLECTIONS", newsletter placeholder/button/success, "FOR" tagline, drawer/form labels — into section settings (page-specific) or locale strings (cross-page).
- **Why it matters**: Merchants can't run a promo or fix wording without a developer.
- **Benefits**: Marketing autonomy; consistent, localizable wording.
- **Trade-offs**: Larger schemas/locale file; content-migration pass.
- **Difficulty**: Medium.
- **Long-term impact**: High.
- **Home**: **Editor** + **Global** (locale).

### 8. Finish internationalization
- **Recommendation**: Extract all remaining UI micro-copy to `locales/en.default.json` via `| t`; adopt `t:` schema keys consistently.
- **Why it matters**: The theme is half-localized — the costliest state to complete later.
- **Benefits**: New locales become drop-in; wording centralized.
- **Trade-offs**: One-time extraction pass.
- **Difficulty**: Medium (mechanical).
- **Long-term impact**: High.
- **Home**: **Global** (locale).

---

## Phase 4 — Harden & tidy (DRY, security, performance, hygiene)

### 9. Extract shared card / carousel / section-header components
- **Recommendation**: One product-card snippet, one carousel JS asset, one section-header snippet; `new-arrivals`/`best-sellers` and the three ornamented sections consume them.
- **Why it matters**: ~575 duplicated card lines and repeated header markup will drift; fixes must currently be applied several times.
- **Benefits**: Fix-once; consistent behavior; less code.
- **Trade-offs**: Extraction + regression testing.
- **Difficulty**: Medium.
- **Long-term impact**: High.
- **Home**: **Code**.

### 10. Close the escaping / raw-SVG holes
- **Recommendation**: Remove the `custom_icon_svg` raw-SVG textarea (use the curated icon `select`); add `| escape` to all editor-sourced text output (`mobile-promo-cards`, `instagram-reels`, `gifts-for-him-her` aria-labels).
- **Why it matters**: Unescaped editor input is a markup-injection surface.
- **Benefits**: Safer; consistent output handling.
- **Trade-offs**: Minimal.
- **Difficulty**: Low.
- **Long-term impact**: Medium.
- **Home**: **Code**.

### 11. Normalize inline JS/CSS and the head hacks
- **Recommendation**: Convert raw `<script>`/`{%- style -%}` to `{% javascript %}`/`{% stylesheet %}` so Shopify dedupes them; replace the captcha `MutationObserver` with a CSS-only rule where feasible.
- **Why it matters**: Per-page inline blocks defeat Shopify's asset de-duplication and inflate page weight; a permanent observer is fragile.
- **Benefits**: Better Core Web Vitals; less fragile head.
- **Trade-offs**: Broad but mechanical.
- **Difficulty**: Medium.
- **Long-term impact**: Medium–High.
- **Home**: **Code**.

### 12. Remove dev artifacts and dead settings
- **Recommendation**: Delete `hello-text.liquid` + `index.page-1/2/3.json`; remove header "Mock" settings, dead `for-every-you.subtitle`, unused `logo_image`/`gold_price`/`button_link`; confirm/remove superseded `collection.liquid`; drop the six disabled sections in `index.json` if not intended for use.
- **Why it matters**: Stubs and dead settings mislead merchants and clutter the codebase.
- **Benefits**: A schema that means what it says; smaller surface.
- **Trade-offs**: Verify nothing references them first.
- **Difficulty**: Low.
- **Long-term impact**: Medium.
- **Home**: **Code**.

### 13. Adopt `shopify theme check` + a clear source-of-authority workflow
- **Recommendation**: Wire the existing `.theme-check.yml` (`recommended`) into pre-commit/CI; treat git as authoritative for Liquid and `shopify theme pull` as merchant-content (settings/templates) sync only; run experiments on an unpublished theme.
- **Why it matters**: History shows live-admin edits pulled into git alongside manual commits — two sources of truth, which is how mock data and disabled sections accumulated and how work can get overwritten.
- **Benefits**: Automated catch of unescaped output/undefined objects/deprecated tags; no admin/local clobbering; experiments never reach production.
- **Trade-offs**: Process discipline; a little CI setup.
- **Difficulty**: Low.
- **Long-term impact**: High.
- **Home**: **Process / Code**.

---

## One-page priority matrix

| # | Improvement | Home | Difficulty | Impact |
|:-:|-------------|------|:----------:|:------:|
| 1 | Single real-cart drawer system | Code | High | Very High |
| 2 | Purge mock/fake data | Code + Editor | Low–Med | High |
| 3 | Global token layer + enforce | Global + Code | Med–High | Very High |
| 4 | Brand-identity single source | Global | Medium | High |
| 5 | Fonts into settings; drop `<link>` | Global + Code | Medium | High |
| 6 | Real PDP schema + metafield specs | Editor + Global + Code | Med–High | High |
| 7 | Expose hardcoded storefront copy | Editor + Global | Medium | High |
| 8 | Finish i18n | Global (locale) | Medium | High |
| 9 | Extract shared components | Code | Medium | High |
| 10 | Escaping / remove raw SVG | Code | Low | Medium |
| 11 | Normalize inline JS/CSS + head | Code | Medium | Med–High |
| 12 | Remove dev stubs / dead settings | Code | Low | Medium |
| 13 | theme-check + workflow authority | Process | Low | High |

**Start with #1 and #3** — they are the two root causes; #2 and #4 are fast trust wins to run alongside. Everything in Phase 4 becomes easier once the foundation (Phase 2) is in place.
