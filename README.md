📌 Loan Approval Prediction using Streamlit
🔮 Loan Approval Prediction is a machine learning-based web application that helps users determine their loan eligibility. The app also includes:

📈 Financial News: Stay updated with the latest financial news.
💰 EMI Calculator: Calculate monthly EMI based on loan amount, interest rate, and tenure.
🚀 Features
✔️ Predict loan approval using Logistic Regression (Pickle Model)
✔️ Store loan applications in SQLite Database
✔️ Fetch real-time financial news
✔️ Calculate loan EMI with an EMI Calculator
✔️ Fully developed using Streamlit UI

🛠️ Tech Stack
Frontend: Streamlit
Machine Learning: Scikit-learn, Logistic Regression
Database: SQLite
APIs: News API for financial news
Deployment: Streamlit Sharing 
project structure
loan-approval-prediction/
│── test/                   
│   ├── loan_application.py   # Loan application processing  
│   ├── financial_news.py     # Fetch financial news  
│   ├── emi_calculator.py     # EMI calculation logic  
│── .env                      # Environment variables  
│── loan_application.db        # SQLite database file  
│── loan_approval_dataset.csv  # Dataset for training/testing  
│── model/                    
│   ├── loan_approval_pred_model.pkl  # Pickled Logistic Regression model  
│   ├── scaler.pkl                    # Pickled scaler for preprocessing  
│   ├── scan.py                        # Script for scanning and processing data  
 Installation Guide
1️⃣ Clone the Repository

git clone https://github.com/Nimal-0710/loan-approval-prediction.git
cd loan-approval-prediction

2️⃣ Set Up a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies

pip install -r requirements
📢 Additional Features
📈 Financial News
Fetches the latest finance-related news.
Uses the NewsAPI (or any free alternative).
Updates in real-time.
💰 EMI Calculator
Users enter loan amount, interest rate, and tenure.
Computes monthly EMI using the formula:
𝐸𝑀𝐼= 𝑃×𝑅×(1+𝑅)𝑁
      (1+𝑅)𝑁−1
where:
P = Loan Amount
R = Interest Rate (monthly)
N = Loan Tenure (months)

📡 Deployment Guide
Deploy Streamlit UI
Sign up on Streamlit Community Cloud (https://share.streamlit.io).
Create a new Streamlit app.
Connect your GitHub repository.
Select streamlit_app.py as the entry point.
Deploy and get the public UI URL.
🎯 Future Enhancements
✅ Improve UI with custom themes
✅ More detailed financial analytics

🤝 Contributing
Want to improve the project? Follow these steps:

Fork the repository.
Create a new branch:

git checkout -b feature-branch
Make your changes and commit:

git commit -m "Added a new feature"
Push and open a Pull Request:

git push origin feature-branch
📜 License
This project is licensed under the MIT License.

📞 Contact
🔗 GitHub: Nimal-0710
📧 Email: nrgnimal9@gmail.com

🎉 Enjoy Predicting Loan Approvals! 🚀

