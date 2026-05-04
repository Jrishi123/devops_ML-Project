# model.py — handles ML model training and prediction
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from pathlib import Path
 
MODEL_PATH = Path('model/iris_model.pkl')
CLASSES = ['setosa', 'versicolor', 'virginica']
 
def train_and_save():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    MODEL_PATH.parent.mkdir(exist_ok=True)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    print(f'Model saved to {MODEL_PATH}')
    return model
 
def load_model():
    if not MODEL_PATH.exists():
        return train_and_save()
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)
 
def predict(features: list) -> dict:
    model = load_model()
    arr = np.array([features])
    prediction = model.predict(arr)[0]
    proba = model.predict_proba(arr)[0]
    return {
        'prediction': CLASSES[prediction],
        'confidence': round(float(proba.max()), 4),
        'all_probabilities': dict(zip(CLASSES, proba.round(4).tolist()))
    }
