import sys
import streamlit as st 
import test.Loan_Prediction
import test.Financial_News
import test.emi_calculator

# Set Streamlit page config
st.set_page_config(page_title="Loan Prediction App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ["🏦 Loan Prediction", "📰 Financial News", "📊 EMI Calculator"])

# Redirect to the selected page
if selected_page == "🏦 Loan Prediction":
    test.Loan_Prediction.show()

elif selected_page == "📰 Financial News":
    test.Financial_News.show()

elif selected_page == "📊 EMI Calculator":
    test.emi_calculator.show()
