from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, ValidationError
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
async def predict_speed(request: Request, pokemon: PokemonInput):
    try:
        # Extract data from request
        data = [pokemon.HP, pokemon.Attack, pokemon.Defense, pokemon.Sp_Atk, pokemon.Sp_Def]
        
        # Make a prediction
        prediction = model.predict([data])
        
        # Return the prediction
        return {"predicted_speed": prediction[0]}
    except ValidationError as e:
        # If input data is invalid
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Input data validation error",
            headers={"X-Error": "There was a problem with the input data"},
        )
    except Exception as e:
        # For all other server-side errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

