import streamlit as st
from components.predictor import Predictor

def main():
    st.title("Loan Prediction App")

    model_name = st.sidebar.selectbox("Select a model", ["Logistic Regression"])

    loan_amount = st.text_input("Enter the loan amount")
    loan_int_rate = st.text_input("Enter the loan interest rate", placeholder="0.05")
    annual_income = st.text_input("Enter the annual income")
    previous_loan_defaults = st.selectbox("Previous loan defaults", ["No", "Yes"])
    
    if st.button("Predict"):
        predictor = Predictor(model_name)
        data = predictor.prepare_data(loan_amount, loan_int_rate, annual_income, previous_loan_defaults)
        prediction = predictor.predict(data)
        st.write(prediction)
    
if __name__ == "__main__":
    main()