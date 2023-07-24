#!/usr/bin/env python3
import os
import requests

# This example shows how multiple files can be uploaded using
# the Python Requests module

url = "http://localhost/upload/"
images_folder = os.path.expanduser("~/supplier-data/images")

for filename in os.listdir(images_folder):
    image_path = os.path.join(images_folder, filename)

    if not os.path.isfile(image_path) or not filename.endswith(".jpeg"):
        continue  # Skip directories, non-file items, and files that are not .jpeg in the folder

    with open(image_path, 'rb') as opened:
        files = {'file': opened}
        r = requests.post(url, files=files)

    if r.status_code == 200:
        print(f"Image '{filename}' uploaded successfully.")
    else:
        print(f"Failed to upload image '{filename}'. Status code: {r.status_code}")
