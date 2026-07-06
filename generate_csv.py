import csv
import random
import math
import os

categories = {
    "Lab Grown Diamond": ["Ring", "Bracelet", "Gents Ring", "Earring", "Pendant"],
    "Natural Diamond": ["Ring", "Bracelet", "Gents Ring", "Earring", "Pendant", "Necklace", "Pendant Set", "Bangle", "Mangalsutra"],
    "Gold Jewellery": ["Chain", "Ladies Ring", "Pendant Set", "Choker Set", "Bracelet", "Bangle", "Necklace Set", "Chikpatti", "Long Set", "Earring", "Tika"]
}

# Realistic INR prices for the Indian Market
price_ranges = {
    "Lab Grown Diamond": (15000, 150000), # 15k to 1.5 Lakhs
    "Natural Diamond": (35000, 750000),   # 35k to 7.5 Lakhs
    "Gold Jewellery": (25000, 400000)     # 25k to 4 Lakhs
}

rows = []
header = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", 
    "Tags", "Published", "Option1 Name", "Option1 Value", "Variant SKU", 
    "Variant Inventory Qty", "Variant Price", "Variant Compare At Price", "Image Src"
]
rows.append(header)

target_per_main = 1010

for main_cat, subcats in categories.items():
    per_subcat = math.ceil(target_per_main / len(subcats))
    
    for subcat in subcats:
        for i in range(1, per_subcat + 1):
            handle = f"{main_cat.lower().replace(' ', '-')}-{subcat.lower().replace(' ', '-')}-{i:04d}"
            title = f"{main_cat} {subcat} Model {i:04d}"
            body = f"<p>Exquisite {main_cat.lower()} {subcat.lower()} designed for elegance and durability. Perfect for any occasion.</p>"
            vendor = "Demo Brand"
            prod_cat = "Apparel & Accessories > Jewelry"
            type_val = subcat
            tags = f"{main_cat}, {subcat}, Demo"
            published = "TRUE"
            
            # Variant Option (Size for rings/bangles, Default for others)
            opt1_name = "Title" if subcat not in ["Ring", "Gents Ring", "Ladies Ring", "Bangle"] else "Size"
            
            if opt1_name == "Size" and subcat == "Bangle":
                opt1_val = str(random.choice(["2.2", "2.4", "2.6", "2.8"]))
            elif opt1_name == "Size":
                opt1_val = str(random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18]))
            else:
                opt1_val = "Default Title"
                
            sku = f"SKU-{main_cat[:2].upper()}-{subcat[:2].upper()}-{i:04d}"
            qty = random.randint(1, 20)
            
            # Generate Price in INR
            min_p, max_p = price_ranges[main_cat]
            price = random.randint(min_p, max_p)
            
            # 20% chance to have a discount (Compare at price is higher)
            compare_price = int(price * random.uniform(1.15, 1.4)) if random.random() < 0.2 else ""
            
            # Empty image source as requested
            img_src = ""
            
            rows.append([
                handle, title, body, vendor, prod_cat, type_val, 
                tags, published, opt1_name, opt1_val, sku, 
                qty, price, compare_price, img_src
            ])

out_path = r"C:\Users\Acer\Dev\swastik-shopify\demo_products.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    
print("CSV generated successfully at", out_path, "with", len(rows)-1, "products.")
