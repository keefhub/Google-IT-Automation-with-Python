#!/usr/bin/env python3

from PIL import Image
import os

input_folder = os.path.expanduser("~/supplier-data/images")
output_folder = input_folder

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    # Skip the .DS_Store file
    if filename == ".DS_Store":
        continue

    if not filename.endswith(".jpeg"):
        # Open the image file
        image_path = os.path.join(input_folder, filename)
        try:
            image = Image.open(image_path)
        except IOError:
            print(f"Error opening image: {image_path}")
            continue

        rgb_image = image.convert("RGB")

        resized_image = rgb_image.resize((600, 400))

        output_path = os.path.join(output_folder, filename.replace(".tiff", ".jpeg"))
        resized_image.save(output_path, "JPEG")

        print(f"Processed image saved: {output_path}")
