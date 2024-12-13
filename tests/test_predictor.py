"""test_predictor.py"""

import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.predictor import Predictor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def test_valid_model_name():
    predictor = Predictor("Logistic Regression")
    assert isinstance(predictor.model, LogisticRegression)

    predictor = Predictor("Random Forest")
    assert isinstance(predictor.model, RandomForestClassifier)

def test_invalid_model_name():
    with pytest.raises(ValueError) as exc_info:
        Predictor("Invalid Model Name")

def test_prepare_data():
    predictor = Predictor("Logistic Regression")
    data = predictor.prepare_data(10000, 0.05, 100000, "Yes")
    assert data.shape == (1, 5)
    assert data.columns.tolist() == ['loan_percent_income', 'loan_int_rate', 'previous_loan_defaults_on_file_Yes', 'previous_loan_defaults_on_file_No', 'person_income']
    assert data.values.tolist() == [[0.1, 0.05, True, False, 100000]]

def test_predict_loan_not_approved():
    predictor = Predictor("Logistic Regression")
    X_test = predictor.prepare_data(8, 6.04, 100, "No")
    assert predictor.predict(X_test) == "Loan will not be approved"

def test_predict_loan_approved():
    predictor = Predictor("Logistic Regression")
    X_test = predictor.prepare_data(13, 14.88, 100, "No")
    assert predictor.predict(X_test) == "Loan will be approved"



