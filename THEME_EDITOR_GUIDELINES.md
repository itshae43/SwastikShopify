# Theme Editor Guidelines — Swastik Jewels

> A decision framework for **what merchants control in the Theme Editor** vs **what developers keep in code**.
> Read this first — `CODE_VS_EDITOR.md` applies these rules section-by-section.

This is a **read-only architecture document**. It contains no code changes — only the rules and rationale for how configuration *should* be split going forward.

---

## 1. The core principle

Your stated goal is exactly right: **not everything should be editor-configurable.** A theme where every color, font, gap, and animation is a setting becomes *harder* to maintain and *easier* for a merchant to break than one with sharp, deliberate boundaries.

Every configurable value has three homes. Assign each one to exactly one:

| Home | What lives here | Who owns it | Changes how often |
|------|-----------------|-------------|-------------------|
| **Theme Editor** (section / block settings) | Per-section, per-campaign, per-page **content** | Merchant / marketing | Weekly–monthly |
| **Global Settings** (`config/settings_schema.json`) | Cross-cutting **design tokens & brand identity** | Merchant once, at setup | Rarely |
| **Code** (Liquid / CSS / JS) | **Structure, behavior, and consistency-critical presentation** | Developer | Per release |

The failure mode this theme currently has is **inversion**: content is hardcoded in `.liquid` files (so merchants *can't* edit it), while design tokens are duplicated inline in every section (so they *can't* stay consistent). The rules below correct that.

---

## 2. The decision test

For any value, ask these three questions in order. The **first "yes"** decides the home.

1. **"Must this look identical in every section for the brand to feel coherent?"**
   → **Global Settings.** (Brand colors, fonts, button style, corner radius, spacing rhythm.)

2. **"Would a non-technical merchant reasonably want to change this on their own, without a developer, as part of running the store?"**
   → **Theme Editor.** (Headings, body copy, images, links, which collection to feature, a testimonial, a promo %.)

3. **"Would exposing this let a merchant break layout, behavior, accessibility, or brand consistency — or does it require developer judgment?"**
   → **Code.** (Grid structure, breakpoints, carousel logic, animation timing, DOM semantics, icon SVGs.)

If a value is tempting in two buckets, prefer the **higher** bucket (Global over Editor, Editor over nothing) — but never duplicate it across buckets.

---

## 3. What belongs in the Theme Editor

Merchants **should** control, per section/block:

- **Copy**: headings, subheadings, descriptions, button labels, eyebrow/tagline text.
- **Media**: images (desktop + mobile variants), videos, per-block imagery.
- **Links**: button/CTA URLs, card links, menu selection (`link_list`).
- **Merchandising choices**: `collection` and `product` pickers, "products to show," "which tab maps to which collection."
- **Repeatable content as blocks**: testimonials, value pillars, hero slides, occasion cards, promo cards, reels, highlight items. Each block = one editable unit the merchant can add/remove/reorder.
- **Per-section toggles that are genuinely editorial**: show/hide "View all" button, autoplay on/off, autoplay speed, number of columns.
- **Per-section background choice** — but chosen from a **constrained set** (e.g. a `select` of "white / cream / dark"), *not* a free color picker (see §5).

**Guideline: content the merchant sees on the storefront and might rewrite for a sale, a season, or a new collection belongs in the editor.** In this theme that includes a large amount of copy currently hardcoded in Liquid — see `CODE_VS_EDITOR.md`.

---

## 4. What belongs in Global Settings

These are **design-system tokens** — set once at theme setup, consumed everywhere via CSS variables. Today `settings_schema.json` exposes only: primary font, `max_page_width`, `min_page_margin`, five colors, and `input_corner_radius`. That is far too thin for a theme this large, which is *why* every section re-hardcodes its own values. Promote these to global:

- **Brand color palette** — primary, accent/gold, secondary background, foreground, plus a small set of surface/border tokens. (Currently *five* colors globally, but sections invent 3+ competing green/gold palettes locally — see `GLOBAL_SETTINGS_GUIDE.md`.)
- **Typography** — heading font **and** body font (only primary font is global today; the four Google Fonts are hardcoded in `layout/theme.liquid`).
- **Button system** — background, text, hover colors, radius. (Currently redefined in every section.)
- **Spacing rhythm** — section vertical padding scale, container `max-width` (sections hardcode `1600px` / `1400px` / `80rem` independently).
- **Brand identity** — store name, logo, tagline, founding year, contact phone/email/address, social links. (Currently duplicated and *contradictory*: "since 1985" in footer vs "SINCE 1997" in header.)

**Guideline: if changing a value in one place should logically change it everywhere, it is a global token, not a per-section setting.**

---

## 5. What belongs in Code (and should NOT be exposed)

Keep these hardcoded — exposing them adds complexity or invites breakage:

- **Layout & structure**: grid column counts, bento/mosaic arrangements, flex direction, the DOM shape of a card. A merchant picking "5 columns" on a layout designed for 4 breaks it.
- **Breakpoints & responsive behavior**: mobile/desktop thresholds, which image variant shows when.
- **Interaction logic**: carousel/coverflow math, drag/touch handling, autoplay engines, accordion toggles, variant-selection logic, AJAX cart calls. This is behavior, not content.
- **Animation & easing**: transition durations, `cubic-bezier` curves, Ken Burns effects.
- **Icon SVGs**: ship a **curated named set** (a `select` of "phone / whatsapp / video") — never a raw-SVG textarea. (`made-for-every-bond` currently accepts raw `custom_icon_svg` and outputs it unescaped — a code/security smell, not a merchant feature.)
- **Design-token *application***: the CSS that consumes `var(--color-accent)` lives in code; only the *value* of the token is a setting.
- **Per-property micro-settings**: do not expose "title font size desktop / mobile / weight" as three sliders per block (as `latest-collections` does). Encode a typographic scale in code; expose at most a "size: small/medium/large" `select`.

**Guideline: if a wrong value would break the page or dilute the brand, and getting it right needs design judgment, it stays in code.**

---

## 6. Anti-patterns to stop repeating

These are present in the current theme and each one blurs the Editor/Code line the wrong way:

1. **Hardcoded copy that should be editable.** Product trust badges, shipping/returns text, "SHOP NOW", "Subscribe", newsletter success message — all baked into Liquid where no merchant can reach them. → Move to **Editor** (or Global for cross-page copy).
2. **Design tokens duplicated inline instead of referenced.** Every section hardcodes `#013F3E` / `#D4AF37` / `Montserrat` rather than consuming the global CSS vars that already exist in `snippets/css-variables.liquid`. → Consume **Global**.
3. **Free color pickers per block.** `latest-collections`, `made-for-every-bond`, etc. expose `bg_color`/`text_color`/`accent_color` per section, which is how the palette fragmented into three variants. → Replace with a constrained **Editor** `select` bound to **Global** tokens.
4. **Dead / mislabeled settings.** `header` ships `logo_image`, `gold_price`, "Mock Wishlist Count", "Use mock cart count of 3" — settings the markup ignores. These confuse merchants and rot. → Remove from **Code**, or wire them up.
5. **Mock data as defaults.** Fake testimonials (Arjun/Priya/Rohan), fake reels view counts, fake best-seller catalog, `123 Mock Address Lane`, `whatsapp-request@placeholder.com`. Defaults should be *empty or neutral*, so unset content is obviously unset — not convincingly fake. → **Code** (change defaults) / **Editor** (real content).
6. **Over-granular settings.** Three font-controls per card block. → Collapse into a coded scale.

---

## 7. Recommendations (with full rationale)

### R1 — Adopt the three-bucket model as an explicit, documented rule
- **Recommendation**: Treat "Editor / Global / Code" as a hard architectural boundary and route every current and future setting through the §2 decision test.
- **Why it matters**: The theme's central problem is not too few features — it is that configuration landed in the wrong bucket (content locked in code, tokens scattered per-section). A shared rule stops the drift.
- **Benefits**: Predictable place for everything; faster onboarding; fewer "why can't I edit this?" merchant tickets; consistent brand.
- **Trade-offs**: Requires an upfront pass to reclassify existing settings; some short-term churn in schema files.
- **Difficulty**: Low to adopt (it's a rule); Medium to retrofit existing sections.
- **Long-term impact**: High — every future section is built right the first time.
- **Home**: Process/Code (the rule governs all three buckets).

### R2 — Constrain merchant styling to `select`-from-tokens, not free pickers
- **Recommendation**: Replace per-section free color/font/size pickers with `select` inputs whose values map to global CSS variables (e.g. background: `white | cream | dark`).
- **Why it matters**: Free pickers are exactly how one brand fractured into `#013F3E`/`#0a2a26`/`#0b2e27` greens and `#D4AF37`/`#b38245`/`#c5a47e` golds.
- **Benefits**: Merchants still get flexibility, but only *on-brand* options; palette can be re-tuned globally later.
- **Trade-offs**: Slightly less freedom for the merchant; needs the global token layer to exist first (R1 in `GLOBAL_SETTINGS_GUIDE.md`).
- **Difficulty**: Medium.
- **Long-term impact**: High — brand consistency becomes structural, not disciplinary.
- **Home**: Editor (the `select`) bound to Global (the values).

### R3 — Promote hardcoded storefront copy into editor/global, delete mock defaults
- **Recommendation**: Every user-facing string currently in `.liquid` markup (see `CODE_VS_EDITOR.md`) becomes either a section setting (page-specific) or a global/locale string (cross-page); all fake defaults become empty/neutral.
- **Why it matters**: Merchants can't run promotions or fix copy without a developer today, and fake data risks shipping live (fake reviews, fake stock claims, placeholder contact info).
- **Benefits**: Merchant autonomy; no accidental fake-data launches; unlocks localization.
- **Trade-offs**: Larger schemas; a content-migration pass.
- **Difficulty**: Medium (mechanical but broad).
- **Long-term impact**: High.
- **Home**: Editor + Global.

### R4 — Keep behavior, structure, and animation in code — resist the urge to expose them
- **Recommendation**: Do **not** add settings for grid structure, breakpoints, carousel timing, or DOM shape. Document them as intentionally coded.
- **Why it matters**: The temptation with a big theme is "make it all configurable." That is what turns a theme unmaintainable.
- **Benefits**: Stable layouts; smaller schemas; merchants can't break responsive behavior.
- **Trade-offs**: Layout changes require a developer (correct trade-off for a premium theme).
- **Difficulty**: Low (it's mostly *not* doing something).
- **Long-term impact**: High — protects the design system.
- **Home**: Code.

---

See `CODE_VS_EDITOR.md` for the per-section verdicts that apply these rules.
