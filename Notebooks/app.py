from flask import Flask, request, jsonify
from joblib import load

# Create a Flask app
app = Flask(__name__)

# Load your trained model
model = load('/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/CDS_HW9/Notebooks/model_filename.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request has JSON data
    if request.is_json:
        # Get JSON data from request
        input_data = request.get_json()

        # Assuming the JSON data is a dictionary with a key 'features' that contains the input features
        features = input_data['features']

        # Predict using your model
        prediction = model.predict([features])

        # Return the prediction
        return jsonify({'prediction': prediction.tolist()})
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
