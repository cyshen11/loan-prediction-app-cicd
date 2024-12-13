"""test_predictor.py"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.predictor import Predictor
from components.logistic_regression import LogisticRegressionModel

def test_valid_model_name():
    predictor = Predictor("Logistic Regression")
    assert isinstance(predictor.model, LogisticRegressionModel)
