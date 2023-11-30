import requests
import json

# URL of the API endpoint
url = "http://127.0.0.1:8000/predict"

# Load data from the JSON file
file_path = '/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/CDS_HW9/example_input.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Sending the POST request to the API and getting the response
response = requests.post(url, json=data)

# Checking if the request was successful
if response.status_code == 200:
    # Printing the prediction
    print("Prediction:", response.json())
else:
    print("Failed to get a valid response. Status code:", response.status_code)
