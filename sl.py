import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title
st.title("Salary Prediction System")

# Dataset
data = {
    "experience": [1, 2, 3, 4, 5, 3, 3],
    "skills":     [2, 4, 5, 7, 8, 9, 1],
    "salary":     [20000, 35000, 50000, 65000, 80000, 70000, 40000]
}

df = pd.DataFrame(data)

# Train Model
X = df[["experience", "skills"]]
y = df["salary"]

model = LinearRegression()
model.fit(X, y)

# User Input
exp = st.slider("Years of Experience", 0, 10, 1)
skills = st.slider("Skill Level (1-10)", 1, 10, 5)

# Prediction Button
if st.button("Predict Salary"):
    input_data = pd.DataFrame([[exp, skills]], columns=["experience", "skills"])
    prediction = model.predict(input_data)

    st.success(f" Predicted Salary: ₹ {int(prediction[0])}")