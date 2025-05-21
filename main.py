# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class DrugInput(BaseModel):
    Age: int
    Sex: int
    BP: int
    Cholesterol: int
    Na_to_K: float

@app.post("/predict")
def predict(data: DrugInput):
    features = np.array([[data.Age, data.Sex, data.BP, data.Cholesterol, data.Na_to_K]])
    prediction = model.predict(features)
    return {"predicted_drug": prediction[0]}
