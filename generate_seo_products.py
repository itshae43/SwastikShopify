import csv

seo_products = [
    {
        'title': '18K White Gold Solitaire Diamond Engagement Ring for Women',
        'type': 'Rings',
        'sku': 'SJ-RING-001',
        'price': '24999',
        'compare': '32999',
        'desc': 'Elevate your special moment with this handcrafted 18K white gold solitaire engagement ring. Featuring a brilliant 1.00-carat VVS1 clarity round diamond set in a classic four-prong setting, this timeless ring delivers unmatched sparkle and elegance. Certified hallmarked gold and conflict-free diamond.',
        'seo_title': '18K White Gold Solitaire Diamond Engagement Ring | Swastik Jewels',
        'seo_desc': 'Shop our 18K White Gold Solitaire Diamond Engagement Ring featuring 1.00 ct VVS1 round diamond. Hallmarked gold & certified luxury jewelry by Swastik Jewels.'
    },
    {
        'title': '22K Traditional Antique Floral Gold Jhumka Earrings',
        'type': 'Earrings',
        'sku': 'SJ-EAR-002',
        'price': '45999',
        'compare': '55999',
        'desc': 'Celebrate heritage craftsmanship with these 22K antique gold jhumka earrings. Adorned with delicate floral filigree engraving, red gemstone accents, and dangling gold bead drops, these earrings are designed to elevate bridal and festive ensembles.',
        'seo_title': '22K Antique Floral Gold Jhumka Earrings for Weddings | Swastik Jewels',
        'seo_desc': 'Buy 22K Traditional Antique Floral Gold Jhumka Earrings with filigree craftsmanship. 100% BIS hallmarked gold bridal earrings by Swastik Jewels.'
    },
    {
        'title': 'Royal Emerald & Diamond Halo Choker Necklace in 18K Gold',
        'type': 'Necklaces',
        'sku': 'SJ-NECK-003',
        'price': '125999',
        'compare': '145999',
        'desc': 'Make a regal statement with this bridal choker necklace in 18K yellow gold. Styled with deep green oval-cut emeralds encircled by sparkling diamond halos, this statement piece blends royal grandeur with contemporary luxury.',
        'seo_title': 'Royal Emerald & Diamond Choker Necklace 18K Gold | Swastik Jewels',
        'seo_desc': 'Discover the Royal Emerald & Diamond Choker Necklace in 18K Gold. Premium bridal jewelry featuring natural emeralds & certified diamonds.'
    },
    {
        'title': '18K Rose Gold Infinity Diamond Tennis Bracelet',
        'type': 'Bracelets',
        'sku': 'SJ-BRAC-004',
        'price': '38999',
        'compare': '48999',
        'desc': 'Add understated glamour to your wrist with this 18K rose gold infinity tennis bracelet. Featuring interconnected figure-eight infinity links studded with pave-set natural diamonds and a double-safety box clasp.',
        'seo_title': '18K Rose Gold Infinity Diamond Tennis Bracelet | Swastik Jewels',
        'seo_desc': 'Shop the 18K Rose Gold Infinity Diamond Tennis Bracelet. Handcrafted with pave diamonds & infinity link design for daily & evening wear.'
    },
    {
        'title': '22K Gold Traditional Kundan Bangles (Pair of 2)',
        'type': 'Bangles',
        'sku': 'SJ-BANG-005',
        'price': '85999',
        'compare': '95999',
        'desc': 'Handmade by master artisans, this pair of 22K gold Kundan kadas features intricate meenakari (enamel work) on the inside and uncut polki Kundan stones set in antique gold finish. Ideal for weddings and heirloom collections.',
        'seo_title': '22K Gold Traditional Kundan Bangles Set of 2 | Swastik Jewels',
        'seo_desc': 'Buy 22K Gold Kundan Kadas with authentic Meenakari art & Polki stones. BIS hallmarked gold bangles for brides & festive occasions.'
    },
    {
        'title': 'Petite Solitaire Diamond Pendant with 18K Gold Chain',
        'type': 'Pendants',
        'sku': 'SJ-PEND-006',
        'price': '18999',
        'compare': '23999',
        'desc': 'A sleek everyday luxury staple, this floating solitaire diamond pendant boasts a 0.50 ct round brilliant diamond in an 18K yellow gold bezel setting. Comes with an adjustable 18-inch 18K gold chain.',
        'seo_title': 'Petite Solitaire Diamond Pendant 18K Gold Chain | Swastik Jewels',
        'seo_desc': 'Minimalist 0.50 ct Solitaire Diamond Pendant with 18K Gold Chain. Perfect everyday luxury gift for women by Swastik Jewels.'
    },
    {
        'title': '18K Yellow Gold Cushion Cut Ruby & Diamond Halo Ring',
        'type': 'Rings',
        'sku': 'SJ-RING-007',
        'price': '32999',
        'compare': '39999',
        'desc': 'A vibrant cocktail ring featuring a 1.5-carat cushion-cut crimson ruby gemstone surrounded by a sparkling halo of round brilliant diamonds set in high-polish 18K yellow gold.',
        'seo_title': '18K Gold Cushion Cut Ruby & Diamond Ring | Swastik Jewels',
        'seo_desc': 'Shop 18K Yellow Gold Cushion Cut Ruby & Diamond Halo Ring. Certified gemstone & diamond statement jewelry by Swastik Jewels.'
    },
    {
        'title': '22K Gold Modern Diamond Mangalsutra for Women',
        'type': 'Mangalsutra',
        'sku': 'SJ-MAN-008',
        'price': '55999',
        'compare': '65999',
        'desc': 'Blending sacred traditions with modern aesthetics, this 22K gold mangalsutra pairs double-strand black spinels with a contemporary geometric diamond pendant set in hallmarked gold.',
        'seo_title': '22K Gold Modern Diamond Mangalsutra Online | Swastik Jewels',
        'seo_desc': 'Explore Modern 22K Gold Diamond Mangalsutras for everyday wear. Lightweight, certified diamonds & hallmarked gold by Swastik Jewels.'
    },
    {
        'title': '950 Platinum & 18K Gold Dual Tone Mens Signet Ring',
        'type': 'Rings',
        'sku': 'SJ-RING-009',
        'price': '42999',
        'compare': '52999',
        'desc': 'Designed for modern gentlemen, this masculine signet ring features a brushed 950 platinum band enhanced with 18K yellow gold borders and a discreet center diamond accent.',
        'seo_title': '950 Platinum & 18K Gold Mens Signet Ring | Swastik Jewels',
        'seo_desc': 'Buy Mens Platinum & 18K Gold Dual Tone Signet Ring. Premium band ring crafted with 950 platinum & conflict-free diamond by Swastik Jewels.'
    },
    {
        'title': '18K White Gold South Sea Pearl & Diamond Drop Earrings',
        'type': 'Earrings',
        'sku': 'SJ-EAR-010',
        'price': '29999',
        'compare': '37999',
        'desc': 'Exuding timeless grace, these earrings showcase 10mm white South Sea cultured pearls suspended beneath brilliant-cut diamond marquise clusters in 18K white gold.',
        'seo_title': '18K White Gold Pearl & Diamond Drop Earrings | Swastik Jewels',
        'seo_desc': 'Shop South Sea Pearl & Diamond Drop Earrings in 18K White Gold. Elegant dangle earrings for evening wear & weddings by Swastik Jewels.'
    },
    {
        'title': '18K White Gold Channel Set Princess Cut Diamond Hoop Earrings',
        'type': 'Earrings',
        'sku': 'SJ-EAR-011',
        'price': '34999',
        'compare': '42999',
        'desc': 'Versatile huggie hoop earrings featuring channel-set princess-cut diamonds along the front curve. Crafted in solid 18K white gold with a secure snap closure.',
        'seo_title': '18K White Gold Princess Cut Diamond Huggie Hoops | Swastik Jewels',
        'seo_desc': 'Buy 18K White Gold Princess Cut Diamond Hoop Earrings. Channel-set diamond huggies designed for daily elegance by Swastik Jewels.'
    },
    {
        'title': '22K Handcrafted Lakshmi Temple Gold Necklace Set',
        'type': 'Necklaces',
        'sku': 'SJ-NECK-012',
        'price': '145999',
        'compare': '165999',
        'desc': 'Rich South Indian heritage temple jewelry featuring embossed Goddess Lakshmi motifs, rubies, and pearls crafted in pure 22K yellow gold. Complete with matching temple earrings.',
        'seo_title': '22K Handcrafted Lakshmi Temple Gold Necklace Set | Swastik Jewels',
        'seo_desc': 'Authentic 22K Gold Lakshmi Temple Necklace Set with ruby drops & matching earrings. Heritage South Indian bridal jewelry by Swastik Jewels.'
    },
    {
        'title': 'Art Deco Blue Sapphire & Diamond Vintage Cocktail Ring 18K Gold',
        'type': 'Rings',
        'sku': 'SJ-RING-013',
        'price': '49999',
        'compare': '59999',
        'desc': 'Inspired by 1920s vintage glam, this cocktail ring features a deep royal blue oval sapphire framed by baguette and round brilliant diamonds in 18K white gold.',
        'seo_title': 'Blue Sapphire & Diamond Vintage Cocktail Ring 18K | Swastik Jewels',
        'seo_desc': 'Shop Vintage Art Deco Blue Sapphire & Diamond Cocktail Ring in 18K Gold. Certified natural sapphire statement ring by Swastik Jewels.'
    },
    {
        'title': '18K Yellow Gold Solid Cuban Link Mens Bracelet',
        'type': 'Bracelets',
        'sku': 'SJ-BRAC-014',
        'price': '68999',
        'compare': '79999',
        'desc': 'Bold and luxurious, this solid 8mm Cuban link bracelet is forged in 18K yellow gold with a polished finish and diamond-accented custom box lock.',
        'seo_title': '18K Yellow Gold Solid Cuban Link Mens Bracelet | Swastik Jewels',
        'seo_desc': 'Buy 18K Yellow Gold Solid Cuban Link Mens Bracelet. Heavy chain link bracelet crafted in hallmarked gold by Swastik Jewels.'
    },
    {
        'title': 'Three-Stone Diamond Past Present Future Anniversary Ring 18K Gold',
        'type': 'Rings',
        'sku': 'SJ-RING-015',
        'price': '39999',
        'compare': '49999',
        'desc': 'Celebrate your journey with three matched round brilliant diamonds symbolizing your past, present, and future. Set in classic 18K white gold basket settings.',
        'seo_title': 'Three-Stone Diamond Past Present Future Ring 18K | Swastik Jewels',
        'seo_desc': 'Shop 18K White Gold Three-Stone Diamond Anniversary Ring. Meaningful trilogy ring featuring certified VVS diamonds by Swastik Jewels.'
    },
    {
        'title': '22K Gold Floral Kundan Maang Tikka with Pearl Drops',
        'type': 'Tikka',
        'sku': 'SJ-TIK-016',
        'price': '19999',
        'compare': '24999',
        'desc': 'Frame your forehead with bridal splendor using this 22K gold maang tikka. Handcrafted with Kundan stone setting, floral detailing, and seed pearl clusters.',
        'seo_title': '22K Gold Floral Kundan Maang Tikka for Brides | Swastik Jewels',
        'seo_desc': 'Buy 22K Gold Kundan Maang Tikka with Pearl Drops. Handcrafted Indian bridal forehead headpiece by Swastik Jewels.'
    },
    {
        'title': '18K Rose Gold Oval Cut Diamond Halo Engagement Ring',
        'type': 'Rings',
        'sku': 'SJ-RING-017',
        'price': '27999',
        'compare': '34999',
        'desc': 'Featuring an elongated oval-cut center diamond surrounded by a delicate pave halo and slim micro-pave diamond band in romantic 18K rose gold.',
        'seo_title': '18K Rose Gold Oval Cut Diamond Halo Ring | Swastik Jewels',
        'seo_desc': 'Shop 18K Rose Gold Oval Cut Diamond Halo Engagement Ring. Elongated oval diamond ring crafted by Swastik Jewels.'
    },
    {
        'title': '22K Yellow Gold Classic Figaro Chain for Unisex',
        'type': 'Chains',
        'sku': 'SJ-CHN-018',
        'price': '22999',
        'compare': '27999',
        'desc': 'A sturdy and timeless 3:1 pattern Figaro chain in 22K yellow gold. High-shine polish with lobster claw clasp for daily durability and style.',
        'seo_title': '22K Yellow Gold Classic Figaro Chain for Men & Women | Swastik Jewels',
        'seo_desc': 'Buy 22K Yellow Gold Figaro Chain online. Durable 100% BIS hallmarked gold neck chain by Swastik Jewels.'
    },
    {
        'title': '18K White Gold Marquise Diamond Cluster Earrings',
        'type': 'Earrings',
        'sku': 'SJ-EAR-019',
        'price': '31999',
        'compare': '38999',
        'desc': 'Arranged in a breathtaking floral cluster, these stud earrings feature marquise and round brilliant diamonds set in 18K white gold with secure push-backs.',
        'seo_title': '18K White Gold Marquise Diamond Cluster Stud Earrings | Swastik Jewels',
        'seo_desc': 'Shop 18K White Gold Marquise & Round Diamond Cluster Earrings. Flower design diamond studs by Swastik Jewels.'
    },
    {
        'title': '18K Tri-Color Gold Stackable Wave Rings (Set of 3)',
        'type': 'Rings',
        'sku': 'SJ-RING-020',
        'price': '26999',
        'compare': '32999',
        'desc': 'Set of 3 stackable wave bands in 18K yellow, rose, and white gold. Styled with subtle hammered textures and micro-pave diamond accents to wear together or separately.',
        'seo_title': '18K Tri-Color Gold Stackable Wave Rings Set of 3 | Swastik Jewels',
        'seo_desc': 'Buy 18K Tri-Color Gold Stackable Wave Rings (Set of 3). Mix & match yellow, rose & white gold diamond bands by Swastik Jewels.'
    }
]

header = [
    'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Product Category', 'Type',
    'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Variant SKU',
    'Variant Inventory Qty', 'Variant Price', 'Variant Compare At Price',
    'Variant Requires Shipping', 'Variant Taxable', 'SEO Title', 'SEO Description', 'Status'
]

rows = [header]
for item in seo_products:
    handle = item['title'].lower().replace(' ', '-').replace('&', 'and').replace('(', '').replace(')', '').replace('\'', '').replace(':', '')
    body = f"<p>{item['desc']}</p>"
    tags = f"{item['type']}, Gold, Diamond, Jewelry, Swastik, Luxury"
    
    rows.append([
        handle, item['title'], body, 'Swastik Jewels', 'Apparel & Accessories > Jewelry', item['type'],
        tags, 'TRUE', 'Title', 'Default Title', item['sku'],
        '10', item['price'], item['compare'],
        'TRUE', 'TRUE', item['seo_title'], item['seo_desc'], 'active'
    ])

out_path = r'c:\Users\Acer\Dev\swastik-shopify\20_test_products_import.csv'
with open(out_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

out_manual = r'c:\Users\Acer\Dev\swastik-shopify\20_test_products_manual.csv'
with open(out_manual, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print('Updated CSV files successfully generated.')
