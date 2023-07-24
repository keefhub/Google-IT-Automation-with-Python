#!/usr/bin/env python3

import os
import requests

directory = os.path.expanduser('~/supplier-data/descriptions')

# Get a list of all .txt files in the directory
txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]

# List to store the feedback dictionaries
feedback_list = []

# Iterate over each text file
for txt_file in txt_files:
    file_path = os.path.join(directory, txt_file)
    
    # Read the contents of the text file
    with open(file_path, 'r') as file:
        lines = file.readlines()

        if len(lines) < 4:
            # Skip this file if it doesn't have enough lines
            print(f"Skipping file: {txt_file}. Not enough lines in the file.")
            continue

        title = lines[0].strip()
        name = lines[1].strip()
        weight = lines[2].strip().replace(" lbs", "")  # Removes " lbs" from the weight string and converts to integer
        description = lines[3].strip()
        
        # Create a dictionary for the feedback
        feedback_dict = {
            'title': title,
            'name': name,
            'weight': int(weight),  # Convert the weight to an integer
            'description': description
        }
        
        # Add the dictionary to the feedback list
        feedback_list.append(feedback_dict)

# Make a POST request to the company's website
url = 'http://34.123.232.188/fruits/' 

for feedback in feedback_list:
    response = requests.post(url, json=feedback)  # sending feedback as JSON data

    # Check the response status
    if response.status_code == 201:
        print("Feedback successfully uploaded!")
    else:
        print("Error uploading feedback.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
