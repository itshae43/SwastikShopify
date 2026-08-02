# Swastik Jewellers - Variant Pricing Calculation PRD

## 1. Overview
The pricing engine automatically calculates the cost of jewelry pieces based on global base rates (24K Gold, Diamond per Carat, Stone per Carat, Labour per Gram) and specific product attributes (Net Weight, Diamond Weight, Stone Weight). It dynamically generates multiple variants for combinations of Gold Colors, Purities, and Diamond Qualities.

This architecture enables a live, scalable CRM/Storefront where global market fluctuations (like a change in 24K gold rate) immediately recalculate all variant prices without needing to update individual products.

## 2. Product Input Data
The system ingests product listings containing the following specific physical attributes:
- **SKU**: Base Stock Keeping Unit
- **Net Weight**: Weight of gold in grams (excluding stones)
- **Diamond Weight**: Weight of diamonds in carats
- **Stone Weight**: Weight of colour stones in carats (defaults to 0)
- **Source Purity**: Used as the default/preferred karat.

## 3. Global Pricing Settings & Constants
The calculations rely on global settings which can be updated centrally in the admin panel:
- **24K Gold Rate**: e.g., ₹14,200 per gram (derived from ₹1,42,000 per 10g).
- **Gold Purity Multipliers**: 
  - **18K** = 76% of 24K (0.76)
  - **14K** = 60% of 24K (0.60)
  - **9K** = 40% of 24K (0.40)
- **Diamond Rates (per carat)**:
  - F-G VS-SI: ₹45,000
  - F-G SI-I: ₹40,000
  - G-H VS-SI: ₹40,000
  - G-H SI-I: ₹35,000
  - H-I VS-SI: ₹32,000
  - H-I SI-I: ₹28,000
  - I-J VS-SI: ₹21,000
  - I-J SI-I: ₹20,000
- **Stone Rate**: e.g., ₹500 per carat
- **Making Charges (Labour)**: e.g., ₹1,000 per gram of net gold weight
- **GST Percentage**: e.g., 3%

## 4. Calculation Formulas
For any given variant, the system calculates the final price using these exact formulas (rounding to nearest integer at each step):

1. **Gold Rate per Gram**:
   `Gold Rate = Round(Base 24K Rate × Purity Multiplier)`

2. **Gold Value**:
   `Gold Value = Round(Gold Rate × Net Weight)`

3. **Diamond Value**:
   `Diamond Value = Round(Diamond Rate per Ct [for specific quality] × Diamond Weight)`

4. **Stone Value**:
   `Stone Value = Round(Stone Rate per Ct × Stone Weight)`

5. **Making Charges (Labour)**:
   `Making Charges = Round(Making Charge per Gram × Net Weight)`
   > [!NOTE]
   > Labour is billed dynamically per gram of net gold weight, not as a flat amount per piece. A heavier piece costs proportionally more to make.

6. **Subtotal**:
   `Subtotal = Gold Value + Diamond Value + Stone Value + Making Charges`

7. **GST Amount**:
   `GST Amount = Round(Subtotal × (GST % / 100))`

8. **Total Final Price**:
   `Total Price = Subtotal + GST Amount`

## 5. Variant Generation Workflow
Instead of storing static prices, the engine dynamically generates combinations for a product based on available options:
- **Colors**: Yellow Gold, Rose Gold, White Gold
- **Purities**: 18K, 14K, 9K
- **Qualities**: All 8 available Diamond Qualities (F-G VS-SI, etc.)

**Generation Process:**
1. Loop through all selected Colors, Purities, and Qualities.
2. For each combination, apply the specific Purity Multiplier to get the Gold Rate.
3. Apply the specific Quality Rate to get the Diamond Rate.
4. Pass these along with the fixed physical attributes (Net Weight, Diamond/Stone Weight) into the Calculation Engine.
5. Store the resulting `goldValue`, `diamondValue`, `makingCharges`, `gstAmount`, and `totalPrice` in the variant payload to send to Shopify or the CRM.
6. **SKU Inheritance**: Every variant carries the product's base SKU (avoiding the need for 72 separate SKUs for a single product).
7. **Sorting**: The "Preferred/Source Purity" from the input data is placed first so the UI opens on the default karat, while still allowing the customer to switch.
