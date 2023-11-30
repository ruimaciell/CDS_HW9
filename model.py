from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump
import pandas as pd

pokemon_data = pd.read_csv('/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/CDS_HW9/pokemon.csv')
# Selecting the features and target
features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def']
target = 'Speed'

X = pokemon_data[features]
y = pokemon_data[target]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting and evaluating the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Serializing the model
model_filename = '/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/CDS_HW9/pokemon_speed_predictor_model.pkl'
dump(model, model_filename)

mse, model_filename  # Return the mean squared error and the path to the saved model file