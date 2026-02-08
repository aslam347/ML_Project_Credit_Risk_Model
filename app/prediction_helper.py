import joblib
import numpy as np
import pandas as pd
import os

# Correct model path for Streamlit Cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "model_data.joblib")

# Load model components
model_data = joblib.load(MODEL_PATH)
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']
cols_to_scale = model_data['cols_to_scale']


def prepare_input(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                  delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                  residence_type, loan_purpose, loan_type):

    input_data = {
        'age': age,
        'loan_tenure_months': loan_tenure_months,
        'number_of_open_accounts': num_open_accounts,
        'credit_utilization_ratio': credit_utilization_ratio,
        'loan_to_income': loan_amount / income if income > 0 else 0,
        'delinquency_ratio': delinquency_ratio,
        'avg_dpd_per_delinquency': avg_dpd_per_delinquency,
        'residence_type_Owned': 1 if residence_type == 'Owned' else 0,
        'residence_type_Rented': 1 if residence_type == 'Rented' else 0,
        'loan_purpose_Education': 1 if loan_purpose == 'Education' else 0,
        'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
        'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0,
        'loan_type_Unsecured': 1 if loan_type == 'Unsecured' else 0,
    }

    df = pd.DataFrame([input_data])

    # 🔥 STEP 1 — match EXACT scaler columns
    all_scaler_cols = scaler.feature_names_in_

    for col in all_scaler_cols:
        if col not in df.columns:
            df[col] = 0

    # Keep only scaler columns for transform
    df_scaled_part = df[all_scaler_cols]
    df_scaled_part = pd.DataFrame(
        scaler.transform(df_scaled_part),
        columns=all_scaler_cols
    )

    # 🔥 STEP 2 — Now match model feature columns
    for col in features:
        if col not in df_scaled_part.columns:
            df_scaled_part[col] = 0

    df_final = df_scaled_part[features]

    return df_final



def calculate_credit_score(input_df, base_score=300, scale_length=600):
    x = np.dot(input_df.values, model.coef_.T) + model.intercept_
    default_probability = 1 / (1 + np.exp(-x))
    non_default_probability = 1 - default_probability
    credit_score = base_score + non_default_probability.flatten() * scale_length

    score = credit_score[0]
    if score < 500:
        rating = "Poor"
    elif score < 650:
        rating = "Average"
    elif score < 750:
        rating = "Good"
    else:
        rating = "Excellent"

    return float(default_probability.flatten()[0]), int(score), rating


def predict(*args):
    input_df = prepare_input(*args)
    return calculate_credit_score(input_df)
