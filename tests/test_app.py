"""test_app.py"""

from streamlit.testing.v1 import AppTest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_main_load():
    at = AppTest.from_file("app.py")
    at.run()
    
    assert "Loan Prediction App" in at.title[0].value
    
    assert at.sidebar.selectbox("model_name").value == "Logistic Regression"
    assert at.sidebar.selectbox("model_name").index == 0
    at.sidebar.selectbox("model_name").set_value("Logistic Regression").run()

    assert at.text_input("loan_amount").value == ""
    at.text_input("loan_amount").set_value("10000").run()

    assert at.text_input("loan_int_rate").value == ""
    at.text_input("loan_int_rate").set_value("0.05").run()

    assert at.text_input("annual_income").value == ""
    at.text_input("annual_income").set_value("100000").run()

    assert at.selectbox("previous_loan_defaults").value == "No"
    at.selectbox("previous_loan_defaults").set_value("Yes").run()

    assert at.button("predict_button").value == False