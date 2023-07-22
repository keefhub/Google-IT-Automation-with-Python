#!/usr/bin/python3

from PIL import Image
import os

# Get the current working directory
cwd = os.getcwd()


input_folder = os.path.join(cwd, "images")

output_folder = "/opt/icons/"


os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    # Skip the .DS_Store file
    if filename == ".DS_Store":
        continue

    if not filename.endswith(".jpeg"):
        # Open the image file
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        rotated_image = image.rotate(-90, expand=True)

        rgb_image = rotated_image.convert("RGB")

        resized_image = rgb_image.resize((128, 128))

        output_path = os.path.join(output_folder, filename.replace(".tiff", ".jpeg"))
        resized_image.save(output_path, "JPEG")

        print(f"Processed image saved: {output_path}")