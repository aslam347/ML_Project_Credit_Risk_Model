# 🏦 Credit Risk Modelling System  
### AI-Powered Loan Risk Assessment Platform

An end-to-end Machine Learning application that predicts loan default probability and evaluates applicant creditworthiness using financial and behavioral data.

Built with:
- Machine Learning
- Streamlit
- Docker
- AWS EC2
- Amazon ECR
- GitHub Actions CI/CD

---

# 🌐 Live Demo

## 🚀 Streamlit Cloud
👉 https://mohamed-aslam-ml-project-credit-risk-model.streamlit.app/

---

# 📌 Project Overview

This project simulates a real-world credit risk evaluation system used in financial institutions for loan underwriting and applicant risk analysis.

The application predicts:
- ✅ Default Probability
- 📊 Credit Score (300–900)
- 🏷 Risk Tier Classification

The system uses applicant financial and credit behavior data such as:
- Income
- Loan Amount
- Credit Utilization
- Delinquency Ratio
- Loan Type
- Open Loan Accounts

---

# 🚀 Key Features

- Credit Risk Prediction
- Credit Score Generation
- Risk Tier Classification
- Streamlit Interactive UI
- Explainable ML Model
- Dockerized Deployment
- AWS EC2 Deployment
- Amazon ECR Integration
- GitHub Actions CI/CD Pipeline
- Automated Testing using Pytest

---

# 🧠 Machine Learning Models

## Primary Model
- Logistic Regression

## Comparative Model
- XGBoost Classifier

---

# 📊 Evaluation Metrics

- ROC-AUC
- Gini Coefficient
- KS Statistic
- Recall
- Accuracy

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

## Cloud & DevOps
- Docker
- AWS EC2
- Amazon ECR
- GitHub Actions
- CI/CD Pipeline

## Testing
- Pytest

---

# ☁ CI/CD Workflow

```text
Developer Push
      ↓
GitHub Actions
      ↓
Run Pytest
      ↓
Build Docker Image
      ↓
Push to Amazon ECR
      ↓
Deploy to AWS EC2
```

---

# 📁 Project Structure

```text
ML_Project_Credit_Risk_Model/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app/
│   ├── artifacts/
│   ├── main.py
│   └── prediction_helper.py
│
├── dataset/
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ▶ Run Locally

## Clone Repository

```bash
git clone https://github.com/aslam347/ML_Project_Credit_Risk_Model.git
cd ML_Project_Credit_Risk_Model
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app/main.py
```

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t credit-risk-model .
```

## Run Docker Container

```bash
docker run -p 8501:8501 credit-risk-model
```

---

# ☁ AWS Deployment

This project is deployed using:
- AWS EC2
- Amazon ECR
- Docker
- GitHub Actions CI/CD

---

# 📈 Business Use Cases

- Loan Default Prediction
- Credit Scoring
- Risk Analytics
- Automated Underwriting
- Financial Risk Assessment

---

# 🔮 Future Enhancements

- SHAP Explainability
- Kubernetes Deployment
- Monitoring Dashboard
- MLflow Integration
- Bias Detection

---

# 👨‍💻 Author

## Mohamed Aslam M

AI/ML Engineer | Backend Developer | MLOps Enthusiast

### Skills
- Python
- Machine Learning
- AWS
- Docker
- CI/CD
- GitHub Actions

---

# ⭐ Project Highlights

✅ End-to-End ML Pipeline  
✅ Production-Style Deployment  
✅ Dockerized Application  
✅ Cloud Deployment using AWS  
✅ Automated CI/CD Workflow  
✅ Real-World Financial AI Use Case  

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
