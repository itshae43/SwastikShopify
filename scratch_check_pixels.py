import os
from PIL import Image

image_path = os.path.join("assets", "Slideshow_Desktop_1_New.png")
if not os.path.exists(image_path):
    print(f"File {image_path} does not exist!")
    exit(1)

try:
    img = Image.open(image_path)
    width, height = img.size
    print(f"Image format: {img.format}, size: {width}x{height}")
    
    # Check the first 10 columns of pixels at different heights
    # We will sample 10 points along the height
    for y in range(0, height, height // 10):
        row_pixels = []
        for x in range(10):
            pixel = img.getpixel((x, y))
            # Format pixel as hex or RGB
            row_pixels.append(pixel)
        print(f"y={y}: {row_pixels}")
except Exception as e:
    print("Error:", e)
