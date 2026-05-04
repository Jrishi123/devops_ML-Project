# schemas.py — data models for the API
from pydantic import BaseModel, Field
from typing import Dict
 
class IrisInput(BaseModel):
    sepal_length: float = Field(..., ge=0, le=10, example=5.1)
    sepal_width:  float = Field(..., ge=0, le=10, example=3.5)
    petal_length: float = Field(..., ge=0, le=10, example=1.4)
    petal_width:  float = Field(..., ge=0, le=10, example=0.2)

 
class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    all_probabilities: Dict[str, float]
    input_received: list
