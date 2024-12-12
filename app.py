import streamlit as st
from components.logistic_regression import LogisticRegressionModel

def main():
    st.title("Loan Prediction App")

    st.sidebar.selectbox("Select a model", ["Logistic Regression"])
    # Load the model
    

if __name__ == "__main__":
    main()