import pandas as pd
from pymongo import MongoClient
import sys

# --- CONFIGURATION ---
# Replace with your actual MongoDB connection string. 
# You can find this in MongoDB Compass by clicking on the connection.
MONGO_URI = "mongodb+srv://swastikjewels2025_db_user:BlGirKXhv4dwxZ3b@cluster0.tsz3lz1.mongodb.net/Swastik?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Swastik"
COLLECTION_NAME = "products"
EXCEL_FILE = "Listings.xlsx"
SKU_COLUMN = "sku" # Replace if the column in your Excel file is named differently

def main():
    try:
        # 1. Read the Excel file
        print(f"Reading Excel file: {EXCEL_FILE}...")
        df = pd.read_excel(EXCEL_FILE)
        
        # Use the first column (index 0) for SKUs
        sku_series = df.iloc[:, 0]
            
        # Get all non-null SKUs from the Excel file and convert to strings
        # We will also drop 'Item Code' if it was accidentally parsed as a value
        excel_skus = set(sku_series.dropna().astype(str).str.strip())
        if 'Item Code' in excel_skus:
            excel_skus.remove('Item Code')
        if 'sku' in excel_skus:
            excel_skus.remove('sku')
            
        print(f"Found {len(excel_skus)} unique SKUs in {EXCEL_FILE}.")

        # 2. Connect to MongoDB
        print("\nConnecting to MongoDB...")
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        
        # 3. Fetch all tagNo from the MongoDB products collection
        print(f"Fetching 'tagNo' from the '{COLLECTION_NAME}' collection...")
        # We only need the tagNo field
        mongo_docs = collection.find({"tagNo": {"$exists": True, "$ne": None}}, {"tagNo": 1})
        
        mongo_tags = set()
        for doc in mongo_docs:
            if "tagNo" in doc and doc["tagNo"]:
                mongo_tags.add(str(doc["tagNo"]).strip())
                
        print(f"Found {len(mongo_tags)} unique tagNos in MongoDB.")
        
        # 4. Compare the two sets
        missing_in_mongo = excel_skus - mongo_tags
        missing_in_excel = mongo_tags - excel_skus
        
        # 5. Output the results
        print("\n--- RESULTS ---")
        print(f"Total SKUs missing in MongoDB: {len(missing_in_mongo)}")
        if len(missing_in_mongo) > 0:
            print("Here are some of the SKUs missing in MongoDB (from your Excel):")
            for sku in list(missing_in_mongo)[:20]: # Show up to 20
                print(f" - {sku}")
            if len(missing_in_mongo) > 20:
                print(f" ... and {len(missing_in_mongo) - 20} more.")
                
            # Optionally, save the missing SKUs to a text file
            with open("missing_skus_in_mongo.txt", "w") as f:
                for sku in sorted(missing_in_mongo):
                    f.write(sku + "\n")
            print("-> A full list of missing SKUs has been saved to 'missing_skus_in_mongo.txt'.")
        else:
            print("Great! All SKUs from the Excel file are present in MongoDB.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
