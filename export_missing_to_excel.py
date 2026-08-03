import pandas as pd
from pymongo import MongoClient

# --- CONFIGURATION ---
MONGO_URI = "mongodb+srv://swastikjewels2025_db_user:BlGirKXhv4dwxZ3b@cluster0.tsz3lz1.mongodb.net/Swastik?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Swastik"
COLLECTION_NAME = "products"
INPUT_EXCEL = "Listings.xlsx"
OUTPUT_EXCEL = "Missing_Listings_All_Sheets.xlsx"

def main():
    print(f"Reading original Excel file: {INPUT_EXCEL}...")
    # Read all sheets by setting sheet_name=None
    all_sheets = pd.read_excel(INPUT_EXCEL, sheet_name=None)
    
    print("Connecting to MongoDB...")
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    # Fetch all tagNo from MongoDB
    print(f"Fetching 'tagNo' from MongoDB collection '{COLLECTION_NAME}'...")
    mongo_docs = collection.find({"tagNo": {"$exists": True, "$ne": None}}, {"tagNo": 1})
    
    mongo_tags = set()
    for doc in mongo_docs:
        if "tagNo" in doc and doc["tagNo"]:
            mongo_tags.add(str(doc["tagNo"]).strip())
            
    print(f"Total unique tags in MongoDB: {len(mongo_tags)}")
    
    def is_missing(val):
        if pd.isna(val):
            return False
        
        # Don't consider the header "Item Code" or "SKU" as a valid item if it somehow gets here
        str_val = str(val).strip()
        if str_val.lower() == 'sku' or str_val.lower() == 'item code':
            return False
            
        return str_val not in mongo_tags

    all_missing_dfs = []
    
    print("\n--- PROCESSING SHEETS ---")
    for sheet_name, df in all_sheets.items():
        print(f"Checking sheet: {sheet_name}")
        if df.empty:
            continue
            
        # Extract SKU from the first column
        sku_series = df.iloc[:, 0]
        
        # Apply the filter
        missing_mask = sku_series.apply(is_missing)
        missing_df = df[missing_mask].copy()
        
        # Drop rows that are completely empty if any
        missing_df = missing_df.dropna(how='all')
        
        if not missing_df.empty:
            # Add a column to identify which sheet it came from (optional, but helpful)
            missing_df.insert(0, 'Source_Sheet', sheet_name)
            all_missing_dfs.append(missing_df)
            print(f"  -> Found {len(missing_df)} missing items in '{sheet_name}'.")
        else:
            print(f"  -> No missing items in '{sheet_name}'.")

    print(f"\n--- RESULTS ---")
    if all_missing_dfs:
        # Combine all missing items into a single DataFrame
        final_missing_df = pd.concat(all_missing_dfs, ignore_index=True)
        missing_count = len(final_missing_df)
        print(f"Total missing products found across all sheets: {missing_count}")
        
        # Save to new Excel file
        print(f"Exporting the missing items to {OUTPUT_EXCEL}...")
        final_missing_df.to_excel(OUTPUT_EXCEL, index=False)
        print("Export completed successfully!")
    else:
        print("No missing products found in any sheet.")

if __name__ == "__main__":
    main()
