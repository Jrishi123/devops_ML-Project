# main.py — FastAPI application
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import IrisInput, PredictionResponse
from app import model as ml
 
app = FastAPI(
    title='Iris ML API',
    description='Predict iris flower species from measurements',
    version='1.0.0'
)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], allow_methods=['*'], allow_headers=['*']
)
 
@app.get('/')
def root():
    return {'message': 'Iris ML API is running!', 'docs': '/docs'}
 
@app.get('/health')
def health():
    return {'status': 'healthy'}
 
@app.post('/predict', response_model=PredictionResponse)
def predict(data: IrisInput):
    features = [
        data.sepal_length, data.sepal_width,
        data.petal_length, data.petal_width
    ]
    result = ml.predict(features)
    result['input_received'] = features
    return result