import streamlit as st
import pandas as pd

def show():
    st.title("🏦 EMI Calculator for Banking")

    # Input Fields for Loan Details
    loan_amount = st.number_input("Enter Loan Amount (₹)", min_value=1000, step=1000)
    interest_rate = st.number_input("Enter Interest Rate (Annual in %)", min_value=1.0, step=0.1, format="%.2f")
    loan_term = st.number_input("Enter Loan Term (in Years)", min_value=1, step=1)
    
    # Processing Fee (Optional for Bank Calculation)
    processing_fee = st.number_input("Processing Fee (%)", min_value=0.0, max_value=5.0, step=0.1, format="%.2f")
    
    # EMI Calculation Button
    if st.button("Calculate EMI"):
        if loan_amount > 0 and interest_rate > 0 and loan_term > 0:
            # Convert annual interest rate to monthly rate
            monthly_interest_rate = (interest_rate / 100) / 12
            months = loan_term * 12

            # EMI Formula
            emi = (loan_amount * monthly_interest_rate) * ((1 + monthly_interest_rate) ** months) / (((1 + monthly_interest_rate) ** months) - 1)

            # Processing Fee Calculation
            total_processing_fee = (processing_fee / 100) * loan_amount
            total_payment = emi * months + total_processing_fee

            # Display EMI Result
            st.success(f"📢 Your EMI will be: ₹{emi:.2f} per month.")
            st.info(f"💰 Total Payment (including processing fee): ₹{total_payment:.2f}")

            # Generate Amortization Schedule
            remaining_balance = loan_amount
            amortization_data = []

            for month in range(1, months + 1):
                interest_payment = remaining_balance * monthly_interest_rate
                principal_payment = emi - interest_payment
                remaining_balance -= principal_payment
                amortization_data.append([month, emi, principal_payment, interest_payment, remaining_balance])

            # Convert to DataFrame and Display
            df = pd.DataFrame(amortization_data, columns=["Month", "EMI (₹)", "Principal Paid (₹)", "Interest Paid (₹)", "Remaining Balance (₹)"])
            st.write("📅 **Loan Amortization Schedule**")
            st.dataframe(df.style.format({"EMI (₹)": "₹{:.2f}", "Principal Paid (₹)": "₹{:.2f}", "Interest Paid (₹)": "₹{:.2f}", "Remaining Balance (₹)": "₹{:.2f}"}))

        else:
            st.warning("⚠️ Please enter valid loan details.")
