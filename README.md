# 🚀 DevOps ML Project with MLflow — Complete Detailed Guide

## 📌 Introduction

This project demonstrates how Machine Learning and DevOps practices work together using MLOps (Machine Learning Operations).

The project trains Machine Learning models using the Iris Dataset and tracks experiments using MLflow.

This project is useful for understanding:

* Machine Learning workflow
* Experiment tracking
* Model versioning
* Metrics logging
* Artifact storage
* CI/CD for ML projects
* Docker containerization
* Production-ready MLOps concepts

---

# 🧠 What is MLOps?

MLOps stands for:

```text id="9d2e89"
Machine Learning + DevOps = MLOps
```

It is the process of automating and managing the complete lifecycle of Machine Learning models.

MLOps helps teams:

* train models efficiently
* track experiments
* deploy models
* monitor performance
* retrain models automatically

---

# 🎯 Goal of This Project

The main goal of this project is to:

✅ Train multiple ML models
✅ Compare model performance
✅ Track experiments using MLflow
✅ Store metrics and artifacts
✅ Create a reusable ML workflow
✅ Prepare for deployment and CI/CD integration

---

# 📚 Dataset Used — Iris Dataset

The project uses the famous Iris Flower Dataset from Scikit-learn.

The dataset contains:

| Feature      | Meaning                |
| ------------ | ---------------------- |
| Sepal Length | Length of flower sepal |
| Sepal Width  | Width of flower sepal  |
| Petal Length | Length of flower petal |
| Petal Width  | Width of flower petal  |

Target classes:

* Setosa
* Versicolor
* Virginica

---

# 🏗️ Project Architecture

```text id="ayp2hf"
User → Training Script → MLflow Tracking → Metrics & Models Storage → MLflow UI
```

Explanation:

1. User runs the training script
2. Models are trained
3. MLflow records experiments
4. Metrics and models are stored
5. MLflow UI displays results visually

---

# 📂 Project Structure

```bash id="r12x3f"
devops-ml-project/
│
├── phase5-mlops/
│   │
│   ├── experiments/
│   │   ├── train.py
│   │   ├── report.json
│   │   ├── requirements.txt
│   │   └── mlruns/
│   │
│   ├── mlflow.db
│   ├── artifacts/
│   └── README.md
│
├── .github/
│   └── workflows/
│       └── mlflow-ci.yml
│
└── Dockerfile
```

---

# 📖 File Explanation

---

## 1️⃣ train.py

This is the main Machine Learning training script.

Responsibilities:

* load dataset
* split data
* train models
* evaluate performance
* log metrics using MLflow
* save trained models

---

## 2️⃣ requirements.txt

Contains all required Python packages.

Example:

```txt id="dyj4fh"
mlflow
scikit-learn
numpy
pandas
```

Purpose:

* ensures reproducible environments
* simplifies dependency installation

Install using:

```bash id="6csdfr"
pip install -r requirements.txt
```

---

## 3️⃣ mlruns/

This folder is automatically created by MLflow.

It stores:

* experiment data
* metrics
* parameters
* artifacts
* model files

Think of it as the database/storage for MLflow.

---

## 4️⃣ report.json

Stores the classification report.

Contains:

* precision
* recall
* f1-score
* support

Useful for:

* performance analysis
* debugging
* model comparison

---

# ⚙️ Technologies Used

| Technology     | Purpose                  |
| -------------- | ------------------------ |
| Python         | Programming Language     |
| Scikit-learn   | Machine Learning library |
| MLflow         | Experiment tracking      |
| NumPy          | Numerical operations     |
| Docker         | Containerization         |
| GitHub Actions | CI/CD automation         |

---

# 🐍 Virtual Environment Setup

## Why Virtual Environment?

A virtual environment isolates project dependencies.

Benefits:

* avoids package conflicts
* cleaner development
* reproducible setup

---

## Create Virtual Environment

### macOS/Linux

```bash id="e31bxf"
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash id="1f6gk5"
python -m venv venv
venv\Scripts\activate
```

---

# 📥 Install Dependencies

```bash id="s6m0o8"
pip install -r requirements.txt
```

Meaning:

* downloads required libraries
* prepares environment for execution

---

# 🧠 Machine Learning Workflow

---

## Step 1 — Load Dataset

```python id="ms7u4z"
from sklearn.datasets import load_iris

data = load_iris()
```

Meaning:

* loads built-in Iris dataset
* returns features and target labels

---

## Step 2 — Split Dataset

```python id="m2vqkh"
train_test_split(X, y, test_size=0.2)
```

Meaning:

* 80% data used for training
* 20% data used for testing

Purpose:

* prevents overfitting
* evaluates model performance

---

## Step 3 — Train Model

Example:

```python id="l85pnx"
RandomForestClassifier()
```

Meaning:

* ensemble ML algorithm
* uses multiple decision trees
* improves prediction accuracy

---

# 📊 Model Evaluation

The project measures:

| Metric   | Meaning                        |
| -------- | ------------------------------ |
| Accuracy | Correct predictions percentage |
| CV Mean  | Average cross-validation score |
| CV Std   | Stability of model performance |

---

# 🔄 Cross Validation

```python id="71dh3e"
cross_val_score(model, X, y, cv=5)
```

Meaning:

* dataset split into 5 parts
* model trained/tested multiple times
* provides reliable evaluation

Benefits:

* reduces bias
* improves confidence in results

---

# 🚀 MLflow Integration

---

# What is MLflow?

MLflow is an open-source platform for managing ML lifecycle.

Features:

* experiment tracking
* model logging
* artifact management
* model registry

---

# MLflow Tracking URI

```python id="m9y9d8"
mlflow.set_tracking_uri("file:./mlruns")
```

Meaning:

* stores experiments locally
* avoids server dependency

---

# Create Experiment

```python id="bxjlwm"
mlflow.set_experiment("iris-classification")
```

Meaning:

* groups related model runs
* organizes experiments

---

# Log Parameters

```python id="fokn0k"
mlflow.log_params(params)
```

Stores:

* hyperparameters
* model configuration

Example:

* number of trees
* max depth

---

# Log Metrics

```python id="0ik0pf"
mlflow.log_metric("accuracy", accuracy)
```

Stores:

* model performance metrics

Useful for:

* comparison
* monitoring
* optimization

---

# Log Artifacts

```python id="8oxt2l"
mlflow.log_artifact("report.json")
```

Artifacts include:

* reports
* datasets
* images
* trained models

---

# Log Model

```python id="btjlwm"
mlflow.sklearn.log_model(model, name="model")
```

Meaning:

* saves trained ML model
* enables future deployment

---

# ▶️ Run Training

```bash id="m79vjs"
python3 train.py
```

Expected output:

```text id="rj6aq0"
random-forest-100: accuracy=1.0000
gradient-boosting: accuracy=1.0000
```

---

# 📈 Launch MLflow UI

```bash id="0x0x0n"
mlflow ui
```

Open browser:

```text id="tn6k7x"
http://127.0.0.1:5000
```

---

# 📊 What You See in MLflow UI

MLflow UI displays:

✅ Experiment runs
✅ Accuracy metrics
✅ Parameters
✅ Artifacts
✅ Saved models
✅ Run comparison

This helps teams analyze and improve ML models efficiently.

---

# 🐳 Docker Integration

---

# Why Docker?

Docker packages the application with all dependencies.

Benefits:

* portability
* reproducibility
* easier deployment

---

# Build Docker Image

```bash id="f76m0y"
docker build -t iris-mlflow .
```

Meaning:

* creates portable application image

---

# Run Docker Container

```bash id="5k7jqv"
docker run -p 5000:5000 iris-mlflow
```

Meaning:

* starts application inside isolated container

---

# 🔄 CI/CD Integration

---

# What is CI/CD?

CI/CD means:

| Term | Meaning                        |
| ---- | ------------------------------ |
| CI   | Continuous Integration         |
| CD   | Continuous Delivery/Deployment |

---

# Why Use CI/CD for ML?

Benefits:

* automated testing
* automated training
* reproducible pipelines
* faster development

---

# GitHub Actions Workflow

Workflow automates:

* dependency installation
* training execution
* validation
* testing

---

# 🛠️ Common Errors and Fixes

---

## Error: Connection Refused

Cause:

* MLflow server not running

Fix:

```python id="rc0d6u"
mlflow.set_tracking_uri("file:./mlruns")
```

---

## Error: Port Already in Use

Fix:

```bash id="xtixxx"
mlflow ui --port 5001
```

---

## Error: ModuleNotFoundError

Fix:

```bash id="r4fjlwm"
pip install mlflow
```

---

# 🌟 Future Enhancements

Possible improvements:

* Kubernetes deployment
* FastAPI prediction API
* AWS SageMaker integration
* Azure ML integration
* Model monitoring
* Auto retraining pipelines
* Prometheus/Grafana monitoring

---

# 👨‍💻 Author

Jothick Rishi

GitHub:
[Jrishi123 GitHub](https://github.com/Jrishi123?utm_source=chatgpt.com)

LinkedIn:
[Jothick Rishi LinkedIn](https://www.linkedin.com/in/jothick-rishi-b05665176/?utm_source=chatgpt.com)

---

# 🎯 Final Conclusion

This project demonstrates a real-world beginner-to-intermediate MLOps workflow.

You learned:

* Machine Learning fundamentals
* Experiment tracking
* MLflow usage
* Model logging
* Docker integration
* CI/CD concepts
* MLOps best practices

This project is highly valuable for:

* DevOps Engineers
* Cloud Engineers
* MLOps Engineers
* Machine Learning Engineers

It serves as an excellent portfolio project showcasing both ML and DevOps skills together 🚀
