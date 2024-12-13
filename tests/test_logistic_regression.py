"""test_logistic_regression.py"""

import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.logistic_regression import LogisticRegressionModel

def test_logistic_regression_init():
    model = LogisticRegressionModel()
    assert model is not None
