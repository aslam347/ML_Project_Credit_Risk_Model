# 🏦 Credit Risk Modelling App  
### AI-Powered Loan Risk Evaluation System  

An end-to-end Streamlit-based Machine Learning application that automates **credit risk assessment** for financial institutions.

This application is designed for **loan processing officers** to evaluate an applicant’s creditworthiness using data-driven risk scoring.

---

## 🌐 Live Demo

👉 https://mohamed-aslam-ml-project-credit-risk-model.streamlit.app/

---

## 📌 Project Overview

The Credit Risk Modelling App predicts the probability of loan default using applicant financial and credit behavior data.

It takes inputs such as:

- Applicant income  
- Loan amount  
- Loan type  
- Credit history (DPD, delinquency ratio)  
- Open loan accounts  
- Credit utilization ratio  

And returns:

- ✅ Risk prediction: Defaulter / Non-Defaulter  
- 📊 Credit Score: 300–900 scale  
- 🏷 Risk Tier Classification  
- 📈 Model-based explainability insights  

---

## 🚀 Features

- Simple and clean Streamlit UI  
- Predicts risk associated with the loan  
- Provides applicant’s credit score  
- Categorizes applicants into risk tiers:
  - **Poor:** 300–499  
  - **Average:** 500–649  
  - **Good:** 650–749  
  - **Excellent:** 750–900  
- Displays key financial insights like credit utilization ratio  
- AI explainability via Logistic Regression coefficients  
- Model performance tracking using:
  - AUC  
  - Gini  
  - KS Statistic  
  - Recall  

---

## 📥 Input Features

The model considers the following applicant attributes:

### 👤 Personal & Financial Information
- Applicant Age  
- Income  
- Loan Amount  
- Loan Tenure (months)  

### 📊 Credit Behaviour Metrics
- Average DPD (Days Past Due)  
- Delinquency Ratio  
- Credit Utilization Ratio  
- Open Loan Accounts  

### 🏠 Loan & Profile Attributes
- Residence Type  
- Loan Purpose  
- Loan Type  

---

## 🧠 Model Details

### Algorithms Used
- Logistic Regression (Primary Model)
- XGBoost Classifier (Comparative Model)

### Why Logistic Regression?
- Highly interpretable  
- Business-friendly explainability  
- Stable in financial risk modelling  

### Evaluation Metrics
- ROC-AUC  
- Gini Coefficient  
- KS Statistic  
- Recall  
- Accuracy  

---

## 📊 Example Prediction Logic

### ⚠ High Risk Applicant
If:
- High Loan-to-Income Ratio  
- High Delinquency Ratio  
- High Credit Utilization  

➡ Model predicts:
- Defaulter  
- Poor Credit Score  

### ✅ Low Risk Applicant
If:
- Low Loan-to-Income Ratio  
- Stable Income  
- Low Delinquency  

➡ Model predicts:
- Non-Defaulter  
- Excellent Credit Score  

---

## 🛠 Tech Stack

### Frontend
- Streamlit  

### Backend
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Joblib  
- XGBoost  

### Deployment
- Streamlit Cloud  
- Docker  
- AWS EC2 (ready for deployment)  

---

## 📁 Project Structure

```text
ML_Project_Credit_Risk_Model/
│
├── app/
│   ├── artifacts/
│   │   └── model_data.joblib
│   ├── main.py
│   └── prediction_helper.py
│
├── dataset/
│   ├── bureau_data.csv
│   ├── customers.csv
│   └── loans.csv
│
├── credit_risk_model_.ipynb
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## ▶ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aslam347/ML_Project_Credit_Risk_Model.git
cd ML_Project_Credit_Risk_Model
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app/main.py
```

---

## 🐳 Run with Docker

### 1️⃣ Build Docker Image

```bash
docker build -t credit-risk-model .
```

### 2️⃣ Run Docker Container

```bash
docker run -p 8501:8501 credit-risk-model
```

### 3️⃣ Open in Browser

```text
http://localhost:8501
```

---

## 🐳 Docker Hub

If the image is pushed to Docker Hub, pull and run it using:

```bash
docker pull mohamedaslam2001/credit-risk-model
docker run -p 8501:8501 mohamedaslam2001/credit-risk-model
```

---

## 💡 Key Highlights

- End-to-end ML pipeline integration  
- Business-friendly risk scoring  
- Production-style deployment  
- Model explainability for future enhancements  
- Designed for real-world loan underwriting use  

---

## 🔮 Future Enhancements

- SHAP-based explainability  
- Model monitoring dashboard  
- Bias & fairness detection  
- CI/CD pipeline integration  
- Cloud deployment with Docker + AWS  

---

## 👨‍💻 Author

**Mohamed Aslam M**  
AI Engineer | Data Science Enthusiast  
Python • Machine Learning • Responsible AI  

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
