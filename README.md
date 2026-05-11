# employee deployment link:https://employee-rkygojrallgdn42ly6pvbf.streamlit.app/
# HR Attrition Prediction App

A Machine Learning web application built using Streamlit that predicts whether an employee will leave the company based on employee-related factors.

The project uses Logistic Regression and provides interactive visualizations for HR analytics.

---

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Pickle

---

# Dataset

Dataset File:

HR_comma_sep.csv

Target Column:
- left

Where:
- 0 = Employee Will Stay
- 1 = Employee Will Leave

---

# Features

✔ Predict employee attrition

✔ Shows probability of employee leaving

✔ Displays model accuracy

✔ Interactive user inputs

✔ Scatter Plot visualization

✔ Logistic Regression Curve visualization

---

# Project Structure

project_folder/
│
├── app.py
├── model.pkl
├── HR_comma_sep.csv
└── README.md

---

# Input Parameters

The application takes the following employee details:

- Satisfaction Level
- Last Evaluation
- Number of Projects
- Monthly Hours
- Years in Company

---

# Machine Learning Model

## Logistic Regression

Used for:
- Employee attrition prediction
- Binary classification

The trained model is loaded using:

pickle.load()

---

# Installation

## Step 1: Install Python

Download Python:
https://www.python.org/downloads/

---

## Step 2: Install Required Libraries

Run the following command:

pip install streamlit pandas numpy matplotlib scikit-learn

---

# Run the Application

Open terminal inside the project folder and run:

streamlit run app.py

---

# Application Workflow

1. User enters employee details
2. Clicks Predict button
3. Model predicts:
   - Employee Will Stay
   - Employee Will Leave
4. Probability percentage is displayed
5. Accuracy score is shown
6. Graphs are visualized

---

# Graphs Included

## 1. Scatter Plot

Displays:
- Satisfaction Level vs Employee Leaving

---

## 2. Logistic Regression Curve

Displays:
- Probability curve for employee attrition

---

# Accuracy Calculation

Accuracy is calculated using:

accuracy_score()

---

# Files Description

## app.py
Main Streamlit application file.

## model.pkl
Saved trained Logistic Regression model.

## HR_comma_sep.csv
Dataset used for training and testing.

---

# Future Improvements

- Add more HR parameters
- Improve UI design
- Add employee department selection
- Deploy application online
- Add feature importance graph

---

# Author

Developed using Python, Streamlit, and Machine Learning for HR Analytics practice.
