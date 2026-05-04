# main.py — FastAPI application
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import IrisInput, PredictionResponse
from app import model as ml
from contextlib import asynccontextmanager

import time


# Track request metrics
request_count = 0
prediction_times = []


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model on startup (not on first request)
    print('Loading ML model...')
    ml.load_model()
    print('Model loaded! API ready.')
    yield
    print('Shutting down...')

# Update FastAPI initialization:

app = FastAPI(
    title='Iris ML API',
    description='Predict iris flower species from measurements',
    version='1.0.0',
    lifespan=lifespan
)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], allow_methods=['*'], allow_headers=['*']
)

# Add metrics endpoint
@app.get('/metrics')
def metrics():
    avg_time = sum(prediction_times[-100:]) / max(len(prediction_times[-100:]), 1)
    return {
        'total_predictions': request_count,
        'avg_prediction_ms': round(avg_time * 1000, 2),
    }

 
@app.get('/')
def root():
    return {'message': 'Iris ML API is running!', 'docs': '/docs'}
 
@app.get('/health')
def health():
    return {'status': 'healthy'}
 
@app.post('/predict', response_model=PredictionResponse)
def predict(data: IrisInput):
    global request_count
    start = time.time()
    features = [
        data.sepal_length, data.sepal_width,
        data.petal_length, data.petal_width
    ]
    result = ml.predict(features)
    result['input_received'] = features
    prediction_times.append(time.time() - start)
    request_count += 1
    return result
