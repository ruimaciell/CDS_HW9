import requests
import json

# The URL of the API endpoint
api_url = 'http://127.0.0.1:5000/predict'

# Load the data to be sent to the API
with open('/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/CDS_HW9/Notebooks/example_input.json', 'r') as file:
    data = json.load(file)

try:
    # Send a POST request to the API with the JSON data
    response = requests.post(api_url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Prediction:", response.json())
    else:
        print(f"Error: {response.status_code}, Message: {response.text}")

except requests.exceptions.ConnectionError:
    print("Failed to connect to the API.")
except requests.exceptions.Timeout:
    print("The request to the API timed out.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
