import csv
import random
import math

categories = {
    "Lab Grown Diamond": ["Ring", "Bracelet", "Gents Ring", "Earring", "Pendant"],
    "Natural Diamond": ["Ring", "Bracelet", "Gents Ring", "Earring", "Pendant", "Necklace", "Pendant Set", "Bangle", "Mangalsutra"],
    "Gold Jewellery": ["Chain", "Ladies Ring", "Pendant Set", "Choker Set", "Bracelet", "Bangle", "Necklace Set", "Chikpatti", "Long Set", "Earring", "Tika"]
}

price_ranges = {
    "Lab Grown Diamond": (15000, 150000),
    "Natural Diamond": (35000, 750000),
    "Gold Jewellery": (25000, 400000)
}

# We add Image Position to the header
header = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", 
    "Tags", "Published", "Option1 Name", "Option1 Value", "Variant SKU", 
    "Variant Inventory Qty", "Variant Price", "Variant Compare At Price", 
    "Image Src", "Image Position"
]

rows = [header]
target_per_main = 1010

for main_cat, subcats in categories.items():
    per_subcat = math.ceil(target_per_main / len(subcats))
    
    for subcat in subcats:
        for i in range(1, per_subcat + 1):
            handle = f"{main_cat.lower().replace(' ', '-')}-{subcat.lower().replace(' ', '-')}-{i:04d}"
            
            # --- ROW 1: Main Product Data & Main Image ---
            title = f"{main_cat} {subcat} Model {i:04d}"
            body = f"<p>Exquisite {main_cat.lower()} {subcat.lower()} designed for elegance and durability.</p>"
            vendor = "Demo Brand"
            prod_cat = "Apparel & Accessories > Jewelry"
            type_val = subcat
            tags = f"{main_cat}, {subcat}, Demo"
            published = "TRUE"
            
            opt1_name = "Title" if subcat not in ["Ring", "Gents Ring", "Ladies Ring", "Bangle"] else "Size"
            if opt1_name == "Size" and subcat == "Bangle":
                opt1_val = str(random.choice(["2.2", "2.4", "2.6", "2.8"]))
            elif opt1_name == "Size":
                opt1_val = str(random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18]))
            else:
                opt1_val = "Default Title"
                
            sku = f"SKU-{main_cat[:2].upper()}-{subcat[:2].upper()}-{i:04d}"
            qty = random.randint(1, 20)
            
            min_p, max_p = price_ranges[main_cat]
            price = random.randint(min_p, max_p)
            compare_price = int(price * random.uniform(1.15, 1.4)) if random.random() < 0.2 else ""
            
            # Use a dummy image generator URL for the main image
            # Note: We encode the text to make the URL safe
            cat_encoded = main_cat.replace(' ', '+')
            img_main = f"https://placehold.co/800x800/f0f0f0/333333.png?text={cat_encoded}+Main"
            
            rows.append([
                handle, title, body, vendor, prod_cat, type_val, 
                tags, published, opt1_name, opt1_val, sku, 
                qty, price, compare_price, img_main, "1"
            ])
            
            # --- ROWS 2-5: Additional Angle Images ---
            # In Shopify CSVs, to add more images to the same product, 
            # you duplicate the Handle, add the new Image Src, and leave other product fields blank.
            angles = ["Angle+1", "Angle+2", "Angle+3", "Angle+4"]
            for index, angle_txt in enumerate(angles):
                img_angle = f"https://placehold.co/800x800/ffffff/555555.png?text={cat_encoded}+{angle_txt}"
                pos = str(index + 2) # Positions 2, 3, 4, 5
                
                # Append row with mostly blank fields
                rows.append([
                    handle, "", "", "", "", "", 
                    "", "", "", "", "", 
                    "", "", "", img_angle, pos
                ])

out_path = r"C:\Users\Acer\Dev\swastik-shopify\demo_products_with_images.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    
print("CSV generated successfully at", out_path)
