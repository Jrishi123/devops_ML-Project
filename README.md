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

```python id="l9ov0m"
load_iris()
```

The Iris dataset contains flower measurements and species labels.

---

## ✅ Splits Data into Training and Testing Sets

```python id="t4qlzz"
train_test_split()
```

* Training data is used to teach the model
* Testing data is used to evaluate accuracy

---

## ✅ Trains a Random Forest Model

```python id="lc1zqa"
RandomForestClassifier()
```

The model learns patterns from flower measurements.

---

## ✅ Evaluates Model Accuracy

```python id="qjgdj0"
accuracy_score()
```

Checks how accurately the model predicts flower species.

---

## ✅ Makes Predictions

```python id="v94l4n"
model.predict()
```

Predicts the flower species from sample input values.

---

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
