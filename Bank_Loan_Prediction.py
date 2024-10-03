import streamlit as st
import pickle
import os

# Load model
try:
    model = pickle.load(open('C:/Users/mubar/Downloads/Streamlit_Bank_Loan_Prediction-master/Streamlit_Bank_Loan_Prediction-master/Model/ML_Model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please check the path to 'ML_Model.pkl'.")

def run():

    st.title("Loan Prediction using Machine Learning")

    ## Account No
    account_no = st.text_input('Account number')

    ## Full Name
    fn = st.text_input('Full Name')

    ## For gender
    gen_display = ('Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependents
    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x])

    ## For education
    edu_display = ('Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

    ## For employment status
    emp_display = ('Job', 'Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('Rural', 'Semi-Urban', 'Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

    ## For Credit Score
    cred_display = ('Between 300 to 500', 'Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)

    ## Loan Amount
    loan_amt = st.number_input("Loan Amount", value=0)

    ## Loan duration
    dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        # Map loan duration to the number of days
        duration = 0
        if dur == 0:
            duration = 60
        elif dur == 1:
            duration = 180
        elif dur == 2:
            duration = 240
        elif dur == 3:
            duration = 360
        elif dur == 4:
            duration = 480

        # Prepare feature array for prediction
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        st.write("Input Features: ", features)

        # Prediction using the model
        try:
            prediction = model.predict(features)
            ans = int(prediction[0])

            if ans == 0:
                st.error(
                    f"Hello {fn} || Account number: {account_no} || According to our calculations, you will not get the loan from the bank."
                )
            else:
                st.success(
                    f"Hello {fn} || Account number: {account_no} || Congratulations!! You will get the loan from the bank."
                )
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

run()
