"""test_logistic_regression.py"""

import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from components.logistic_regression import LogisticRegressionModel

def test_logistic_regression_init():
    model = LogisticRegressionModel()
    assert model is not None

def test_predict_loan_not_approved():
    model = LogisticRegressionModel()
    X_test = pd.DataFrame({
        'loan_percent_income': [0.08],
        'loan_int_rate': [6.04],
        'previous_loan_defaults_on_file_Yes': [False],
        'previous_loan_defaults_on_file_No': [True],
        'person_income': [96865.0]
    })
    assert model.predict(X_test) == 0

def test_predict_loan_approved():
    model = LogisticRegressionModel()
    X_test = pd.DataFrame({
        'loan_percent_income': [0.13],
        'loan_int_rate': [14.88],
        'previous_loan_defaults_on_file_Yes': [False],
        'previous_loan_defaults_on_file_No': [True],
        'person_income': [37298.0]
    })
    assert model.predict(X_test) == 1
