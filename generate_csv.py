import csv

colors = ["Yellow Gold", "Rose Gold", "White Gold"]
purities = [
    ("18kt", 5000), # example price per gram
    ("14kt", 4000),
    ("9kt", 3000)
]
diamond_grades = [
    ("F-G VS-SI", 45000),
    ("F-G SI-I", 40000),
    ("G-H VS-SI", 40000),
    ("G-H SI-I", 35000),
    ("H-I VS-SI", 32000),
    ("H-I SI-I", 28000),
    ("I-J VS-SI", 21000),
    ("I-J SI-I", 20000),
]

net_weight = 14.25
gross_weight = 15.0
diamond_weight = 1.75
stone_weight = 0.5
making_charges = 13500

header = [
    "Handle","Title","Body (HTML)","Vendor",
    "Option1 Name","Option1 Value",
    "Option2 Name","Option2 Value",
    "Option3 Name","Option3 Value",
    "Variant SKU","Variant Price",
    "Product Metafield: custom.gross_weight",
    "Product Metafield: custom.net_weight",
    "Product Metafield: custom.diamond_weight",
    "Product Metafield: custom.stone_weight",
    "Variant Metafield: custom.gold_value",
    "Variant Metafield: custom.diamond_value",
    "Variant Metafield: custom.making_charges",
    "Variant Metafield: custom.gst_amount"
]

rows = []
is_first_row = True

for color in colors:
    for purity_name, purity_rate in purities:
        for grade_name, grade_rate in diamond_grades:
            
            # Simulated calculations based on your provided per-carat prices
            gold_value = round(net_weight * purity_rate)
            diamond_value = round(diamond_weight * grade_rate)
            
            subtotal = gold_value + diamond_value + making_charges
            gst = round(subtotal * 0.03)
            total_price = subtotal + gst
            
            sku = f"SKU-{purity_name[:2]}-{color[:1]}-{grade_name.replace(' ', '')}"
            
            row = {
                "Handle": "diamond-ring-01",
                "Option1 Name": "Gold Color",
                "Option1 Value": color,
                "Option2 Name": "Gold Purity",
                "Option2 Value": purity_name,
                "Option3 Name": "Diamond Quality",
                "Option3 Value": grade_name,
                "Variant SKU": sku,
                "Variant Price": total_price,
                "Variant Metafield: custom.gold_value": gold_value,
                "Variant Metafield: custom.diamond_value": diamond_value,
                "Variant Metafield: custom.making_charges": making_charges,
                "Variant Metafield: custom.gst_amount": gst,
            }
            
            if is_first_row:
                row["Title"] = "Elegant Diamond Ring"
                row["Body (HTML)"] = "<p>A beautiful ring.</p>"
                row["Vendor"] = "Swastik Jewellers"
                row["Product Metafield: custom.gross_weight"] = gross_weight
                row["Product Metafield: custom.net_weight"] = net_weight
                row["Product Metafield: custom.diamond_weight"] = diamond_weight
                row["Product Metafield: custom.stone_weight"] = stone_weight
                is_first_row = False
            
            # Fill missing keys with empty string
            final_row = [row.get(col, "") for col in header]
            rows.append(final_row)

with open("sample_product_import_full.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
