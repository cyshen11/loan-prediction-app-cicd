import streamlit as st
from components.logistic_regression import LogisticRegressionModel

def main():
    st.title("Loan Prediction App")

    st.sidebar.selectbox("Select a model", ["Logistic Regression"])

    st.text_input("Enter the loan amount")
    st.text_input("Enter the loan interest rate", placeholder="0.05")
    st.text_input("Enter the annual income")
    st.selectbox("Previous loan defaults", ["No", "Yes"])
    # Load the model
    
if __name__ == "__main__":
    main()