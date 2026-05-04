# DevOps + Machine Learning Project

## 📌 Overview

This project is part of my DevOps and Machine Learning learning journey.
In this phase, I set up a professional development environment, automated project setup using Bash scripting, and built my first Machine Learning model using Python.

---

# 🚀 Technologies Used

* Python 3
* Bash Scripting
* Git & GitHub
* scikit-learn
* NumPy
* Pandas
* Linux / macOS Terminal

---

# 📁 Project Structure

```text id="d2xq4x"
devops-ml-project/
│
├── phase1-foundation/
│   ├── scripts/
│   │   ├── setup.sh
│   │   └── hello_ml.py
│   ├── requirements.txt
│   └── README.md
│
└── .gitignore
```

---

# ⚙️ Python Setup Script

File: `scripts/setup.sh`

This Bash script automates the initial project setup process.

## What This Script Does

### ✅ Creates a Python Virtual Environment

```bash id="h7hbrj"
python3 -m venv venv
```

A virtual environment isolates project dependencies from the system Python installation.

---

### ✅ Activates the Virtual Environment

```bash id="jlwmjg"
source venv/bin/activate
```

This ensures all Python packages are installed only for this project.

---

### ✅ Installs Required Python Packages

```bash id="5z2hsm"
pip install -r requirements.txt
```

Automatically installs dependencies listed in `requirements.txt`.

---

### ✅ Creates Logging Directory

```bash id="td3nbd"
mkdir -p logs
```

Stores setup logs for tracking and debugging.

---

### ✅ Writes Setup Logs

```bash id="62wd6u"
echo "[OK] Setup complete at $(date)" >> logs/setup.log
```

Maintains a log history of setup executions.

---

# 🤖 Machine Learning Script

File: `scripts/hello_ml.py`

This script demonstrates a complete beginner-friendly Machine Learning workflow using Python and scikit-learn.

---

# 🧠 What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence where computers learn patterns from data and make predictions without being explicitly programmed.

Instead of writing fixed rules, we train models using datasets so they can:

* classify data
* predict outcomes
* detect patterns
* automate decision-making

Machine Learning is widely used in:

* recommendation systems
* fraud detection
* chatbots
* self-driving cars
* healthcare
* cloud automation

---

# 📊 What This ML Script Does

## ✅ Loads the Iris Dataset

from sklearn.datasets import load_iris


The Iris dataset contains flower measurements and species labels.

The dataset contains:

   150 flower samples
   4 flower measurements (features)
   3 flower species:
      Setosa
      Versicolor
      Virginica

This dataset is commonly used for beginner Machine Learning projects and classification tasks.
---
## ✅ Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier

This is the Machine Learning algorithm used in the project.

What Random Forest Does
Creates multiple decision trees
Combines the results from all trees
Improves prediction accuracy

The final prediction is selected using majority voting from all decision trees.

Common Uses

Random Forest is commonly used for:

classification
prediction
data analysis

It is widely used because it provides accurate and reliable predictions.


## ✅ train_test_split

from sklearn.model_selection import train_test_split

This function splits the dataset into:

training data

testing data

Why Data Splitting is Important

✅ Training Data

Used to teach the Machine Learning model.

✅ Testing Data

Used to evaluate how well the model performs on unseen data.

This helps measure real-world prediction capability and avoids overfitting.

---

## ✅ accuracy_score

from sklearn.metrics import accuracy_score

This function calculates how accurate the model predictions are.

It compares:

actual values
predicted values

and calculates the prediction accuracy percentage.

Example:

Accuracy: 96.67%

This means the model predicted correctly for about 97 out of 100 samples.

---


# 🤖 Detailed Machine Learning Workflow

## 🔹 Step 1 — Load Dataset

```python id="v4g5lw"
data = load_iris()
X, y = data.data, data.target
```

### ✅ What Happens Here

### `load_iris()`

Loads the built-in Iris flower dataset into memory.

---

## ✅ `data.data`

Contains flower measurements such as:

* sepal length
* sepal width
* petal length
* petal width

Stored in variable:

```python id="mjlwmq"
X
```

`X` = input features

---

## ✅ `data.target`

Contains flower categories:

* setosa
* versicolor
* virginica

Stored in variable:

```python id="jbr7n4"
y
```

`y` = output labels

---

# 📊 Print Dataset Information

```python id="p6o8t5"
print(f'Dataset: {X.shape[0]} samples, {X.shape[1]} features')
```

## ✅ `X.shape`

Returns:

* number of rows
* number of columns

### Example Output

```text id="6x5l2s"
Dataset: 150 samples, 4 features
```

Meaning:

* 150 flower records
* 4 measurements per flower

---

# 🌸 Print Flower Classes

```python id="3tw5y9"
print(f'Classes: {data.target_names}')
```

### Example Output

```text id="u2p0vx"
Classes: ['setosa' 'versicolor' 'virginica']
```

These are the flower species the model will learn.

---

# 🔹 Step 2 — Split Training and Testing Data

```python id="s77d8f"
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

## ✅ Purpose

Machine Learning models must be tested using unseen data.

---

## ✅ `test_size=0.2`

Means:

* 80% data → training
* 20% data → testing

From 150 samples:

* 120 samples for training
* 30 samples for testing

---

## ✅ `random_state=42`

Ensures the data split remains the same every time the program runs.

Used for reproducibility.

---

# 🔹 Step 3 — Train the Machine Learning Model

```python id="92x6u2"
model = RandomForestClassifier(n_estimators=100, random_state=42)
```

Creates the Random Forest Machine Learning model.

---

## ✅ `n_estimators=100`

The model creates:

* 100 decision trees

More trees generally improve prediction quality and accuracy.

---

# 🧠 Train the Model

```python id="pbr9eh"
model.fit(X_train, y_train)
```

This is where actual Machine Learning happens.

The model:

* studies patterns
* learns relationships
* connects flower measurements to flower species

---

# ✅ Print Training Status

```python id="s34e6m"
print('Model trained!')
```

Confirms the training process completed successfully.

---

# 🔹 Step 4 — Evaluate the Model

## Predict Using Test Data

```python id="c42h83"
predictions = model.predict(X_test)
```

The model predicts flower species for testing samples.

---

# 🎯 Calculate Accuracy

```python id="nyw49m"
accuracy = accuracy_score(y_test, predictions)
```

Compares:

* actual answers
* predicted answers

and measures model accuracy.

---

# ✅ Print Accuracy

```python id="h3rz8v"
print(f'Accuracy: {accuracy:.2%}')
```

### Example Output

```text id="w5gg6o"
Accuracy: 96.67%
```

Meaning:

* the model predicted correctly about 97% of the time

---

# 🔹 Step 5 — Make Your Own Prediction

```python id="fjlwm8"
sample = [[5.1, 3.5, 1.4, 0.2]]
```

These values represent flower measurements:

* sepal length
* sepal width
* petal length
* petal width

---

# 🌸 Predict Flower Type

```python id="pht3j0"
result = model.predict(sample)
```

The model predicts the flower category based on the input values.

---

# ✅ Print Prediction Result

```python id="yep7rt"
print(f'Prediction for {sample[0]}: {data.target_names[result[0]]}')
```

### Example Output

```text id="2i4lm7"
Prediction for [5.1, 3.5, 1.4, 0.2]: setosa
```

The model predicts the flower species as:

✅ **Setosa**

---

# 🧠 Overall Workflow

```text id="4g1r7p"
Load Dataset
      ↓
Split Train/Test Data
      ↓
Create ML Model
      ↓
Train Model
      ↓
Test Accuracy
      ↓
Make Predictions
```

---

# 🚀 What You Learned

This single script teaches:

* dataset handling
* supervised learning
* model training
* prediction
* accuracy testing
* real Machine Learning workflow

---

# 🌟 Real-World Applications

These concepts are the foundation of:

* AI systems
* recommendation engines
* fraud detection
* predictive analytics
* automation systems
* smart applications


# ▶️ Run the Project

## Run Setup Script

```bash id="s5b7pv"
chmod +x scripts/setup.sh
./scripts/setup.sh
```

---

## Activate Virtual Environment

```bash id="qbz3d3"
source venv/bin/activate
```

---

## Run ML Script

```bash id="k8fw13"
python3 scripts/hello_ml.py
```

---

# ✅ Expected Output

```text id="3ihnh2"
Dataset: 150 samples, 4 features
Classes: ['setosa' 'versicolor' 'virginica']
Model trained!
Accuracy: 96.67%
Prediction for [5.1, 3.5, 1.4, 0.2]: setosa
```

---

# 📚 Key Learnings

* Linux command line usage
* Bash scripting automation
* Python virtual environments
* Dependency management
* Git & GitHub workflow
* Machine Learning basics
* Model training and prediction

---

# 👨‍💻 Author

Jothick Rishi

* GitHub: https://github.com/Jrishi123
* LinkedIn: https://www.linkedin.com/in/jothick-rishi-b05665176/
