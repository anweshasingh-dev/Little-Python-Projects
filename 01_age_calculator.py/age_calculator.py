import streamlit as st
st.title("Age Calculator")
from datetime import date
today = date.today()

centuary_ago = date(1900, 1, 1)
default_dob = date(2000, 1, 1)

dob = st.date_input("Enter your date of birth:", 
    value=default_dob, 
    min_value=centuary_ago, 
    max_value=today)


st.write("Today's date is:", today)


if st.button("Calculate Age"):
    age = today.year - dob.year
    # If the current month/day is before the birth month/day, this subtracts 1.
    # Otherwise, it subtracts 0.
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    st.success(f"You are {age} years old! 🎉")
