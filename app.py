
import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

st.title("📰 Fake News Detection App")
st.write("Enter a news statement to check if it's real or fake.")

user_input = st.text_area("News Statement", "")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        clean_input = clean_text(user_input)
        vectorized_input = vectorizer.transform([clean_input])
        prediction = model.predict(vectorized_input)[0]
        st.success(f"The statement is predicted to be **{prediction.upper()}**.")
