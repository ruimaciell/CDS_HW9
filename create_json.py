import json

# Example input data
data = {
    "HP": 80,
    "Attack": 100,
    "Defense": 65,
    "Sp_Atk": 70,
    "Sp_Def": 10
}

# File path
file_path = '/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/CDS_HW9/example_input.json'

# Writing to a file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"File created: {file_path}")
