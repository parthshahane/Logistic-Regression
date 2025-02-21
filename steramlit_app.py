import streamlit as st
def main():
    st.title("Titanic Survival Prediction")
    st.write("Enter passenger details to predict survival.")
    
    # User inputs
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.radio("Sex", ["Male", "Female"])
    age = st.slider("Age", 1, 100, 25)
    sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
    parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
    fare = st.number_input("Fare", 0.0, 500.0, 50.0)
    embarked = st.selectbox("Embarked Port", ["C", "Q", "S"])
    if st.button("Predict Survival"):
        user_data = pd.DataFrame([[pclass, 1 if sex == "Male" else 0, age, sibsp, parch, fare,
                                   1 if embarked == "Q" else 0, 1 if embarked == "S" else 0]],
                                 columns=X.columns)
        user_data = scaler.transform(user_data)
        prediction = model.predict(user_data)
        st.write("Survived" if prediction[0] == 1 else "Did Not Survive")

if __name__ == "__main__":
    main()
