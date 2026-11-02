from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Healthcare Diagnosis Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://health-sense-ai-seven.vercel.app"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load trained model
model = joblib.load("models/disease_prediction_model.pkl")

# Load symptom names
df = pd.read_csv("data/raw/Training.csv")
df = df.dropna(axis=1, how="all")

symptoms = df.drop(columns=["prognosis"]).columns.tolist()

# Define input format
class SymptomInput(BaseModel):
    symptoms: list[str]

# Home endpoint
@app.get("/")
def home():
    return {"message": "Healthcare Diagnosis Assistant API is running!"}

@app.get("/symptoms")
def get_symptoms():
    return {"symptoms": symptoms}

# Prediction endpoint
@app.post("/predict")
def predict(data: SymptomInput):

    if not data.symptoms:
        raise HTTPException(
            status_code=400,
            detail="Please select at least one symptom."
        )

    invalid = [
        s for s in data.symptoms
        if s not in symptoms
    ]

    if invalid:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid symptoms: {invalid}"
        )

    input_data = [0] * len(symptoms)

    for symptom in data.symptoms:
        index = symptoms.index(symptom)
        input_data[index] = 1

    input_df = pd.DataFrame([input_data], columns=symptoms)

    probabilities = model.predict_proba(input_df)[0]

    top_3 = probabilities.argsort()[-3:][::-1]

    results = [
        {
            "condition": model.classes_[i],
            "model_score": round(float(probabilities[i]) * 100, 2)
        }
        for i in top_3
    ]

    return {
        "predictions": results,
        "disclaimer": "Educational model output only. Not a medical diagnosis."
    }
