# pip install streamlit scikit-learn
import streamlit as st
import pickle

# 1. Load your saved model (and your vectorizer!)
model = pickle.load(open('trained_model.sav', 'rb'))
# vectorizer = pickle.load(open('vectorizer.sav', 'rb'))

# 2. Build the website UI
st.title("Twitter Sentiment Analyzer")
st.write("Enter a tweet below to see if it's positive or negative!")

user_input = st.text_input("Tweet:")

# 3. Create the prediction button
if st.button("Predict"):
    if user_input:
        # Transform the user's text into numbers using your saved vectorizer
        vectorized_input = vectorizer.transform([user_input])

        # Feed the numbers into your saved model
        prediction = model.predict(vectorized_input)

        # Display the result (assuming 1 is positive and 0 is negative)
        if prediction[0] == 1:
            st.success("Positive tweet! 😊")
        else:
            st.error("Negative tweet! 😔")
