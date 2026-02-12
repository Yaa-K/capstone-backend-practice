from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class LearnerData(BaseModel):
    attendance: int
    average_score: float
    login_frequency: int

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/predict")
def predict(data: LearnerData):
    # Fake AI logic (simulate risk score)
    risk_score = random.uniform(0, 1)

    if risk_score > 0.7:
        risk_level = "High Risk"
    elif risk_score > 0.4:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level,
        "explanation": "Risk determined based on engagement patterns."
    }
