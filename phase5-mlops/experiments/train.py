# train.py — ML training with full experiment tracking
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import json
 
mlflow.set_tracking_uri('http://127.0.0.1:5001')  # Store experiments locally
mlflow.set_experiment('iris-classification')
 
def train_model(model, model_name, params):
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )
 
    with mlflow.start_run(run_name=model_name):
        # Log hyperparameters
        mlflow.log_params(params)
 
        # Train
        model.fit(X_train, y_train)
 
        # Evaluate
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        cv_scores = cross_val_score(model, data.data, data.target, cv=5)
 
        # Log metrics
        mlflow.log_metric('accuracy', accuracy)
        mlflow.log_metric('cv_mean', cv_scores.mean())
        mlflow.log_metric('cv_std', cv_scores.std())
 
        # Save classification report
        report = classification_report(y_test, predictions,
                                       target_names=data.target_names,
                                       output_dict=True)
        with open('report.json', 'w') as f:
            json.dump(report, f, indent=2)
        mlflow.log_artifact('report.json')
 
        # Save model
        mlflow.sklearn.log_model(model, 'model')
 
        print(f'{model_name}: accuracy={accuracy:.4f}, cv={cv_scores.mean():.4f}')
        return accuracy
 
if __name__ == '__main__':
    # Experiment 1: Random Forest
    train_model(
        RandomForestClassifier(n_estimators=100, random_state=42),
        'random-forest-100',
        {'model': 'RandomForest', 'n_estimators': 100}
    )
 
    # Experiment 2: More trees
    train_model(
        RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42),
        'random-forest-200',
        {'model': 'RandomForest', 'n_estimators': 200, 'max_depth': 5}
    )
 
    # Experiment 3: Gradient Boosting
    train_model(
        GradientBoostingClassifier(n_estimators=100, random_state=42),
        'gradient-boosting',
        {'model': 'GradientBoosting', 'n_estimators': 100}
    )
 
    print('All experiments complete! View at http://localhost:5000')
