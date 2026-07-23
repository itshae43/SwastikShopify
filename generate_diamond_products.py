import csv

diamond_products = [
    # --- RINGS (5 Products) ---
    {
        'title': 'Lab Grown Solitaire Diamond Engagement Ring in 18K White Gold',
        'type': 'Rings',
        'sku': 'SJ-DIA-RNG-001',
        'price': '34999',
        'compare': '42999',
        'tags': 'Lab Grown Diamonds, Rings, Everyday Sparkle, Gifts for Her, Diamond, Swastik, Luxury',
        'desc': 'Handcrafted 18K white gold solitaire ring featuring a 1.00 ct VVS1 round lab-grown diamond in a classic 4-prong setting. IGI certified with brilliant sparkle.',
        'seo_title': 'Lab Grown Solitaire Diamond Ring 18K White Gold | Swastik Jewels',
        'seo_desc': 'Buy Lab Grown Solitaire Diamond Engagement Ring in 18K White Gold. Certified 1.00 ct VVS1 round diamond ring by Swastik Jewels.'
    },
    {
        'title': 'Natural Oval Cut Diamond Halo Ring in 18K Yellow Gold',
        'type': 'Rings',
        'sku': 'SJ-DIA-RNG-002',
        'price': '58999',
        'compare': '69999',
        'tags': 'Natural Diamonds, Rings, Party Wear, For Brides, Diamond, Swastik, Luxury',
        'desc': 'Features a stunning 1.20 ct natural oval diamond framed by a delicate micro-pave diamond halo set in high-polish 18K yellow gold.',
        'seo_title': 'Natural Oval Cut Diamond Halo Ring 18K Gold | Swastik Jewels',
        'seo_desc': 'Shop Natural Oval Cut Diamond Halo Ring in 18K Yellow Gold. Certified natural diamonds & exquisite craftsmanship by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Princess Cut Diamond Eternity Band Ring',
        'type': 'Rings',
        'sku': 'SJ-DIA-RNG-003',
        'price': '29999',
        'compare': '36999',
        'tags': 'Lab Grown Diamonds, Rings, Daily Wear, Eternal Promises, Diamond, Swastik, Luxury',
        'desc': 'Continuous channel-set princess cut lab-grown diamonds running around an 18K white gold band. Sleek, comfortable, and brilliant.',
        'seo_title': 'Lab Grown Princess Cut Diamond Eternity Band | Swastik Jewels',
        'seo_desc': 'Buy Lab Grown Princess Cut Diamond Eternity Band Ring in 18K White Gold. Perfect anniversary & wedding ring by Swastik Jewels.'
    },
    {
        'title': 'Natural Three-Stone Diamond Anniversary Ring in 18K Rose Gold',
        'type': 'Rings',
        'sku': 'SJ-DIA-RNG-004',
        'price': '44999',
        'compare': '54999',
        'tags': 'Natural Diamonds, Rings, Forever Classics, Eternal Promises, Diamond, Swastik, Luxury',
        'desc': 'Symbolizing past, present, and future with three matched brilliant-cut natural diamonds set in romantic 18K rose gold.',
        'seo_title': 'Natural Three-Stone Diamond Ring 18K Rose Gold | Swastik Jewels',
        'seo_desc': 'Shop Natural Three-Stone Diamond Anniversary Ring in 18K Rose Gold. Certified VVS natural diamond trilogy ring by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Cushion Cut Diamond Cocktail Statement Ring',
        'type': 'Rings',
        'sku': 'SJ-DIA-RNG-005',
        'price': '39999',
        'compare': '48999',
        'tags': 'Lab Grown Diamonds, Rings, Party Wear, Everyday Sparkle, Diamond, Swastik, Luxury',
        'desc': 'A showstopping 1.50 ct cushion cut lab-grown diamond encased in a split-shank pave diamond band forged in 18K yellow gold.',
        'seo_title': 'Lab Grown Cushion Cut Diamond Cocktail Ring | Swastik Jewels',
        'seo_desc': 'Buy Lab Grown Cushion Cut Diamond Cocktail Statement Ring in 18K Gold. Certified lab grown diamond jewelry by Swastik Jewels.'
    },

    # --- EARRINGS (5 Products) ---
    {
        'title': 'Natural Solitaire Diamond Stud Earrings (1.50 ct VVS1) in 18K Gold',
        'type': 'Earrings',
        'sku': 'SJ-DIA-EAR-006',
        'price': '49999',
        'compare': '59999',
        'tags': 'Natural Diamonds, Earrings, Daily Wear, Forever Classics, Diamond, Swastik, Luxury',
        'desc': 'Timeless stud earrings featuring two matched 0.75 ct natural round brilliant diamonds (1.50 ct tw) set in 18K yellow gold basket settings.',
        'seo_title': 'Natural Solitaire Diamond Stud Earrings 1.50 ct | Swastik Jewels',
        'seo_desc': 'Shop Natural Solitaire Diamond Stud Earrings in 18K Gold. 1.50 ct tw VVS1 certified diamonds for daily luxury by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Diamond Huggie Hoop Earrings in 18K White Gold',
        'type': 'Earrings',
        'sku': 'SJ-DIA-EAR-007',
        'price': '22999',
        'compare': '27999',
        'tags': 'Lab Grown Diamonds, Earrings, Office Wear, Daily Wear, Diamond, Swastik, Luxury',
        'desc': 'Elegant daily-wear huggie hoops featuring front-facing pave lab-grown diamonds set in solid 18K white gold with snap latch.',
        'seo_title': 'Lab Grown Diamond Huggie Hoop Earrings 18K | Swastik Jewels',
        'seo_desc': 'Buy Lab Grown Diamond Huggie Hoop Earrings in 18K White Gold. Lightweight diamond earrings for office & daily wear by Swastik Jewels.'
    },
    {
        'title': 'Natural Diamond Marquise Cluster Drop Earrings',
        'type': 'Earrings',
        'sku': 'SJ-DIA-EAR-008',
        'price': '62999',
        'compare': '74999',
        'tags': 'Natural Diamonds, Earrings, Festive Wear, Wedding Wear, Diamond, Swastik, Luxury',
        'desc': 'Floral cluster drop earrings featuring marquise and pear cut natural diamonds cascading from brilliant studs in 18K white gold.',
        'seo_title': 'Natural Diamond Marquise Cluster Drop Earrings | Swastik Jewels',
        'seo_desc': 'Shop Natural Diamond Marquise Cluster Drop Earrings. Handcrafted bridal & wedding diamond earrings by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Emerald Cut Diamond Halo Dangle Earrings',
        'type': 'Earrings',
        'sku': 'SJ-DIA-EAR-009',
        'price': '37999',
        'compare': '45999',
        'tags': 'Lab Grown Diamonds, Earrings, Party Wear, Gifts for Her, Diamond, Swastik, Luxury',
        'desc': 'Sophisticated dangle earrings starring emerald-cut lab-grown diamonds enveloped by pave halos in 18K yellow gold.',
        'seo_title': 'Lab Grown Emerald Cut Diamond Halo Earrings | Swastik Jewels',
        'seo_desc': 'Buy Lab Grown Emerald Cut Diamond Halo Dangle Earrings in 18K Gold. Certified lab grown diamond drops by Swastik Jewels.'
    },
    {
        'title': 'Natural Diamond & South Sea Pearl Drop Earrings',
        'type': 'Earrings',
        'sku': 'SJ-DIA-EAR-010',
        'price': '41999',
        'compare': '49999',
        'tags': 'Natural Diamonds, Earrings, For Brides, Wedding Wear, Diamond, Swastik, Luxury',
        'desc': 'Lustrous 10mm white South Sea pearls suspended beneath natural diamond cluster tops in hallmarked 18K white gold.',
        'seo_title': 'Natural Diamond & South Sea Pearl Drop Earrings | Swastik Jewels',
        'seo_desc': 'Shop Natural Diamond & South Sea Pearl Drop Earrings. Elegant wedding & evening drop earrings by Swastik Jewels.'
    },

    # --- NECKLACES (5 Products) ---
    {
        'title': 'Natural Diamond Tennis Choker Necklace in 18K White Gold',
        'type': 'Necklaces',
        'sku': 'SJ-DIA-NCK-011',
        'price': '155999',
        'compare': '179999',
        'tags': 'Natural Diamonds, Necklaces, Wedding Wear, For Brides, Diamond, Swastik, Luxury',
        'desc': 'A continuous strand of 8.00 carats of natural round brilliant diamonds prong-set in 18K white gold with a custom safety clasp.',
        'seo_title': 'Natural Diamond Tennis Choker Necklace 18K White Gold | Swastik Jewels',
        'seo_desc': 'Buy Natural Diamond Tennis Choker Necklace in 18K White Gold. 8.00 ct tw certified natural diamond bridal necklace by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Diamond Floral Layered Necklace',
        'type': 'Necklaces',
        'sku': 'SJ-DIA-NCK-012',
        'price': '48999',
        'compare': '58999',
        'tags': 'Lab Grown Diamonds, Necklaces, Festive Wear, Everyday Sparkle, Diamond, Swastik, Luxury',
        'desc': 'Modern 2-layer gold chain necklace adorned with lab-grown diamond floral pendants set in 18K yellow gold.',
        'seo_title': 'Lab Grown Diamond Floral Layered Necklace 18K | Swastik Jewels',
        'seo_desc': 'Shop Lab Grown Diamond Floral Layered Necklace in 18K Gold. Lightweight, stylish layered diamond necklace by Swastik Jewels.'
    },
    {
        'title': 'Natural Diamond & Blue Sapphire Royal Halo Pendant Necklace',
        'type': 'Necklaces',
        'sku': 'SJ-DIA-NCK-013',
        'price': '52999',
        'compare': '62999',
        'tags': 'Natural Diamonds, Necklaces, Party Wear, Close To Heart, Diamond, Swastik, Luxury',
        'desc': 'Features a deep royal blue oval sapphire encircled by brilliant natural diamond halos, suspended from an 18K white gold chain.',
        'seo_title': 'Natural Diamond & Sapphire Halo Pendant Necklace | Swastik Jewels',
        'seo_desc': 'Buy Natural Diamond & Blue Sapphire Royal Halo Pendant Necklace in 18K Gold. Certified gemstone necklace by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Solitaire Diamond Floating Chain Necklace',
        'type': 'Necklaces',
        'sku': 'SJ-DIA-NCK-014',
        'price': '26999',
        'compare': '32999',
        'tags': 'Lab Grown Diamonds, Necklaces, Daily Wear, Office Wear, Diamond, Swastik, Luxury',
        'desc': 'A minimalist 0.75 ct lab-grown diamond sliding along an ultra-fine 18K gold chain for floating elegance.',
        'seo_title': 'Lab Grown Solitaire Diamond Floating Necklace | Swastik Jewels',
        'seo_desc': 'Shop Lab Grown Solitaire Diamond Floating Chain Necklace in 18K Gold. Perfect everyday luxury pendant necklace by Swastik Jewels.'
    },
    {
        'title': 'Natural Heart Cut Diamond Locket Necklace in 18K Rose Gold',
        'type': 'Necklaces',
        'sku': 'SJ-DIA-NCK-015',
        'price': '38999',
        'compare': '46999',
        'tags': 'Natural Diamonds, Necklaces, Close To Heart, Gifts for Her, Diamond, Swastik, Luxury',
        'desc': 'Romantic heart-shaped pendant featuring a center heart-cut natural diamond accented by pave diamonds in 18K rose gold.',
        'seo_title': 'Natural Heart Cut Diamond Locket Necklace 18K | Swastik Jewels',
        'seo_desc': 'Buy Natural Heart Cut Diamond Locket Necklace in 18K Rose Gold. Romantic gift for her by Swastik Jewels.'
    },

    # --- BRACELETS (5 Products) ---
    {
        'title': 'Natural Diamond Classic Tennis Bracelet in 18K White Gold',
        'type': 'Bracelets',
        'sku': 'SJ-DIA-BRC-016',
        'price': '79999',
        'compare': '92999',
        'tags': 'Natural Diamonds, Bracelets, Forever Classics, Daily Wear, Diamond, Swastik, Luxury',
        'desc': 'Flexible 3.00 ct natural round diamond tennis bracelet crafted in hallmarked 18K white gold with double security clasp.',
        'seo_title': 'Natural Diamond Classic Tennis Bracelet 18K Gold | Swastik Jewels',
        'seo_desc': 'Shop Natural Diamond Classic Tennis Bracelet in 18K White Gold. 3.00 ct tw certified natural diamond bracelet by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Diamond Infinity Link Bangle Bracelet',
        'type': 'Bracelets',
        'sku': 'SJ-DIA-BRC-017',
        'price': '35999',
        'compare': '42999',
        'tags': 'Lab Grown Diamonds, Bracelets, Office Wear, Everyday Sparkle, Diamond, Swastik, Luxury',
        'desc': 'Sleek hinged bangle featuring interlocking infinity symbols lined with pave lab-grown diamonds in 18K yellow gold.',
        'seo_title': 'Lab Grown Diamond Infinity Link Bangle Bracelet | Swastik Jewels',
        'seo_desc': 'Buy Lab Grown Diamond Infinity Link Bangle Bracelet in 18K Gold. Elegant daily wear diamond bracelet by Swastik Jewels.'
    },
    {
        'title': 'Natural Diamond Oval Cut Halo Station Bracelet in 18K Gold',
        'type': 'Bracelets',
        'sku': 'SJ-DIA-BRC-018',
        'price': '46999',
        'compare': '55999',
        'tags': 'Natural Diamonds, Bracelets, Party Wear, Gifts for Her, Diamond, Swastik, Luxury',
        'desc': 'Five oval-cut natural diamond halo stations linked together along a delicate 18K yellow gold chain.',
        'seo_title': 'Natural Diamond Oval Halo Station Bracelet 18K | Swastik Jewels',
        'seo_desc': 'Shop Natural Diamond Oval Cut Halo Station Bracelet in 18K Yellow Gold. Certified natural diamond station bracelet by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Mens Diamond Heavy Cuban Link Bracelet',
        'type': 'Bracelets',
        'sku': 'SJ-DIA-BRC-019',
        'price': '64999',
        'compare': '76999',
        'tags': 'Lab Grown Diamonds, Bracelets, Gifts For Him, Daily Wear, Diamond, Swastik, Luxury',
        'desc': 'Masculine 8mm solid Cuban chain link bracelet in 18K gold featuring a pave lab-grown diamond lock clasp.',
        'seo_title': 'Lab Grown Mens Diamond Cuban Link Bracelet 18K | Swastik Jewels',
        'seo_desc': 'Buy Mens Lab Grown Diamond Cuban Link Bracelet in 18K Gold. Bold heavy chain bracelet for men by Swastik Jewels.'
    },
    {
        'title': 'Natural Diamond Bezel Set Chain Charm Bracelet',
        'type': 'Bracelets',
        'sku': 'SJ-DIA-BRC-020',
        'price': '29999',
        'compare': '35999',
        'tags': 'Natural Diamonds, Bracelets, Close To Heart, Everyday Sparkle, Diamond, Swastik, Luxury',
        'desc': 'Floating bezel-set natural round diamonds scattered along an adjustable 18K rose gold chain bracelet.',
        'seo_title': 'Natural Diamond Bezel Set Chain Charm Bracelet | Swastik Jewels',
        'seo_desc': 'Shop Natural Diamond Bezel Set Chain Charm Bracelet in 18K Rose Gold. Delicate charm bracelet by Swastik Jewels.'
    },

    # --- PENDANTS (5 Products) ---
    {
        'title': 'Natural Solitaire Diamond Bezel Pendant with 18K Chain',
        'type': 'Pendants',
        'sku': 'SJ-DIA-PND-021',
        'price': '23999',
        'compare': '28999',
        'tags': 'Natural Diamonds, Pendants, Daily Wear, Minimalist, Diamond, Swastik, Luxury',
        'desc': 'A sparkling 0.40 ct natural round diamond enclosed in a sleek 18K yellow gold bezel ring, complete with 18-inch gold chain.',
        'seo_title': 'Natural Solitaire Diamond Bezel Pendant 18K Chain | Swastik Jewels',
        'seo_desc': 'Buy Natural Solitaire Diamond Bezel Pendant with 18K Chain. Minimalist certified diamond pendant by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Pear Cut Diamond Halo Pendant in 18K White Gold',
        'type': 'Pendants',
        'sku': 'SJ-DIA-PND-022',
        'price': '31999',
        'compare': '38999',
        'tags': 'Lab Grown Diamonds, Pendants, Office Wear, Gifts for Her, Diamond, Swastik, Luxury',
        'desc': 'Features a graceful 1.00 ct teardrop pear-cut lab-grown diamond wrapped in a micro-pave diamond halo in 18K white gold.',
        'seo_title': 'Lab Grown Pear Cut Diamond Halo Pendant 18K White Gold | Swastik Jewels',
        'seo_desc': 'Shop Lab Grown Pear Cut Diamond Halo Pendant in 18K White Gold. Teardrop lab grown diamond pendant by Swastik Jewels.'
    },
    {
        'title': 'Natural Diamond Evil Eye Protection Charm Pendant',
        'type': 'Pendants',
        'sku': 'SJ-DIA-PND-023',
        'price': '19999',
        'compare': '24999',
        'tags': 'Natural Diamonds, Pendants, Close To Heart, Daily Wear, Diamond, Swastik, Luxury',
        'desc': 'Modern talisman pendant featuring natural diamonds and blue sapphire inlay forming a protective evil eye motif in 18K gold.',
        'seo_title': 'Natural Diamond Evil Eye Protection Charm Pendant | Swastik Jewels',
        'seo_desc': 'Buy Natural Diamond Evil Eye Charm Pendant in 18K Gold. Protective talisman jewelry with certified diamonds by Swastik Jewels.'
    },
    {
        'title': 'Lab Grown Cushion Diamond Cross Pendant in 18K Gold',
        'type': 'Pendants',
        'sku': 'SJ-DIA-PND-024',
        'price': '33999',
        'compare': '40999',
        'tags': 'Lab Grown Diamonds, Pendants, Eternal Promises, Gifts for Her, Diamond, Swastik, Luxury',
        'desc': 'Classic cross pendant handset with cushion and round lab-grown diamonds in high-polish 18K yellow gold.',
        'seo_title': 'Lab Grown Cushion Diamond Cross Pendant 18K Gold | Swastik Jewels',
        'seo_desc': 'Shop Lab Grown Cushion Diamond Cross Pendant in 18K Gold. Timeless religious cross pendant by Swastik Jewels.'
    },
    {
        'title': 'Natural Diamond Floral Cluster Starburst Pendant',
        'type': 'Pendants',
        'sku': 'SJ-DIA-PND-025',
        'price': '36999',
        'compare': '43999',
        'tags': 'Natural Diamonds, Pendants, Party Wear, Festive Wear, Diamond, Swastik, Luxury',
        'desc': 'Radiant starburst pendant composed of marquise and round natural diamonds emitting 360-degree shimmer in 18K white gold.',
        'seo_title': 'Natural Diamond Floral Cluster Starburst Pendant | Swastik Jewels',
        'seo_desc': 'Buy Natural Diamond Floral Cluster Starburst Pendant in 18K White Gold. Certified diamond starburst pendant by Swastik Jewels.'
    }
]

header = [
    'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Product Category', 'Type',
    'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Variant SKU',
    'Variant Inventory Qty', 'Variant Price', 'Variant Compare At Price',
    'Variant Requires Shipping', 'Variant Taxable', 'SEO Title', 'SEO Description', 'Status'
]

rows = [header]
for item in diamond_products:
    handle = item['title'].lower().replace(' ', '-').replace('&', 'and').replace('(', '').replace(')', '').replace('\'', '').replace(':', '').replace('.', '')
    body = f"<p>{item['desc']}</p>"
    
    rows.append([
        handle, item['title'], body, 'Swastik Jewels', 'Apparel & Accessories > Jewelry', item['type'],
        item['tags'], 'TRUE', 'Title', 'Default Title', item['sku'],
        '10', item['price'], item['compare'],
        'TRUE', 'TRUE', item['seo_title'], item['seo_desc'], 'active'
    ])

out_path = r'c:\Users\Acer\Dev\swastik-shopify\diamond_test_products_import.csv'
with open(out_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print('Diamond products CSV generated successfully at:', out_path)
