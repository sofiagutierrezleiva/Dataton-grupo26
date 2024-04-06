from PIL import Image, ImageDraw
import numpy as np
import os

def process_image(image_path, coordinates):
    img = Image.open(image_path)
    x1, y1, x2, y2 = coordinates
    region = img.crop((x1, y1, x2, y2))
    
    region_np = np.array(region)
    colors, count = np.unique(region_np.reshape(-1, region_np.shape[-1]), axis=0, return_counts=True)
    most_common_color = colors[count.argmax()]
    
    processed_img = Image.new("RGB", img.size, "black")
    draw = ImageDraw.Draw(processed_img)

    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            if all(pixel == most_common_color):
                draw.point((x, y), "white")
    
    return processed_img

coordinates = (110, 45, 160, 95) 


for file in os.listdir("images/landsat9_c2l2_sr"):
    if file.endswith("_mask.png"):
        image_path = os.path.join("images/landsat9_c2l2_sr", file)
        processed_img = process_image(image_path, coordinates)
        processed_img.save(os.path.join("corrected_images/landsat9_c2l2_sr", file))
        print(f"Processed {file}")
