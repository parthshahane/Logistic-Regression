import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler

# Load trained model
with open("logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load dataset for preprocessing
df_train = pd.read_csv("/mnt/data/Titanic_train.csv")
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

# Standardization
scaler = StandardScaler()
scaler.fit(df_train[features])

# Streamlit UI
st.title("Titanic Survival Prediction")
st.write("Enter passenger details to predict survival")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ['Male', 'Female'])
age = st.number_input("Age", min_value=0, max_value=100, value=30)
sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=30.0)
embarked = st.selectbox("Embarked", ['C', 'Q', 'S'])

# Encode categorical variables
sex = 1 if sex == 'Male' else 0
embarked = {'C': 0, 'Q': 1, 'S': 2}[embarked]

# Ensure the correct number of features
user_input = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, embarked]], columns=features)

# Standardize the input data
user_input = scaler.transform(user_input)

# Prediction
if st.button("Predict Survival"):
    prediction = model.predict(user_input)
    result = "Survived" if prediction[0] == 1 else "Did not survive"
    st.write("Prediction:", result)
