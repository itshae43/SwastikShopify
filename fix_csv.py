import re

with open('ai_generated_product_import.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i > 1:
        # Replace 6 commas with 4 commas after the price
        line = re.sub(r'(\d{6}),,,,,,', r'\1,,,,', line)
    new_lines.append(line)

with open('ai_generated_product_import.csv', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
