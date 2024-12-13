"""test_predictor.py"""

import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.predictor import Predictor
from components.logistic_regression import LogisticRegressionModel

def test_valid_model_name():
    predictor = Predictor("Logistic Regression")
    assert isinstance(predictor.model, LogisticRegressionModel)

def test_invalid_model_name():
    with pytest.raises(ValueError) as exc_info:
        Predictor("Invalid Model Name")