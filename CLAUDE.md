# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A **custom Shopify Online Store 2.0 theme** for *Swastik Jewels*, an Indian jewelry retailer (prices in INR / ₹). It is built on top of Shopify's [Skeleton Theme](https://github.com/Shopify/skeleton-theme) base but has been heavily extended with bespoke storefront sections, drawers, and a client-side cart/wishlist layer.

**`AGENTS.md` is the authoritative Liquid/Shopify reference** (directory roles, `{% schema %}` rules, LiquidDoc, the full filter/tag/object catalog, translation & localization standards). Read it before writing Liquid — it starts with a mandatory instruction to call `learn_shopify_api` once when working with Liquid themes. This file only covers what is specific to *this* repo and not derivable from AGENTS.md.

## Commands

There is no build step, package manager, or test suite — Liquid is rendered by Shopify's servers. Development uses the Shopify CLI:

```bash
shopify theme dev      # Local preview with hot reload against a dev store
shopify theme check    # Lint (theme-check, "recommended" ruleset — see .theme-check.yml)
shopify theme push     # Upload theme to the connected store
shopify theme pull     # Download store's current theme state (commits here are often auto-pulls)
```

`.shopifyignore` / `.gitignore` exclude `*.zip`, CSVs, and `.shopify/` from CLI + git operations.

### Product data (CSV import)

`generate_csv.py` / `generate_csv_images.py` synthesize Shopify product-import CSVs (`demo_products*.csv`) with realistic INR jewelry pricing across the three collections (Lab Grown Diamond, Natural Diamond, Gold Jewellery). These are import fixtures for the store admin, **not** part of the theme — run with plain `python generate_csv.py`.

## Architecture & conventions specific to this theme

### Global client-side cart & wishlist (the most important custom system)

`snippets/theme-ajax-sync.liquid` is rendered once in `layout/theme.liquid` and owns **all** add-to-cart, wishlist, and toast behavior globally via event delegation. Key facts:

- Cart and wishlist state are mirrored in **`localStorage`** (`cart_count`, `cart_items_data`, `wishlist`, `wishlist_items_data`). Add-to-cart POSTs to `/cart/add.js`, but on failure **falls back to a mock cart** so the UI always advances — badge counts are client-side and can diverge from real Shopify cart state.
- It hooks into DOM by **CSS class and data attributes**, not IDs. Product cards must expose `data-product-id` and `data-url` on the card root, and use the class families `.best-sellers__*`, `.new-arrivals__*`, `.product-single__*`, `.product-card-ui__*`. Renaming these classes silently breaks cart/wishlist/toast wiring.
- Exposes globals other sections call: `window.showSwastikToast(...)`, `window.openCartDrawer()`, `window.openWishlistDrawer()`, `window.updateCartBadge()`, `window.updateWishlistBadge()`.
- Header triggers use classes `.header__cart-trigger` / `.header__wishlist-trigger`; badges are `#cart-count-badge` / `#wishlist-count-badge`.

The three global drawers/widgets — `cart-drawer`, `wishlist-drawer`, `whatsapp-widget` — are rendered as sections at the bottom of `theme.liquid`, not in templates.

### Sections

The storefront is composed of many custom full-width sections (`sections/*.liquid`) — hero-banner, best-sellers, new-arrivals, gold-collection-showcase, shop-by-occasion, for-every-you, made-for-every-bond, etc. Conventions:

- **BEM class naming** scoped to the section: `.section-name__element--modifier` (e.g. `.best-sellers__card-title`). CSS/JS live inline in the section via `{% stylesheet %}` / `{% javascript %}`.
- The homepage has **four variants**: `templates/index.json` plus `index.page-1/2/3.json` (alternate landing layouts). Custom collection templates exist per collection: `collection.gold-jewellery.json`, `collection.lab-grown.json`, `collection.natural-diamonds.json`.

### Product cards

Render via `{% render 'product-card', product: product, class_prefix: '...', badge_text: '...' %}`. The `class_prefix` param (default `best-sellers`) drives the BEM prefix so the same markup adapts to different sections. Prices are localized to rupees with `{{ price | money | replace: '$', '₹' | replace: ' Rs.', '₹' }}` — follow this pattern for any new price output. The card's per-component CSS is the static asset `assets/component-product-card.css`.

### Head / assets

`layout/theme.liquid` inlines `snippets/css-variables.liquid`, preloads `assets/critical.css`, and loads Google Fonts directly (Cormorant Garamond, Playfair Display, Montserrat, Inter — `serif-font` class maps to the display serif). It also injects CSS/JS to hide Shopify's hCaptcha badge and third-party chat widgets so they don't collide with the custom WhatsApp widget — preserve this when editing the head.

### Scratch files (ignore)

Root-level `scratch*.js`, `scratch*.txt`, `scratch*.py`, `sample_products.csv`, `swastik-jewels-products.csv`, and the `*.zip` archives are experiment/backup artifacts (several are UTF-16). They are not wired into the theme — don't treat them as source.
