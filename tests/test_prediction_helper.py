from app.prediction_helper import prepare_input


def test_prepare_input_shape():

    df = prepare_input(
        age=28,
        income=1200000,
        loan_amount=2560000,
        loan_tenure_months=36,
        avg_dpd_per_delinquency=20,
        delinquency_ratio=30,
        credit_utilization_ratio=30,
        num_open_accounts=2,
        residence_type="Owned",
        loan_purpose="Education",
        loan_type="Unsecured"
    )

    assert df.shape[0] == 1