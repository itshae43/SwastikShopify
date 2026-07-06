# Code vs Theme Editor vs Global Settings — Per-Section Audit

> For every section and component: what each option **currently** is, and where it **should** live.
> Legend for the "Should be" column: **[E]** Theme Editor · **[G]** Global Settings · **[C]** Code.
> Framework and rationale: see `THEME_EDITOR_GUIDELINES.md`.

This is a **read-only audit**. Nothing here is a code change — it is the target-state mapping.

---

## How to read this

Each section lists:
- **Currently editor-controlled** — what its `{% schema %}` exposes today.
- **Currently hardcoded** — what is baked into Liquid/CSS/JS.
- **Verdict** — the recommended home for each notable option, with the reasoning.

A recurring theme: **copy and brand tokens are in the wrong bucket almost everywhere.** Rather than repeat the full 7-field recommendation for all 40 sections, the cross-cutting recommendations are consolidated in §"Global recommendations" at the end; per-section rows call out what is specific.

---

## A. Homepage merchandising sections

### `hero-banner.liquid`
- **Editor today**: `autoplay`, `autoplay_speed`, `hero_size`, `hero_height`, `overlay_opacity`; per-`slide` block: images (desktop/mobile), alignment, subheading, title, description, 2× button label+link. Good block model.
- **Hardcoded today**: a duplicate fallback slide (copy + `Slideshow_Desktop_1_New.png`); slide markup uses raw `<script>` (per-page, not deduped); accent `#D4AF37`, primary `#013F3E`, mobile height `694px` (twice), easing curves.
- **Verdict**:
  - Slide content, images, buttons → **[E]** ✅ already correct.
  - `autoplay`, `autoplay_speed`, `overlay_opacity` → **[E]** ✅ (genuinely editorial).
  - `hero_height` / `hero_size` → **[E]** acceptable, but clamp the range in **[C]**.
  - Colors, `694px`, easing, the slideshow engine → **[C]** (consume global tokens; convert `<script>` to `{% javascript %}`).
  - The no-blocks **fallback slide** → **[C]** but change default to *empty*, not fake copy.

### `latest-collections.liquid`
- **Editor today**: `title`, `bg_color`, paddings, footer button (label/link + 4 button colors); per-`collection_card` block: image, title, subtitle, link, `text_position` (9 options), `title_style`, `custom_title_color`, `subtitle_color`, **title font size desktop/mobile/weight**.
- **Hardcoded today**: keyword→asset fallback (`bond_mothers.png`, `testimonial_bg_silk.png` — borrowed from other sections); dead `nth-child(4)` CSS; `#013F3E`, `Montserrat`, `max-width:1600px`.
- **Verdict**:
  - Card image/title/subtitle/link, `text_position` → **[E]** ✅.
  - 4 button colors + `custom_title_color` + `subtitle_color` → **[G]** (button + text tokens); replace with a `title_style` **[E]** `select` only.
  - **Per-block font size ×3 + weight** → **[C]** — over-granular; collapse to one "size" `select`. (See guideline §5.)
  - Keyword→asset fallback logic → **[C]**, defaults empty.

### `discover-grid.liquid`
- **Editor today**: `subheading`, `title`, `description`, `bg_color`; per-`card`: image, image_mobile, link. Uses `t:` locale keys for some labels.
- **Hardcoded today**: section-level default strings; layout comments assume fixed categories (Rings/Earrings/Pendants/Tennis); colors `#0b2e27` / `#c5a47e` (a *third* palette variant); `Georgia, serif`.
- **Verdict**:
  - Card image/link, section copy → **[E]** ✅.
  - `bg_color` picker → **[G]**-bound `select`.
  - `#0b2e27` / `#c5a47e` / `Georgia` → **[C]** consuming **[G]** tokens (these diverge from brand).
  - Bento grid structure → **[C]** ✅.
  - Finish the i18n it started → locale **[G]**.

### `gold-collection-showcase.liquid`
- **Editor today**: subheading/heading/description/button, `bg_color`/`text_color`/`accent_color`; per-`collection` block: collection picker + title/image override. **Fully uses `t:` keys** (cleanest schema).
- **Hardcoded today**: `#fbf6f0` / `#0a2a26` / `#b38245` (palette variant B); `Georgia, serif`.
- **Verdict**:
  - Collection picker + overrides + copy → **[E]** ✅ (this is the model other sections should follow).
  - 3 color pickers → **[G]** tokens via `select`.
  - Uses real `placeholder_svg_tag` (not fake assets) → **[C]** ✅ good.

### `featured-collection.liquid`
- **Editor today**: title, subheading, collection, `products_to_show`, `columns_desktop`, `columns_mobile`, `show_view_all`.
- **Hardcoded today**: fallback mock products "Exquisite Masterpiece #N" at **₹125,000**; "Sale" badge; "View all masterpieces"; brand colors.
- **Verdict**:
  - Collection, counts, columns, toggle → **[E]** ✅.
  - "Sale"/"View all masterpieces" strings → **[E]** or locale **[G]**.
  - **Mock ₹125,000 products** → **[C]**, default empty (must never render on a live store).

### `featured-categories.liquid`
- **Editor today**: `title` (default typo `"Jewelry categor"`), `bg_color`; per-`category` block: title, image, `item_count` text, link.
- **Hardcoded today**: title→placeholder-PNG `case` map; a no-blocks fallback that **fully duplicates** the preset's 5 categories; `onerror`→`logo.png`; inconsistent count formatting ("12+ Items" vs "12 + ITEMS").
- **Verdict**:
  - Category blocks (title/image/count/link) → **[E]** ✅.
  - Fix the default typo → **[C]**.
  - Duplicate fallback loop → **[C]**, remove or empty.
  - `item_count` as free text → keep **[E]** but standardize format in **[C]**.

### `new-arrivals.liquid` & `best-sellers.liquid`
- **Editor today**: section copy + colors; `new-arrivals` has a `collection` picker; `best-sellers` has up to 3 `tab` blocks (title + collection).
- **Hardcoded today**: **large fabricated product catalogs** with INR prices bypassing `| money` (₹24,999 etc.), fake discounts, `best_seller_*.png` assets; near-identical ~575-line CSS and card-carousel JS duplicated between the two ("Same behavior as best sellers" comment); `best-sellers-fallback-grid.liquid` snippet ships a full fake catalog with fake "BIS Hallmarked / 18K Gold" claims.
- **Verdict**:
  - Collection / tab→collection mapping, section copy → **[E]** ✅ (this is the right control surface).
  - The **fake product data / fallback grid** → **[C]**, must default to empty; a live store should show real products or nothing.
  - Prices → **[C]** use `| money` (never hardcode ₹).
  - Duplicated card CSS/JS → **[C]** extract to a shared snippet/asset (see `MAINTAINABILITY_REPORT.md`).

---

## B. Homepage content / storytelling sections

### `brand-story.liquid`
- **Editor today**: image, `layout` (left/right), `bg_color` (white/cream/dark `select` — good pattern), subheading/title/content/button. All copy is settings-driven ✅.
- **Hardcoded today**: brand palette hex as SVG/CSS fallbacks; `3.8rem`/`8rem` magic numbers.
- **Verdict**: Copy/image/layout/bg-select → **[E]** ✅. Colors → **[G]**. This section is close to correct; the `bg_color` `select` is the pattern to copy elsewhere.

### `why-choose-us.liquid`
- **Editor today**: title/subheading/description/`bg_color`; up to 4 `pillar` blocks (title, description, `icon` select).
- **Hardcoded today**: icon SVG paths (correctly, as a curated set); `#F8F3ED`/`#F0E8E2` magic colors not exposed; header/ornament markup duplicated with shop-by-occasion & testimonials.
- **Verdict**: Pillar content + icon `select` → **[E]** ✅ (icon-as-select is the correct model — contrast with `made-for-every-bond`). Colors → **[G]**. Shared header markup → **[C]** extract to a snippet.

### `shop-by-occasion.liquid`
- **Editor today**: section copy, `bg_color`, `view_all_link`; up to 4 `occasion` blocks (title/description/image/link/`icon` select).
- **Hardcoded today**: **"SHOP NOW" and "VIEW ALL COLLECTIONS" buttons are hardcoded outside the schema** (merchant cannot edit); title→placeholder-PNG fallback; `#012b2a` magic hover.
- **Verdict**: Occasion blocks → **[E]** ✅. **Button labels → [E]** (currently unreachable — high-value fix). Colors → **[G]**.

### `for-every-you.liquid`
- **Editor today**: heading/subheading/`bg_color`/`text_color`; per-`slide`: image, image_mobile, title, `subtitle` (**declared but never rendered — dead**), link.
- **Hardcoded today**: coverflow JS (~195 lines); slides rendered 3× in DOM; fonts `Playfair Display`/`Inter` (diverge from theme).
- **Verdict**: Slide image/title/link → **[E]** ✅. Coverflow engine, 3× duplication, breakpoints → **[C]** ✅ (correctly coded). **Remove the dead `subtitle` setting → [C].** Fonts → **[G]**.

### `made-for-every-bond.liquid`
- **Editor today**: headings/description/button, `bg_color`/`text_color`/`accent_color`; per-`bond`: image, title, subtitle, link, `icon` select, **`custom_icon_svg` raw-SVG textarea**.
- **Hardcoded today**: title-string→asset fallback (matches English "Mother"/"Sister"/"Bride" — breaks on rename/translation); palette B (`#b38245`/`#0a2a26`).
- **Verdict**: Bond content + icon `select` → **[E]** ✅. **`custom_icon_svg` (raw, unescaped) → [C] remove** — this is a security/consistency hole, not a merchant feature (guideline §5). Colors → **[G]**. String-match fallback → **[C]**.

### `store-highlights.liquid`
- **Editor today**: 5 color settings + autoplay/speed; per-`highlight`: `icon` select, title, description. **Uses `t:` keys** ✅.
- **Hardcoded today**: `gap=16` in JS twice; icon option labels not localized.
- **Verdict**: Highlight blocks → **[E]** ✅. The 6 color settings → **[G]** tokens (this section alone exposes bg/border/icon/text/desc colors — textbook over-exposure). Autoplay/speed → **[E]** ✅.

### `gifts-for-him-her.liquid`
- **Editor today**: Him/Her image + title + link (×2), 4 color settings.
- **Hardcoded today**: **"FOR" tagline hardcoded 4× outside schema**; `gifts_him.png`/`gifts_her.png` fallbacks; unescaped titles in `aria-label`.
- **Verdict**: Images/titles/links → **[E]** ✅. **"FOR" → [E]** (or [C] if it's a fixed design element — decide, then make it reachable). Colors → **[G]**. Escaping → **[C]** fix.

### `mobile-promo-cards.liquid`
- **Editor today**: paddings; per-`promo_card`: 2 gradient colors, top text, huge number, suffix, divider toggle, 2 subtitles, bottom text, link. Fully block-driven ✅.
- **Hardcoded today**: **Liquid `default` gradient (`#9B1A22`/`#540D12`) ≠ schema default (`#A91D22`/`#5A0A0D`)** — two different reds; no `| escape` on any output.
- **Verdict**: Promo content (%, copy, link) → **[E]** ✅ (this is legitimately campaign content). Gradient colors → **[E]** acceptable (promo cards are intentionally loud) but reconcile the two defaults in **[C]** and add `| escape`.

### `instagram-reels.liquid`
- **Editor today**: section copy + button + `bg_color`; per-`reel`: video, image, `view_count` text.
- **Hardcoded today**: **fabricated view counts** as defaults (12.6K…); uses `{%- style -%}` not `{% stylesheet %}`; unique golds `#d8c3b1`/`#9a7d65`; unescaped output; inline `onclick`.
- **Verdict**: Reel video/image/link → **[E]** ✅. `view_count` → **[E]** but default empty (fabricated engagement is a trust/legal risk). Colors → **[G]**. `{%- style -%}` → **[C]** normalize to `{% stylesheet %}`.

### `testimonials-slider.liquid`
- **Editor today**: section copy, 3 colors, autoplay/speed; per-`testimonial`: rating, text, author, location. **Uses `t:` keys** ✅.
- **Hardcoded today**: fake defaults (Arjun/Priya/Rohan reviews); WebKit-only `WebKitCSSMatrix`; clone-based infinite loop (3× DOM).
- **Verdict**: Testimonial blocks → **[E]** ✅ (correct model). **Default reviews → [C] empty** (shipping fake reviews is a serious trust issue). Colors → **[G]**. Slider engine → **[C]** ✅.

### `newsletter.liquid`
- **Editor today**: `bg_color` (white/cream/dark select ✅), subheading/title/description.
- **Hardcoded today**: **placeholder "Enter your email address", button "Subscribe", and success message hardcoded outside schema** — not editable or localizable.
- **Verdict**: Copy + bg select → **[E]** ✅. **Placeholder / button / success → [E] or locale [G]** (high-value, low-effort). Colors → **[G]**.

---

## C. Commerce core

### `product.liquid` (PDP) — **highest-priority gap**
- **Editor today**: **`"settings": []` — nothing.** Zero merchant control.
- **Hardcoded today**: mock price/title/description defaults (₹24,999 / "Golden Teardrop Pendant" / `mock-pendant-id` / variant `998877`); **"23% OFF" badge unrelated to real price**; **fake "128 reviews" + always-5-stars**; **fabricated spec table (3.45 g, SI-IJ color)** that is wrong for every real product; hardcoded trust badges, shipping/returns/care copy; breadcrumb "Home"; `₹` hardcoded (not locale-aware); ~660 lines CSS + ~290 lines JS.
- **Verdict**:
  - Variant logic, gallery, accordion behavior, add-to-cart JS → **[C]** ✅ (correctly coded).
  - **Trust badges, shipping/returns/care copy → [E]** (blocks) or **[G]** (they repeat store-wide) — merchants must be able to edit policy text.
  - **Specs (gold weight, purity, clarity) → product metafields**, rendered in **[C]** — never hardcoded; they differ per product.
  - **Reviews/rating → real review app or metafield**, or remove. Fake reviews are a trust/legal risk.
  - "ADD TO CART"/"BUY IT NOW"/"IN STOCK"/"Home" → locale **[G]**.
  - Discount % → computed in **[C]** from real prices, not a hardcoded "23% OFF".
  - Price rendering → `| money` in **[C]**, not hardcoded `₹`.

### `header.liquid`
- **Editor today**: `logo_image` (**unused**), `logo_width`, `gold_price` (**unused**), `wishlist_count` ("Mock Wishlist Count", **unused**), `mock_cart_count` ("Use mock cart count of 3", **unused**), `show_announcement`, 3 announcement texts, `menu` (link_list).
- **Hardcoded today**: logo forced to `logo.png` (ignores setting); brand text "Swastik/JEWELS"; **full fallback nav tree** (Jewellery/Bridal/Diamonds/Collections + hardcoded collection handles) duplicated in desktop + mobile; `'our story'` string special-case; gold-rate fallback `15,620`.
- **Verdict**:
  - `menu` (link_list), announcement toggle + texts → **[E]** ✅ (announcement text ideally locale **[G]**).
  - **Wire up `logo_image` → [E]/[G]** (logo is brand identity → prefer **[G]**), then delete the hardcoded `logo.png`.
  - **Delete dead "Mock" settings → [C]** (they mislead merchants).
  - Fallback nav tree → **[C]**, but ideally require a real menu (empty fallback), since hardcoded handles rot.
  - `gold_price` setting vs metafield → pick one; if metafield is the source, delete the setting.

### `footer.liquid`
- **Editor today**: brand name/description, 4 social links, 2 link_list menus, contact address/phone/email, 3 policy URLs, 3 footer colors. **Well-structured** — the cleanest brand section.
- **Hardcoded today**: "Quick Links"/"Customer Care" headings; fallback link trees to pages that may not exist; **"since 1985" default contradicts header's "SINCE 1997"**; `.serif-font` class applied then overridden.
- **Verdict**:
  - **Brand name, contact info, social links → [G]** (they belong store-wide, and duplicating them here vs header caused the 1985/1997 contradiction).
  - Menus → **[E]** ✅.
  - Section headings → locale **[G]**.
  - Footer colors → **[G]** tokens.

### `main-collection-product-grid.liquid`
- **Editor today**: only `bg_color`.
- **Hardcoded today**: all UI labels ("FILTERS", "Clear All", "Sort by:", "No products found", "Next/Prev"); `₹` in slider; **`class_prefix: 'best-sellers'` hardcoded** on every card (copy-paste); fonts `Inter`/`Merriweather` (diverge from theme). Uses **real Shopify filtering/sort/pagination** ✅.
- **Verdict**: Filtering/sort/pagination logic → **[C]** ✅ (genuinely functional). UI labels → locale **[G]**. Fonts → **[G]** (currently off-brand). `class_prefix` → **[C]** fix. `bg_color` → **[G]**.

### `main-collection-banner.liquid`
- **Editor today**: title (override), image, subtitle (richtext), button label/link, 4 colors. Falls back to `collection.title`/`.description` ✅.
- **Hardcoded today**: default "LAB GROWN DIAMONDS" (can mislabel other collections); `&rarr;`; `.serif-font`.
- **Verdict**: All content → **[E]** ✅ (this section is well-designed). Colors → **[G]**. Default title → **[C]** make blank so it falls back to the real collection title.

### `collection.liquid`, `collections.liquid`, `cart.liquid`
- **Status**: Stock Shopify boilerplate — use `| t`, `| money`, real objects, minimal schema. **These are correct.**
- **Verdict**: Leave as **[C]** stock. Note `collection.liquid` overlaps `main-collection-product-grid` — likely dead (see `MAINTAINABILITY_REPORT.md`). `cart.liquid` is unstyled because the AJAX drawer is the real cart UI — acceptable, but verify it's a usable fallback.

---

## D. Drawers, services, utilities

### `cart-drawer.liquid` + `wishlist-drawer.liquid` + `snippets/sidebar-drawer.liquid`
- **Editor today**: none (`settings: []`); `whatsapp-widget` has `whatsapp_number`.
- **Hardcoded today**: all labels; **`₹`/`en-IN` `formatMoney` defined 3× separately**; **three overlapping drawer systems**; cart-drawer renders **localStorage mock items when the real cart is empty**; wishlist is **localStorage-only** (no server persistence); demo CDN placeholder image.
- **Verdict**:
  - Drawer structure/behavior → **[C]**.
  - Labels → locale **[G]**.
  - **Consolidate 3 drawers → 1**, one `formatMoney`, currency via `| money` / `cart.currency` → **[C]** (see `MAINTAINABILITY_REPORT.md` — this is the top functional risk).
  - **Mock-cart divergence from the real Shopify cart → [C] fix** (correctness, not configuration).

### `whatsapp-widget.liquid`
- **Editor today**: `whatsapp_number` (default `1234567890`; real value `8920905268` is set in `settings_data.json`).
- **Hardcoded today**: menu copy, 3 prefilled WhatsApp messages (English), `#25D366`, couples to video-call via `.js-video-call-modal`.
- **Verdict**: **`whatsapp_number` → [G]** (it's brand contact identity, also used by header/footer/expert-consultation — one source of truth). Message copy → **[E]** or locale **[G]**. Widget behavior → **[C]**.

### `video-call.liquid` & `expert-consultation.liquid`
- **Editor today**: banner copy/image/colors; expert-consultation has `contact_option` blocks.
- **Hardcoded today**: full modal form labels/time-pills; **`whatsapp-request@placeholder.com` silently submitted**; US phone placeholder on an INR store; `button_link` setting **ignored**; expert-consultation preset ships fake `+1234567890`.
- **Verdict**: Banner + contact-option blocks → **[E]** ✅. Form labels → locale **[G]**. **Placeholder email hack, US placeholder, dead `button_link` → [C] fix.** Fake preset numbers → **[C]** empty.

### `custom-contact-page.liquid`
- **Editor today**: heading/subheading/description, `map_embed` (raw HTML iframe), business hours, legal entity, email, phone, address.
- **Hardcoded today**: "How to Reach Us!", "within 24 hours" line, field labels — outside schema; `123 Mock Address Lane` default; raw `<style>` not `{% stylesheet %}`.
- **Verdict**: Contact fields → **[E]** ✅, but **email/phone/address/legal entity → [G]** (same brand-contact single-source-of-truth as footer/header/whatsapp). Field labels → locale **[G]**. Mock address default → **[C]** empty.

### `custom-section.liquid`, `blocks/group.liquid`, `blocks/text.liquid`, `snippets/image.liquid`, `snippets/meta-tags.liquid`, `snippets/css-variables.liquid`
- **Status**: Stock/clean, `t:`-localized, token-driven. **Correct as-is.**
- **Verdict**: Leave as **[C]**. `css-variables.liquid` is the **[G]** token layer other sections *should* consume but mostly don't — the fix is to make sections consume it, not to change this file.

### Utility & stub sections
- `article` / `blog` / `search` / `page` / `404` / `password` → stock, localized, correct → **[C]** leave.
- **`hello-text.liquid` + `index.page-1/2/3.json`** → **dev stubs ("Hello Page 1/2/3") shipped in the theme.** → **[C] remove** before production.

---

## Global recommendations (apply across the sections above)

### GR1 — Move brand identity to a single global source of truth
- **Recommendation**: Store name, logo, tagline, founding year, phone, email, address, WhatsApp number, social links live once in **Global Settings**; header/footer/contact/whatsapp/expert-consultation consume them.
- **Why it matters**: The same facts are duplicated and already contradict each other (1985 vs 1997; `1234567890` vs `8920905268` vs `+1234567890`; two emails).
- **Benefits**: One edit updates everywhere; no contradictions; correct contact info can't be half-updated.
- **Trade-offs**: Small refactor of ~5 sections to read globals.
- **Difficulty**: Medium.
- **Long-term impact**: High.
- **Home**: **[G]**.

### GR2 — Move all hardcoded UI micro-copy to locale files
- **Recommendation**: "ADD TO CART", "SHOP NOW", "Subscribe", "FILTERS", "Next/Prev", drawer/form labels → `locales/en.default.json`, rendered via `| t`.
- **Why it matters**: ~30 sections hardcode English; the theme is half-internationalized and merchants can't restyle CTAs.
- **Benefits**: Localizable; consistent wording; editable without touching Liquid.
- **Trade-offs**: One-time extraction pass; larger locale file.
- **Difficulty**: Medium (mechanical).
- **Long-term impact**: High (unlocks i18n + wording consistency).
- **Home**: **[G]** (locale) — with a few page-specific strings as **[E]**.

### GR3 — Replace per-section color pickers with token-bound selects
- **Recommendation**: Collapse the 3 competing green/gold palettes into the global tokens; expose only constrained `select`s where a merchant truly needs a per-section variant.
- **Why / Benefits / Trade-offs / Difficulty / Impact / Home**: see `THEME_EDITOR_GUIDELINES.md` R2 and `GLOBAL_SETTINGS_GUIDE.md`. **Home: [G] values, [E] select.**

### GR4 — Purge mock data and dead settings from code
- **Recommendation**: Empty all fake defaults (products, reviews, view counts, prices, contact placeholders) and delete unused schema settings (header "Mock" settings, `for-every-you.subtitle`, ignored `logo_image`/`gold_price`/`button_link`).
- **Why it matters**: Fake data can ship live (fake reviews, fake stock claims, fake catalog); dead settings mislead merchants.
- **Benefits**: No accidental fake launches; honest empty states; a schema that means what it says.
- **Trade-offs**: Sections look emptier in a fresh install (correct — prompts merchants to add real content).
- **Difficulty**: Low–Medium.
- **Long-term impact**: High (trust + maintainability).
- **Home**: **[C]** (defaults) + **[E]** (real content).
