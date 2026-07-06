# Maintainability Report — Swastik Jewels Theme

> Day-to-day maintenance risks: what makes this theme hard to change safely, and what to do about each.
> Read-only assessment. No code was modified.

---

## Scorecard

| Dimension | Grade | One-line reason |
|-----------|:-----:|-----------------|
| Consistency (tokens) | 🔴 D | One brand rendered as 3 greens / 3+ golds / 4 font stacks. |
| Merchant editability | 🟠 C | Key copy (incl. entire PDP) hardcoded outside schemas. |
| Correctness (cart) | 🔴 D | Mock cart/wishlist diverges from the real Shopify cart. |
| Duplication / DRY | 🟠 C− | new-arrivals≈best-sellers; 3 drawers; `formatMoney` ×3. |
| Internationalization | 🟠 C− | ~8/40 sections localized; half-finished. |
| Data honesty | 🔴 D | Fake products/reviews/counts/contact info shipped. |
| Performance hygiene | 🟠 C | Huge inline CSS/JS per section; hardcoded font `<link>`; MutationObserver. |
| Security hygiene | 🟠 C | Unescaped editor output (raw SVG, promo/reel text). |
| Stock-surface quality | 🟢 A− | Boilerplate sections are clean and correct. |
| Process / workflow | 🟠 C | Live-admin edits pulled into git alongside manual commits. |

---

## 1. Consistency & the token layer

**Finding.** `snippets/css-variables.liquid` defines the right `:root` variables, but sections bypass them and hardcode hex/fonts. Result: `#013F3E` vs `#0a2a26` vs `#0b2e27`; `#D4AF37` vs `#b38245` vs `#c5a47e`; Montserrat vs Inter+Merriweather vs Playfair+Inter; container `1600px`/`1400px`/`80rem`.

**Why it hurts maintenance.** A rebrand or seasonal palette change means editing dozens of files and hoping none were missed. There is no single lever.

**Recommendation.** Expand global tokens and refactor sections to consume `var(--*)` (see `GLOBAL_SETTINGS_GUIDE.md` GS1).
- **Why it matters**: consistency becomes structural, not a matter of discipline.
- **Benefits**: one-lever re-skin; smaller section CSS; no drift.
- **Trade-offs**: broad but low-risk find/replace; must pick canonical values.
- **Difficulty**: Medium–High. **Long-term impact**: Very High.
- **Home**: Global Settings (values) + Code (consumption).

## 2. The mock cart / wishlist system — top correctness risk

**Finding.** `theme-ajax-sync.liquid` runs `handleAddToCartSuccess()` on both success *and* failure of `/cart/add.js`; `cart-drawer.liquid` shows localStorage "mock" items when the real cart is empty; prices are DOM-scraped; wishlist is localStorage-only; three drawers coexist with three `formatMoney` copies.

**Why it hurts maintenance.** Two sources of truth for the cart is the hardest class of bug to reason about — badge counts, drawer contents, and the real checkout can all disagree. Any change risks widening the gap.

**Recommendation.** Consolidate to **one** drawer system reading the **real** Shopify cart (`/cart.js`, `/cart/add.js`, `/cart/change.js`); remove the mock fallback and DOM price-scraping; make wishlist server-backed or clearly labeled device-local.
- **Why it matters**: correctness of the core purchase flow.
- **Benefits**: badge = drawer = checkout, always; one code path to maintain.
- **Trade-offs**: real behavioral refactor; needs careful QA of add/remove/qty/checkout.
- **Difficulty**: High. **Long-term impact**: Very High.
- **Home**: Code.

## 3. Duplication

**Finding.** `new-arrivals` and `best-sellers` duplicate ~575 lines of card CSS + the card carousel JS; header/ornament markup repeats across 3 sections; nav fallback duplicated desktop/mobile; `collection.lab-grown.json` is an unedited clone of `collection.json`; product-card markup partially reimplemented in sections.

**Why it hurts maintenance.** A card or carousel fix must be applied in several places; they *will* drift.

**Recommendation.** Extract a shared product-card + shared carousel (snippet + one JS asset), a shared section-header snippet; always render `snippets/product-card.liquid`.
- **Why it matters**: fixes land once. **Benefits**: less code, consistent behavior.
- **Trade-offs**: upfront extraction + regression testing. **Difficulty**: Medium.
- **Long-term impact**: High. **Home**: Code.

## 4. Internationalization

**Finding.** Only `store-highlights`, `testimonials-slider`, `gold-collection-showcase`, `discover-grid`, `collections`, `custom-section` + stock sections use `t:`/`| t`. ~30 sections are raw English; several hardcode strings outside their schema.

**Why it hurts maintenance.** Half-done i18n is the worst state — every new locale requires first *finding* and extracting scattered strings.

**Recommendation.** Extract all UI micro-copy to `locales/en.default.json` via `| t` (see `CODE_VS_EDITOR.md` GR2).
- **Difficulty**: Medium (mechanical). **Long-term impact**: High. **Home**: Global (locale).

## 5. Data honesty

**Finding.** Fake catalog (`best-sellers-fallback-grid`), fake reviews/ratings/specs (`product.liquid`), fake reels counts, placeholder contact data — all as defaults that can render live. Some claims (fabricated reviews, "BIS Hallmarked/18K Gold" on fake items) carry **legal/advertising** exposure in India.

**Recommendation.** Empty all fake defaults; render real products or nothing; source specs from metafields; use a real review app or remove ratings (see `CODE_VS_EDITOR.md` GR4).
- **Difficulty**: Low–Medium. **Long-term impact**: High (trust + legal). **Home**: Code (defaults) + Editor (real content).

## 6. Performance hygiene

**Finding.** 200–660 lines inline CSS + up to ~290 lines inline JS per section; `hero-banner` uses raw `<script>` (per-page, breaks dedup); `instagram-reels` uses `{%- style -%}`; `theme.liquid` hardcodes a 4-family Google Fonts `<link>` (render-blocking) and runs a permanent `MutationObserver` to hide a captcha node.

**Recommendation.** Normalize all inline JS to `{% javascript %}` and CSS to `{% stylesheet %}` (so Shopify dedupes them); move fonts into font settings (GS3); replace the MutationObserver hack with a CSS-only rule if possible.
- **Difficulty**: Medium. **Long-term impact**: Medium–High (Core Web Vitals). **Home**: Code + Global.

## 7. Security hygiene

**Finding.** `made-for-every-bond` outputs `custom_icon_svg` unescaped; `mobile-promo-cards` and `instagram-reels` output all block/section text without `| escape`; `gifts-for-him-her` uses unescaped `aria-label`s.

**Recommendation.** Remove the raw-SVG textarea (use the icon `select` set); add `| escape` to all editor-sourced text output.
- **Difficulty**: Low. **Long-term impact**: Medium. **Home**: Code.

## 8. Dead code & dev artifacts

**Finding.** `hello-text.liquid` + `index.page-1/2/3.json` ("Hello Page 1/2/3") stubs; six disabled sections retained in `index.json`; header "Mock" settings; dead `for-every-you.subtitle`, unused `logo_image`/`gold_price`/`button_link`; likely-dead `collection.liquid`; `component-product-card.css` vs inline card CSS coexisting.

**Recommendation.** Delete stubs, dead settings, and disabled sections not intended for use; confirm and remove superseded `collection.liquid`.
- **Difficulty**: Low. **Long-term impact**: Medium (clarity). **Home**: Code.

## 9. Process / workflow risk

**Finding.** History: 130 `shopify[bot]` "Update from Shopify" commits interleaved with 100 manual "fix" commits — the theme is edited live in admin **and** in git. `settings_data.json`/templates are authoritative from two directions.

**Why it hurts maintenance.** Admin edits can silently overwrite local work (and vice-versa); experiments (mock data, disabled sections) accumulate because the live store is the working surface.

**Recommendation.**
- Establish a clear direction of authority: develop code in git, treat `shopify theme pull` of `settings_data.json`/templates as merchant-content sync only; avoid editing section *Liquid* in the admin.
- Adopt `shopify theme check` in a pre-commit/CI step (config already exists: `.theme-check.yml` extends `recommended`) to catch unescaped output, undefined objects, and deprecated tags automatically.
- Use a dev/unpublished theme for experiments so stubs never reach the live theme.
- **Difficulty**: Low (process). **Long-term impact**: High. **Home**: Process/Code.

---

## Quick-reference: effort vs impact

| Fix | Effort | Impact | Priority |
|-----|:------:|:------:|:--------:|
| Consolidate cart/wishlist onto real Shopify cart | High | Very High | 1 |
| Expand + enforce global token layer | Med–High | Very High | 2 |
| Purge mock data & dead settings | Low–Med | High | 3 |
| Brand-identity single source of truth | Medium | High | 4 |
| Extract shared card/carousel/header | Medium | High | 5 |
| Finish i18n (extract UI copy) | Medium | High | 6 |
| Add `| escape` / remove raw SVG | Low | Medium | 7 |
| Normalize inline JS/CSS + fonts | Medium | Med–High | 8 |
| Remove dev stubs / disabled sections | Low | Medium | 9 |
| Adopt theme-check + workflow discipline | Low | High | 10 |
