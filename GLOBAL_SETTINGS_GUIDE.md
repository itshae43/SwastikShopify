# Global Settings Guide — Swastik Jewels

> What lives in `config/settings_schema.json` today, what *should*, and why the current thinness is the root cause of the theme's inconsistency.
> Read-only analysis — no code changes.

---

## 1. What "Global Settings" are for

Global settings are the **design system's control panel**: a small set of tokens the merchant sets **once at setup**, consumed **everywhere** through CSS variables (`snippets/css-variables.liquid` → `:root`). They are not content and not per-section — they are the values that must stay identical across the whole store for it to feel like one brand.

The test (from `THEME_EDITOR_GUIDELINES.md` §2): **"If changing this in one place should change it everywhere, it is global."**

---

## 2. Current state

`config/settings_schema.json` exposes only:

| Group | Setting | Type | Notes |
|-------|---------|------|-------|
| Typography | `type_primary_font` | font_picker | **Only one font.** No body/heading split. |
| Layout | `max_page_width` | select (90rem / 110rem) | OK |
| Layout | `min_page_margin` | range | OK |
| Colors | `color_primary` | color (#013F3E) | |
| Colors | `color_accent` | color (#D4AF37) | |
| Colors | `background_color` | color (#FFFFFF) | |
| Colors | `color_secondary_bg` | color (#FDFBF7) | |
| Colors | `foreground_color` | color (#1A1A1A) | |
| Colors | `input_corner_radius` | range | |

Plus one orphan: `settings_data.json` carries `checkout_logo_image: "logo.png"` and the WhatsApp number `8920905268`, but **`checkout_logo_image` is not defined in `settings_schema.json`** — a stranded value with no editor UI.

**`snippets/css-variables.liquid` correctly turns these into `--color-primary`, `--color-accent`, `--color-background`, `--color-secondary-bg`, `--color-foreground`.** The token layer exists. The problem is that **almost no section consumes it** — they hardcode the same hex values (often *wrong* variants) inline instead.

---

## 3. The root-cause finding

> The global settings are too thin, so every section reinvents them locally — and they drifted.

Concrete evidence of the drift this caused:

- **Three "brand green" values**: `#013F3E` (global) vs `#0a2a26` vs `#0b2e27`.
- **Three "brand gold" values**: `#D4AF37` (global) vs `#b38245` vs `#c5a47e`, plus `#d8c3b1`/`#9a7d65` in instagram-reels.
- **Fonts**: `type_primary_font` is the only global font, yet `layout/theme.liquid` **hardcodes four Google Fonts** (Cormorant Garamond, Inter, Montserrat, Playfair Display), and sections variously hardcode Montserrat, `Inter`+`Merriweather` (collection grid), or `Playfair`+`Inter` (for-every-you).
- **Container width**: hardcoded as `1600px`, `1400px`, and `80rem` in different sections — no global.
- **Buttons**: background/text/hover colors + radius redefined in nearly every section.
- **Brand contact/identity**: store name, phone, email, address, WhatsApp, founding year duplicated across header/footer/contact/whatsapp — and now **contradict each other** (1985 vs 1997; three different phone numbers).

None of these are per-section decisions. They are global tokens that were never given a global home, so they fragmented.

---

## 4. Recommended global settings model

The following should be **promoted to Global Settings** (or already are and should simply be *consumed*). Each row is justified; the consolidated recommendation with trade-offs follows in §5.

### 4a. Color tokens (expand slightly, then enforce)
Keep the five existing colors and add the surfaces sections currently hardcode:
- `color_primary`, `color_accent`, `background_color`, `color_secondary_bg`, `foreground_color` — **keep**.
- Add: `color_surface` (card backgrounds — sections hardcode `#faf7f2`/`#F8F3ED`/`#fff`), `color_border` (hardcoded `#ebe7df`/`#E8D5C4`), `color_muted_text` (hardcoded `#555555`/`#777`), `color_button_hover` (hardcoded `#012b2a`/`#002E28`/`#025654`).
- **Retire palette B/C** (`#0a2a26`, `#b38245`, `#0b2e27`, `#c5a47e`) — map them onto the primary tokens.

### 4b. Typography (add the missing axis)
- Keep `type_primary_font`; **add `type_heading_font`** (body vs display).
- Decide the Cormorant/Playfair/Montserrat/Inter question **once, globally**, and load fonts from the font settings — not a hardcoded `<link>` in `theme.liquid`.

### 4c. Button system
- `button_bg`, `button_text`, `button_hover_bg`, `button_hover_text`, `button_radius` (or reuse `input_corner_radius`). Sections then consume `--button-*` instead of redefining four button colors each (as `latest-collections` does).

### 4d. Spacing & layout rhythm
- `section_padding_scale` (or discrete `select`: compact/normal/spacious) and a global `container_max_width`. Replaces the ad-hoc `1600/1400/80rem` and per-section `padding_top/bottom` sliders.

### 4e. Brand identity block (new group)
- `brand_name`, `logo` (real logo picker — replaces the stranded `checkout_logo_image` and the ignored header `logo_image`), `brand_tagline`, `founding_year`, `contact_phone`, `contact_email`, `contact_address`, `whatsapp_number`, and social URLs.
- Header, footer, contact page, whatsapp-widget, expert-consultation all **read these** instead of holding their own copies.

---

## 5. Recommendations

### GS1 — Expand the global token set, then make sections consume it
- **Recommendation**: Add surface/border/muted/button color tokens, a heading font, a button group, and spacing/container tokens to `settings_schema.json`; refactor sections to consume the existing + new `--*` variables instead of inline hex.
- **Why it matters**: The token layer already exists (`css-variables.liquid`) but is bypassed, which is precisely why one brand became three palettes and four font stacks.
- **Benefits**: Re-skinning the store becomes a 10-minute settings change; brand consistency is structural; section CSS shrinks dramatically.
- **Trade-offs**: A broad (but mechanical) refactor to replace hardcoded values with `var(--token)`; must pick canonical values where three currently compete.
- **Difficulty**: Medium–High (touches most sections, but low-risk find-and-replace).
- **Long-term impact**: Very High — this is the single highest-leverage structural change.
- **Home**: **Global Settings** (values) + **Code** (consumption).

### GS2 — Create a Brand Identity settings group as the single source of truth
- **Recommendation**: One global group holding name/logo/tagline/year/phone/email/address/WhatsApp/social; all sections reference it.
- **Why it matters**: Contact and identity facts are duplicated and already inconsistent (1985/1997; three phone numbers; two emails); a wrong or half-updated number is a real customer-facing failure.
- **Benefits**: One edit propagates everywhere; impossible to have contradictory brand facts; correct info guaranteed store-wide.
- **Trade-offs**: ~5 sections must be pointed at the globals; merchant sees one more settings group.
- **Difficulty**: Medium.
- **Long-term impact**: High.
- **Home**: **Global Settings**.

### GS3 — Move font loading into the font settings, drop the hardcoded `<link>`
- **Recommendation**: Load fonts via `font_url`/`font_face` from `type_primary_font` + a new `type_heading_font`; remove the four-family Google Fonts `<link>` in `layout/theme.liquid`.
- **Why it matters**: The hardcoded `<link>` bypasses the theme's own font system, adds a render-blocking third-party request, and lets sections drift onto off-brand stacks.
- **Benefits**: Faster first paint (fewer blocking requests, Shopify-CDN fonts); one place controls typography; no off-brand fonts.
- **Trade-offs**: Must reconcile the current 4 display fonts down to a deliberate 1–2; visual QA needed.
- **Difficulty**: Medium.
- **Long-term impact**: High (performance + consistency).
- **Home**: **Global Settings** + **Code**.

### GS4 — Register or remove the stranded `checkout_logo_image`
- **Recommendation**: Either define a proper global `logo` setting (and use it in header + checkout) or remove the orphaned `checkout_logo_image` value.
- **Why it matters**: A value in `settings_data.json` with no schema entry is invisible/uneditable and rots; meanwhile header hardcodes `logo.png` and ignores its own `logo_image` setting.
- **Benefits**: Logo becomes editable in one place; no ghost settings.
- **Trade-offs**: Minor.
- **Difficulty**: Low.
- **Long-term impact**: Medium.
- **Home**: **Global Settings**.

### GS5 — Do NOT globalize genuinely per-section choices
- **Recommendation**: Keep autoplay/speed, which-collection-to-feature, per-section copy, and per-block content in the **Editor**, not Global.
- **Why it matters**: Over-correcting into "everything global" is as bad as the current fragmentation — a merchant should set a hero's autoplay per hero, not store-wide.
- **Benefits**: Preserves legitimate per-section flexibility.
- **Trade-offs**: None — this is a guardrail.
- **Difficulty**: Low.
- **Long-term impact**: Medium.
- **Home**: **Theme Editor** (explicitly *not* Global).

---

## 6. Summary table — target global settings

| Group | Tokens | Status |
|-------|--------|--------|
| Colors | primary, accent, background, secondary-bg, foreground | ✅ exist — **enforce consumption** |
| Colors | surface, border, muted-text, button-hover | ➕ add (currently hardcoded per section) |
| Typography | primary font | ✅ exists |
| Typography | heading font | ➕ add |
| Buttons | bg, text, hover-bg, hover-text, radius | ➕ add (currently per-section) |
| Layout | max_page_width, page_margin | ✅ exist |
| Layout | container_max_width, section_padding_scale | ➕ add (currently `1600/1400/80rem` ad-hoc) |
| Brand identity | name, logo, tagline, year, phone, email, address, whatsapp, social | ➕ add (currently duplicated & contradictory) |
