
# 📰 Fake News Detection App

This is a simple Streamlit web app that predicts whether a given news statement is **real** or **fake** using a machine learning model trained on the LIAR dataset.

## 🚀 Features
- Input any news statement
- Cleans and preprocesses text
- Uses TF-IDF and a Logistic Regression model to classify as real or fake
- Interactive interface with Streamlit

## 📁 Files
- `app.py` – Streamlit app code
- `fake_news_model.pkl` – Trained Logistic Regression model
- `tfidf_vectorizer.pkl` – Fitted TF-IDF vectorizer
- `requirements.txt` – List of dependencies

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fake-news-detection-streamlit.git
   cd fake-news-detection-streamlit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## 🌐 Deployment

You can deploy this app for free using [Streamlit Cloud](https://share.streamlit.io):
- Upload your files to GitHub
- Connect your repo to Streamlit Cloud
- Set `app.py` as the entry point

## 📊 Model Info

Trained using Logistic Regression on the LIAR dataset.
- Text cleaned and vectorized using TF-IDF
- Binary classification: `real` vs `fake`

## ✍️ Author

Created by [Your Name]. Connect on [LinkedIn](https://linkedin.com).

