# hello_ml.py — Your first machine learning script
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
 
# 1. Load data
data = load_iris()
X, y = data.data, data.target
print(f'Dataset: {X.shape[0]} samples, {X.shape[1]} features')
print(f'Classes: {data.target_names}')
 
# 2. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
# 3. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print('Model trained!')
 
# 4. Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2%}')
 
# 5. Make a prediction
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example flower measurements
result = model.predict(sample)
print(f'Prediction for {sample[0]}: {data.target_names[result[0]]}')
