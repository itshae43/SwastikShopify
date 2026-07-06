# Swastik Jewels — Go-Live Guide

A complete, step-by-step guide to fill your theme with **real** products and launch. Everything here matches *your* theme's actual sections and settings.

> **Two kinds of work:**
> - **In code (already done for you):** I removed all the fake/mock products, reviews, prices and placeholder data, and rewired **Add to Cart / Buy Now / Wishlist** to use Shopify's **real cart**. See the last section, "What I changed in the code."
> - **In your Shopify Admin (your job — this guide):** upload products, create collections, connect them to the homepage, turn on filters, and fill in product details. I can't do these from the theme files — they live in your store's admin.

Work top to bottom. Budget ~1–2 hours the first time.

---

## 0. Before you start

1. Log into **Shopify Admin** → `https://admin.shopify.com`.
2. Keep two tabs open: **Admin** and your **theme preview** (Online Store → Themes → your theme → **Customize** / **Preview**).
3. This theme prices in **₹ (INR)** — make sure your store currency is set: **Settings → General → Store currency = Indian Rupee (INR)**.

---

## 1. Upload your content (products & images)

This is the foundation — nothing shows on the homepage until products exist.

### 1a. Add products
**Admin → Products → Add product.** For each piece of jewellery fill in:

| Field | What to put | Why it matters |
|-------|-------------|----------------|
| **Title** | e.g. "Golden Teardrop Pendant" | Shows on cards, product page, cart |
| **Description** | Full description | Shows in the "Product Details" accordion on the product page |
| **Media (images)** | 1–5 real photos | First image = card image; all images show in the product page gallery |
| **Price** | e.g. 24999 | Shows everywhere (no more fake prices) |
| **Compare-at price** | Only if on sale (e.g. 31999) | Triggers the "X% OFF" badge automatically. **Leave blank if not on sale** — no fake discount will show |
| **Inventory → Track quantity** | On, set a quantity | Powers the real "In stock / Sold out" state |
| **Status** | **Active** | Draft products don't appear on the storefront |

> **Tip — bulk upload:** You already have CSV files in the project (`demo_products.csv`, etc.). To import: **Admin → Products → Import → Add file**. Review the preview before confirming. Make sure image URLs in the CSV are public, or add images manually after import.

### 1b. Add variants (sizes, metals, lengths)
If a product comes in options (e.g. 16"/18"/20" chain, or Yellow/Rose/White gold):
- On the product page in Admin, scroll to **Variants → + Add options like size or color**.
- Add the option name (e.g. "Chain Length") and values.
- The product page will automatically show these as selectable pills. (The old fake "METAL / CHAIN LENGTH" pills are gone — only your real options appear now.)

---

## 2. Create collections (and use your custom collection pages)

Collections are groups of products. Your theme has **three special collection page designs already built**, which activate automatically **if you name the collection handle exactly right**.

### 2a. Create a collection
**Admin → Products → Collections → Create collection.**
- **Title**: e.g. "Gold Jewellery"
- **Collection type**:
  - **Automated** (recommended): set a condition like *Product tag is equal to `gold`*, and every tagged product joins automatically.
  - **Manual**: you pick products by hand.

### 2b. Use the special designs — set the handle
Scroll down to **Search engine listing → Edit** on the collection, and set the **URL handle** to one of these to get the matching custom banner design:

| Collection handle | Gets this special design |
|-------------------|--------------------------|
| `gold-jewellery` | "GOLD JEWELLERY" gold banner |
| `natural-diamonds` | "NATURAL DIAMONDS" banner |
| `lab-grown` | "LAB GROWN DIAMONDS" banner |

Any **other** collection still works — it just uses the default collection design. Create as many as you like (e.g. `rings`, `earrings`, `pendants`, `bangles`, `necklaces`, `bridal`).

> **Recommended starter set:** `gold-jewellery`, `natural-diamonds`, `lab-grown`, plus category collections `rings`, `earrings`, `pendants`, `bangles`, `necklaces`. Your header menu and homepage will link to these.

---

## 3. Connect collections to the homepage cards

Open **Online Store → Themes → Customize**. On the **Home page** you'll see the sections. Because the fake data is gone, empty sections now show a small grey note **in the editor only** (never to customers) telling you what to set. Fill each one:

| Homepage section | What to set in the editor | Result |
|------------------|---------------------------|--------|
| **New Arrivals** | Section settings → **Collection** → pick a collection | Shows up to 8 real products in the carousel |
| **Best Sellers** | Add a **Tab** block for each category → set the tab **Title** and **Collection** | Each tab shows 4 real products |
| **Featured Collection** | Section settings → **Collection** | Product grid from that collection |
| **Gold Collection Showcase** | Add **Collection Item** blocks → pick a **Collection** in each (optionally a custom title/image) | The circular collection tiles |
| **Featured Categories** | Add **Category** blocks → set **Title**, **Image**, **Link** (to a collection) | Category pills |
| **Discover Grid** | Edit each **Card** block → set **Image (Desktop)**, **Image (Mobile)**, **Link** | The 4-card bento grid |
| **Latest Collections** | Edit each **Collection Card** block → set **Image**, **Title**, **Link** | The 3 staggered cards |

**How to link a card to a collection:** in a block's **Link** field, click it and pick the collection from the list, or paste the URL `/collections/your-handle` (e.g. `/collections/gold-jewellery`).

Then **Save** (top right).

### Header & footer menus
- **Admin → Online Store → Navigation → Main menu**: add links to your collections/pages. In the theme, open the **Header** section and set **Menu** = your Main menu.
- Footer: open the **Footer** section → set **Quick Links Menu** and **Customer Care Menu** to menus you create in Navigation.

---

## 4. Turn on collection filters (Filters sidebar)

Your collection pages already have the **filter sidebar + price slider** built in — they just need Shopify's filter data turned on.

1. Install the free **Shopify Search & Discovery** app: **Admin → Apps → Shopify App Store → search "Search & Discovery" → Install**.
2. Open the app → **Filters** tab.
3. **Add filters** you want shoppers to use, for example:
   - **Availability** (In stock)
   - **Price** (powers the ₹ price slider)
   - **Product type**, **Vendor**
   - Any **variant option** (e.g. Metal, Size) or **tag** / **metafield**
4. Save. Visit any collection page — the **FILTERS** sidebar and price slider now work automatically.

> Filters read from your products, so tag and categorise products well (Type, Vendor, tags). The more structured your product data, the better the filters.

---

## 5. The product page

Your product page (`sections/product.liquid`) now shows **only real data**. Here's how to make each part correct:

| Part of the page | Where it comes from | Your action |
|------------------|--------------------|-------------|
| Title, price, images, gallery | The product itself | Fill these in step 1 |
| **"X% OFF" badge** | Auto-calculated from **Compare-at price** | Only set a compare-at price for real sales |
| **In Stock / Sold Out** | Product inventory | Track inventory; sold-out disables Add to Cart automatically |
| Variant option pills | Product variants | Add variants (step 1b) |
| Description (in accordion) | Product **Description** | Write a good description |
| **Specifications table** | **Product metafields** (see below) | Add metafields to show a specs table |
| Shipping & Care accordions | Fixed store policy text in the theme | These are generic and true for your store; edit in `sections/product.liquid` if needed |
| Trust badges (BIS Hallmarked, etc.) | Fixed in the theme | Keep only if true for your store |

### 5a. Add a real Specifications table (metafields)
The fake specs (3.45g, SI-IJ colour, etc.) are gone. To show a real specs table **per product**, create these metafield definitions once, then fill them per product:

1. **Admin → Settings → Custom data → Products → Add definition.** Create these four (Namespace and key must match exactly):

   | Name | Namespace and key | Type |
   |------|-------------------|------|
   | Gold Purity | `custom.gold_purity` | Single line text |
   | Approx Gold Weight | `custom.gold_weight` | Single line text |
   | Diamond Color & Clarity | `custom.diamond_clarity` | Single line text |
   | Hallmarking Center | `custom.hallmarking_center` | Single line text |

2. On each product page in Admin, scroll to **Metafields** and fill in whichever apply (e.g. Gold Purity = "22K Yellow Gold (BIS Certified)").
3. The specs table on the product page shows **only the rows you filled in.** If you fill none, the table simply doesn't appear — no fake data.

### 5b. Reviews (optional)
The fake "128 reviews / 5 stars" was removed. To show real reviews, install a reviews app (**Shopify Product Reviews**, **Judge.me**, or **Loox**) and add its widget. There's a comment marker in `sections/product.liquid` showing where the rating block used to be.

---

## 6. Cart, Wishlist (Like) & Buy Now — how they work now

I rewired these to the **real Shopify cart** so what the customer sees always matches checkout. Here's the behaviour and how to test:

### Add to Cart
- Clicking **Add to Cart** (on a card or the product page) adds the real product to Shopify's cart, the cart **drawer** slides open showing the real items and subtotal, and the header **cart count** updates.
- If an item is **sold out** or a variant isn't chosen, the customer now sees the **real reason** in a toast — it will **not** silently pretend to add (the old behaviour faked success even on failure).

### Buy It Now
- On the product page, **Buy It Now** adds the item to the real cart and sends the customer **straight to checkout** (`/checkout`).
- Sold-out products have this button disabled.

### Wishlist (the heart / "Like")
- The heart saves items to a **wishlist stored in the shopper's browser** (per device) and opens the wishlist drawer. This is intentional (you chose "wishlist stays in the browser") — it needs no login and works instantly.
- **Note:** a browser wishlist is per-device and clears if the shopper clears their browser data. If later you want wishlists that follow a customer across devices, that needs a wishlist **app** (e.g. Wishlist Plus) or customer-account storage — tell me and I can wire it.

### How to test before launch (do this!)
1. Preview the store, open a product, click **Add to Cart** → the drawer should show the correct item, image, and price, and the header count should go up by 1.
2. Change quantity and **Remove** in the drawer → totals update.
3. Click **Checkout** → you land on Shopify's checkout with the same items and total.
4. Set a product to **0 inventory** → its page shows **Sold Out** and Add to Cart is disabled.
5. Click a **heart** → item appears in the wishlist drawer; refresh the page → it's still there.

---

## 7. The checkout page — which page do you use?

**You don't build or design a checkout page in this theme — Shopify hosts it for you.** This is normal and correct for every Shopify store.

- The **cart drawer** and the **cart page** (`/cart`) are part of your theme. The **Checkout** button sends customers to Shopify's **secure hosted checkout** at `/checkout`.
- **Do not** try to make a custom checkout section — Shopify does not allow editing checkout in normal (non-Plus) themes, and you don't need to.

**What you *should* configure for checkout (in Admin, not the theme):**
1. **Settings → Checkout** — customer contact method, whether accounts are required, tipping, marketing consent, and **checkout branding** (logo, colours, fonts) via **Customize**.
2. **Settings → Payments** — connect **Shopify Payments** / **Razorpay** / **UPI** / cards so customers can actually pay. **Without a payment provider, checkout won't complete.**
3. **Settings → Shipping and delivery** — set your shipping zones/rates (or free shipping) for India.
4. **Settings → Taxes and duties** — configure GST as needed.

**Cart page vs cart drawer:** your theme uses the slide-out **cart drawer** as the main cart. The full `/cart` page (`templates/cart.json`) still exists as a fallback (the "View Cart" link). It's plain but functional — fine to leave as-is for launch.

---

## 8. Final pre-launch checklist

- [ ] Products added, **Active**, with images and prices
- [ ] Collections created; `gold-jewellery` / `natural-diamonds` / `lab-grown` handles set for the special pages
- [ ] Every homepage section has a collection/blocks assigned (no grey "select a collection" notes left in the editor)
- [ ] Header **Menu** and footer menus set from **Navigation**
- [ ] **Search & Discovery** app installed and filters added
- [ ] Product **metafields** created and filled for specs (optional but recommended)
- [ ] **Payments** connected, **Shipping** and **Taxes** configured
- [ ] Tested Add to Cart → Drawer → Checkout end to end with a real test order
- [ ] Contact details correct: **WhatsApp Widget** number, **Footer** phone/email/address, **Contact** page
- [ ] Remove leftover demo pages if unused: in the editor, the `Hello Page 1/2/3` templates (`index.page-1/2/3`) are dev leftovers — you can ignore or delete them
- [ ] When ready: **Online Store → Themes → your theme → Publish**

---

## What I changed in the code (summary)

So you know exactly what's different from before:

**Real Shopify cart (no more "mock" cart):**
- `snippets/theme-ajax-sync.liquid` — Add to Cart now posts to Shopify's `/cart/add.js`, re-reads the real cart, and updates the badge from the true item count. It **no longer fakes success when the add fails**, and no longer guesses prices by scraping the page.
- `sections/cart-drawer.liquid` — the drawer now shows **only the real Shopify cart**. The old localStorage "mock cart" fallback (which could show items that weren't really in your cart) was removed.

**Removed fake/mock content:**
- `snippets/product-card.liquid` — removed fake fallbacks (fake handle, price ₹24,999, variant `998877`); cards now render only real product data.
- `sections/new-arrivals.liquid`, `sections/best-sellers.liquid`, `sections/featured-collection.liquid`, `sections/featured-categories.liquid` — removed the hardcoded fake products/categories. When a collection isn't set yet, they show **nothing to customers** and a small helper note **only in the theme editor**.
- `snippets/best-sellers-fallback-grid.liquid` — **deleted** (this was a whole fake product catalogue with invented "BIS Hallmarked" claims).
- `sections/product.liquid` — removed the fake "23% OFF" badge (now auto-calculated from a real Compare-at price), the fake "(128 reviews)" and 5-star rating, the fake "METAL/CHAIN LENGTH" pills (now shows only your real variants), and the fake spec values (now driven by product metafields). Added real **In Stock / Sold Out** state that disables the buttons when unavailable.

**Left as-is (safe):** the wishlist stays browser-based per your choice; the shipping/care/trust text on the product page is generic store policy you can edit; `snippets/sidebar-drawer.liquid` is an old unused drawer (not shown anywhere) — safe to ignore or delete later.

---

### Need help with the next step?
Tell me if you want me to: wire cross-device wishlists via an app, promote your brand colours/contact info into global settings (see the audit docs in the project root), or set up the header mega-menu. The broader improvement roadmap is in `TOP_IMPROVEMENTS.md` at the project root.
