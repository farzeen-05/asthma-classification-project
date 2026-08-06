# 🫁 Asthma Severity Classification — ML Web App

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-MIT-yellow)

> A machine learning web app that classifies asthma severity levels based on a combination of patient symptoms/vitals and environmental risk factors.

🔗 **Live Demo:** [https://asthma-classification-project.onrender.com](https://asthma-classification-project.onrender.com/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Features Used](#features-used)
- [Model](#model)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Deployment](#deployment)

---

## Overview

Asthma severity assessment typically relies on a mix of clinical evaluation and environmental awareness. This project builds a multi-class classification pipeline that takes patient and environmental data as input and predicts the likely severity level, served through a simple Flask web interface for quick, accessible screening support.

**What it does:**
- Accepts patient and environmental inputs through a web form
- Runs a trained multi-class classification model
- Returns the predicted asthma severity level instantly
- Deployed as a live, publicly accessible web app

> **Note:** This tool is intended as an educational/screening-support project, not a diagnostic medical device.

---

## Architecture

```
User (Web Form)
      │
      ▼
Flask App (patient + environmental data submitted)
      │
      ▼
Preprocessing (feature encoding/scaling)
      │
      ▼
Trained Classification Model (scikit-learn)
      │
      ▼
Predicted Severity Level → rendered back to user
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask |
| Machine Learning | Scikit-learn (Logistic Regression / Random Forest / XGBoost) |
| Data Processing | Pandas, NumPy |
| Frontend | HTML, CSS |
| Deployment | Render |

---

## Features Used

The model predicts severity based on a mix of:

**Patient symptoms/vitals**
| Feature | Description |
|---------|-------------|
| Age | Patient age |
| Symptom frequency | Frequency/severity of breathing difficulty, wheezing, coughing |
| Vitals | Relevant clinical measurements (e.g. respiratory rate, oxygen levels) |

**Environmental factors**
| Feature | Description |
|---------|-------------|
| Air Quality Index | Local air pollution levels |
| Pollen Count | Seasonal allergen exposure |
| Other environmental triggers | e.g. humidity, temperature |

---

## Model

Multiple classification algorithms were evaluated using scikit-learn, including **Logistic Regression**, **Random Forest Classifier**, and **XGBoost Classifier**, with the best-performing model selected based on evaluation metrics (accuracy, F1-score, confusion matrix) across the severity classes.

**Pipeline steps:**
1. Data cleaning and handling of missing values
2. Feature encoding for categorical variables
3. Feature scaling for numeric inputs
4. Model training and hyperparameter tuning
5. Model evaluation and selection across severity classes
6. Serialization of the final model (`pickle`/`joblib`) for inference in the Flask app

---

## Project Structure

```
asthma-classification-project/
├── app.py                  # Flask application entry point
├── model/
│   └── model.pkl             # Trained classification model
├── templates/
│   └── index.html            # Web form UI
├── static/                 # CSS/JS assets
├── notebooks/               # EDA & model training notebooks
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- pip

### Local Setup

```bash
# Clone the repository
git clone https://github.com/farzeen-05/asthma-classification-project.git
cd asthma-classification-project

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Deployment

Deployed on **Render**, serving the Flask app directly with the pre-trained model bundled into the deployment — lightweight and easy to host on a free tier, with no external database or GPU required.

---

## Author

**Farzeen Abdul Khadir**
ECE Graduate | ML & Full-Stack Developer | MLOps & Cloud

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?logo=linkedin)](https://www.linkedin.com/in/farzeen-abdul-khadir-8921ba2a1)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github)](https://github.com/farzeen-05)
[![Email](https://img.shields.io/badge/Email-farzeen99453@gmail.com-EA4335?style=flat&logo=gmail)](mailto:farzeen99453@gmail.com)

---

## License

This project is licensed under the MIT License.
