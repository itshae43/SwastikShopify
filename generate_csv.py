import csv

colors = ["Rose Gold", "Yellow Gold", "White Gold"]
purities = [("9kt", 0.375), ("14kt", 0.583), ("18kt", 0.75)]
diamonds = [
    ("F-G VS-SI", 45000),
    ("F-G SI-I", 40000),
    ("G-H VS-SI", 40000),
    ("G-H SI-I", 35000),
    ("H-I VS-SI", 3200),
    ("H-I SI-I", 28000),
    ("I-J VS-SI", 2100),
    ("I-J SI-I", 2000)
]

# The Master Formula Variables (Test Data)
gold_rate_24k = 7000 # per gram
gold_weight = 5.0 # grams
diamond_weight = 1.0 # carat
making_charges = 3000

rows = []
header = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", "Tags", "Published",
    "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value", "Option3 Name", "Option3 Value",
    "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Qty", "Variant Inventory Policy", 
    "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price", "Variant Requires Shipping", "Variant Taxable",
    "Image Src", "Image Position", "Image Alt Text", "Gift Card", "SEO Title", "SEO Description",
    "Google Shopping / Google Product Category", "Google Shopping / Gender", "Google Shopping / Age Group", 
    "Google Shopping / MPN", "Google Shopping / AdWords Grouping", "Google Shopping / AdWords Labels", 
    "Google Shopping / Condition", "Google Shopping / Custom Product", "Google Shopping / Custom Label 0", 
    "Google Shopping / Custom Label 1", "Google Shopping / Custom Label 2", "Google Shopping / Custom Label 3", 
    "Google Shopping / Custom Label 4", "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item", 
    "Included / India", "Status"
]

first_row = True
for color in colors:
    for purity_name, purity_mult in purities:
        for dia_name, dia_price_per_ct in diamonds:
            # The Automatic Math Calculation
            gold_cost = gold_rate_24k * purity_mult * gold_weight
            diamond_cost = dia_price_per_ct * diamond_weight
            total_price = round(gold_cost + diamond_cost + making_charges)
            
            # Shopify only needs Title and Status on the first row of a product
            title = "Sample Custom Diamond Ring" if first_row else ""
            status = "active" if first_row else ""
            
            # Fill out the row with Shopify's required empty columns
            row = [
                "sample-custom-diamond-ring", # Handle
                title, # Title
                "", "", "", "", "", "", # Body to Published
                "Metal Color", color, # Option 1
                "Gold Purity", purity_name, # Option 2
                "Diamond Quality", dia_name, # Option 3
                "", "", "shopify", "10", "deny", "manual", # SKU to Fulfillment
                str(total_price), # Variant Price
                "", "TRUE", "TRUE", # Compare Price, Shipping, Taxable
                "", "", "", "FALSE", "", "", # Image to SEO
                "", "", "", "", "", "", "", "", "", "", "", "", "", "", # Google Shopping
                "kg", "", "", "TRUE", status # Unit to Status
            ]
            rows.append(row)
            first_row = False

with open('sample_jewelry_product.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
print("CSV generated successfully.")
