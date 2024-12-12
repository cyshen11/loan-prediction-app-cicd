from components.logistic_regression import LogisticRegressionModel
import pandas as pd

class Predictor():
    def __init__(self, model_name):
        if model_name == "Logistic Regression":
            self.model = LogisticRegressionModel()
        else:
            raise ValueError(f"Model {model_name} not found")

    def prepare_data(self, loan_amount, loan_int_rate, annual_income, previous_loan_defaults):
        loan_percent_income = float(loan_amount) / float(annual_income)
        previous_loan_defaults_on_file_Yes = True if previous_loan_defaults == "Yes" else False
        previous_loan_defaults_on_file_No = True if previous_loan_defaults == "No" else False

        data = pd.DataFrame({
            'loan_percent_income': [loan_percent_income],
            'loan_int_rate': [loan_int_rate],
            'previous_loan_defaults_on_file_Yes': [previous_loan_defaults_on_file_Yes],
            'previous_loan_defaults_on_file_No': [previous_loan_defaults_on_file_No],
            'person_income': [annual_income]
        })
        return data

    def predict(self, X_test):
        pred = self.model.predict(X_test)

        if pred[0] == 1:
            return "Loan will be approved"
        else:
            return "Loan will not be approved"
