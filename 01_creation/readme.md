# Streamlit Age Calculator

A lightweight, interactive web application built with Streamlit that calculates a user's exact age based on their Date of Birth (DOB).

---

## Approach & Logic

Instead of dealing with tedious string manipulations or complex date formatting, this application utilizes Python's native `datetime` library paired with Streamlit's frontend widgets.

### 1. Smart Date Constraints

To provide a clean user experience, the `st.date_input` widget is configured with specific boundary constraints:

- **Default Value:** January 1, 2000 (`default_dob`)
- **Minimum Value:** January 1, 1900 (`centuary_ago`) — _Ensures a wide historical range for older generations._
- **Maximum Value:** Current Date (`today`) — _Prevents users from selecting a birth date in the future._

### 2. Core Algorithm (Pseudocode)

The application avoids simple year subtraction (which can cause off-by-one errors depending on the current month) by using a tuple comparison:

```python
# Calculate the baseline year difference
age = today.year - dob.year

# If the current month/day falls before the birth month/day,
# the evaluation returns True (1), subtracting 1 from the age.
# Otherwise, it evaluates to False (0), keeping the baseline age.
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

st.success(f"You are {age} years old! 🎉")
```
