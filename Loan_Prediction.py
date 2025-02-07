import streamlit as st
import pandas as pd
import sqlite3
import pickle as pk
from datetime import datetime

def show():
    st.title('Loan_Prediction App')

    # Load model and scaler
    model = pk.load(open('model.pkl', 'rb'))
    scaler = pk.load(open('scaler.pkl', 'rb'))

    # Database connection
    conn = sqlite3.connect("loan_applications.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dob TEXT,
            gender TEXT,
            no_of_dependents INTEGER,
            education INTEGER,
            self_employed INTEGER,
            income_annum INTEGER,
            loan_amount INTEGER,
            loan_term INTEGER,
            cibil_score INTEGER,
            assets INTEGER,
            prediction TEXT,
            application_date TEXT
        )
    ''')
    conn.commit()

    # User Input
    name = st.text_input("Enter Your Name")
    dob = st.date_input("Select your Date of Birth")
    gender = st.radio("Select Gender", ("Male", "Female", "Other"))
    
    # **Replace sliders with number inputs**
    no_of_dep = st.number_input('Number of Dependents', min_value=0, max_value=5, step=1)
    grad = st.selectbox('Choose Education', ['Graduated', 'Not Graduated'])
    self_emp = st.selectbox('Self Employed?', ['Yes', 'No'])
    Annual_Income = st.number_input('Annual Income (₹)', min_value=0, max_value=10000000, step=10000)
    Loan_Amount = st.number_input('Loan Amount (₹)', min_value=0, max_value=10000000, step=10000)
    Loan_Dur = st.number_input('Loan Duration (Years)', min_value=0, max_value=20, step=1)
    Cibil = st.number_input('CIBIL Score', min_value=0, max_value=1000, step=1)
    Assets = st.number_input('Assets (₹)', min_value=0, max_value=10000000, step=10000)

    # Convert categorical values
    grad_s = 0 if grad == 'Graduated' else 1
    emp_s = 0 if self_emp == 'No' else 1

    if st.button("Predict"):
        pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets]],
                                columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 
                                         'loan_amount', 'loan_term', 'cibil_score', 'Assets'])
        pred_data = scaler.transform(pred_data)
        predict = model.predict(pred_data)

        # Determine Prediction Result
        result = "Approved" if predict[0] == 1 else "Rejected"
        st.markdown(f"### Loan Status: **{result}**")

        # Store in Database
        cursor.execute('''
            INSERT INTO loans (name, dob, gender, no_of_dependents, education, self_employed, income_annum, 
                               loan_amount, loan_term, cibil_score, assets, prediction, application_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, dob.strftime('%Y-%m-%d'), gender, no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Cibil, Assets, result, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
    
    if st.button("Show Loan Applications"):
        df = pd.read_sql("SELECT * FROM loans", conn)
        st.dataframe(df)

    conn.close()
