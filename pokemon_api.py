from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

# Define a class for the input data
class PokemonInput(BaseModel):
    HP: int
    Attack: int
    Defense: int
    Sp_Atk: int
    Sp_Def: int

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load("pokemon_speed_predictor_model.pkl")

# Define a root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Pokémon Speed Prediction API!"}

# Define the prediction endpoint
@app.post("/predict")
async def predict_speed(pokemon: PokemonInput):
    try:
        # Extract data from request
        data = [pokemon.HP, pokemon.Attack, pokemon.Defense, pokemon.Sp_Atk, pokemon.Sp_Def]
        
        # Make a prediction
        prediction = model.predict([data])
        
        # Return the prediction
        return {"predicted_speed": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

