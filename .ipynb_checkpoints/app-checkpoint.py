import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("HR Attrition Prediction")

# Inputs
satisfaction = st.slider(
    "Satisfaction Level",
    0.0,
    1.0,
    0.5
)

evaluation = st.slider(
    "Last Evaluation",
    0.0,
    1.0,
    0.5
)

projects = st.number_input(
    "Number of Projects",
    1,
    10,
    3
)

hours = st.number_input(
    "Monthly Hours",
    50,
    400,
    160
)

years = st.number_input(
    "Years in Company",
    1,
    20,
    3
)

# Prediction Button
if st.button("Predict"):

    sample = np.array([[
        satisfaction,
        evaluation,
        projects,
        hours,
        years,
        0,
        0,
        0,0,0,0,0,0,0,0,0,
        1,0
    ]])

    prediction = model.predict(sample)

    probability = model.predict_proba(sample)

    if prediction[0] == 1:
        st.error("Employee Will Leave")
    else:
        st.success("Employee Will Stay")

    st.write(
        "Probability of Leaving:",
        round(probability[0][1] * 100,2),
        "%"
    )