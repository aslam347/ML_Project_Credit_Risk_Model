from app.prediction_helper import predict


def test_predict_output():

    probability, credit_score, rating = predict(
        28,
        1200000,
        2560000,
        36,
        20,
        30,
        30,
        2,
        "Owned",
        "Education",
        "Unsecured"
    )

    assert isinstance(probability, float)
    assert isinstance(credit_score, int)
    assert isinstance(rating, str)

    assert 300 <= credit_score <= 900