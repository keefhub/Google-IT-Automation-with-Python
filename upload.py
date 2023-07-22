import os
import requests

directory = '/data/feedback'

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
        title = lines[0].strip()
        name = lines[1].strip()
        date = lines[2].strip()
        feedback = lines[3].strip()
        
        # Create a dictionary for the feedback
        feedback_dict = {
            'title': title,
            'name': name,
            'date': date,
            'feedback': feedback
        }
        
        # Add the dictionary to the feedback list
        feedback_list.append(feedback_dict)

# Make a POST request to the company's website
url = 'http://34.75.14.120/feedback/'  

for feedback in range(len(feedback_list)):
    response = requests.post(url, json=feedback) #sending in feedback in json file

# Check the response status
    if response.status_code == 201:
        print("Feedbacks successfully uploaded!")
    else:
        print("Error uploading feedbacks.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

