# test_api.py — automated tests for the ML API
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.model import predict
 
client = TestClient(app)
 
def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert 'message' in response.json()
 
def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'
 
def test_predict_setosa():
    response = client.post('/predict', json={
        'sepal_length': 5.1, 'sepal_width': 3.5,
        'petal_length': 1.4, 'petal_width': 0.2
    })
    assert response.status_code == 200
    data = response.json()
    assert data['prediction'] == 'setosa'
    assert data['confidence'] > 0.9
 
def test_predict_versicolor():
    response = client.post('/predict', json={
        'sepal_length': 6.0, 'sepal_width': 2.9,
        'petal_length': 4.5, 'petal_width': 1.5
    })
    assert response.status_code == 200
    assert response.json()['prediction'] == 'versicolor'
 
def test_predict_invalid_input():
    response = client.post('/predict', json={
        'sepal_length': -1,  # Invalid: negative value
        'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2
    })
    assert response.status_code == 422  # Validation error
 
def test_model_prediction_logic():
    result = predict([5.1, 3.5, 1.4, 0.2])
    assert 'prediction' in result
    assert 'confidence' in result
    assert result['confidence'] >= 0 and result['confidence'] <= 1
