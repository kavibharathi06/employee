# HR Attrition Prediction using Logistic Regression

## Project Overview

The HR Attrition Prediction App is a Machine Learning-based web application developed using Streamlit. The application predicts whether an employee is likely to leave the company based on employee-related parameters such as satisfaction level, evaluation score, working hours, and years of experience.

This project focuses on employee retention analysis and demonstrates the use of Logistic Regression for classification problems in Human Resource Analytics.

---

## Objectives

* To predict employee attrition.
* To analyze employee satisfaction and performance factors.
* To understand classification algorithms in Machine Learning.
* To develop an interactive HR analytics application.

---

## Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Programming Language      |
| Streamlit    | Web Application Framework |
| Pandas       | Data Processing           |
| NumPy        | Numerical Computation     |
| Matplotlib   | Data Visualization        |
| Scikit-learn | Machine Learning          |
| Pickle       | Model Serialization       |

---

## Dataset Information

The dataset contains employee information and attrition status.

### Dataset Columns

| Column Name          | Description                  |
| -------------------- | ---------------------------- |
| satisfaction_level   | Employee satisfaction score  |
| last_evaluation      | Performance evaluation score |
| number_project       | Number of projects handled   |
| average_montly_hours | Monthly working hours        |
| time_spend_company   | Years spent in company       |
| left                 | Attrition status             |

### Target Variable

* 1 → Employee Will Leave
* 0 → Employee Will Stay

---

## Machine Learning Model

### Logistic Regression

The project uses Logistic Regression for predicting employee attrition. The trained model is stored using Pickle and loaded during application runtime.

---

## Project Workflow

1. Load employee dataset.
2. Preprocess categorical variables using One-Hot Encoding.
3. Load the trained Machine Learning model.
4. Accept user inputs through Streamlit.
5. Predict employee attrition.
6. Display probability score and visualizations.

---

## Features

* Employee attrition prediction.
* Probability estimation.
* Interactive user inputs.
* Model accuracy display.
* Scatter Plot visualization.
* Logistic Regression Curve.

---

## Input Parameters

The application accepts the following employee details:

* Satisfaction Level
* Last Evaluation
* Number of Projects
* Monthly Working Hours
* Years in Company

---

## Data Visualizations

### Scatter Plot

Shows the relationship between employee satisfaction level and attrition.

### Logistic Regression Curve

Displays the probability of employee attrition based on satisfaction level.

---

## Model Evaluation

The performance of the model is evaluated using the `accuracy_score()` function.

---

## Project Structure

```bash
HR_Attrition_Project/
│
├── app.py
├── model.pkl
├── HR_comma_sep.csv
├── README.md
└── requirements.txt
```

---

## Installation

### Install Required Libraries

```bash
pip install streamlit pandas numpy matplotlib scikit-learn
```

### Run the Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Add more employee parameters.
* Improve user interface design.
* Deploy the application on cloud platforms.
* Add advanced analytics dashboards.

---

## Conclusion

This project demonstrates the practical application of Machine Learning in HR Analytics. It helps in understanding employee attrition prediction using Logistic Regression and provides experience in building interactive Machine Learning applications using Streamlit.
