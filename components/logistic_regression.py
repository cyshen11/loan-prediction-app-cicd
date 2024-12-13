import pickle
from joblib import load

class LogisticRegressionModel:
    def __init__(self):
        self.model = load('models/lr_model.joblib')

    def predict(self, X_test):
        return self.model.predict(X_test)