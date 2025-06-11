
# 📰 Fake News Detection using NLP & Machine Learning

This project is a Fake News Detection system built using the **LIAR dataset**. It applies **Natural Language Processing (NLP)** and **machine learning** techniques to classify short political statements as either **real** or **fake**. The app is deployed via **Streamlit** to allow users to test the model with their own input.

## 🚀 Demo

👉 Try it live : [[Streamlit App URL](https://fake-news-detection-69esj4uppayjusnynwazfz.streamlit.app/)]

## 📦 Project Structure

```
├── app.py                   # Streamlit app file
├── fake_news_model.pkl      # Trained Logistic Regression model
├── tfidf_vectorizer.pkl     # TF-IDF vectorizer used during training
├── requirements.txt         # Required Python packages
└── README.md
```

## 🧠 Model Details

- **Dataset**: [LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)
- **Target labels**: Originally multi-class (true, false, half-true, etc.)  
  → Converted to binary: **real** vs **fake**
- **Vectorization**: TF-IDF (top 5000 features)
- **Models Tested**: Logistic Regression, Naive Bayes, Random Forest
- **Best Performing**: Logistic Regression (balanced accuracy & explainability)

## 🧹 Data Preprocessing

- Lowercasing
- Punctuation removal
- Stopword removal (from NLTK)
- TF-IDF vectorization

## 📈 Evaluation

- ROC curves for all models
- Confusion matrices
- Feature importance (top words contributing to fake/real predictions)
- Sample misclassifications explored

## 💻 Run Locally

1. Clone the repo:
 
   git clone https://github.com/yourusername/fake-news-detection-streamlit.git
   cd fake-news-detection-streamlit
   

2. Install dependencies:

   pip install -r requirements.txt


3. Run the app:

   streamlit run app.py


## 🌍 Deploy on Streamlit Cloud

- Upload all files to GitHub
- Go to [Streamlit Cloud](https://share.streamlit.io)
- Connect repo and set `app.py` as the entry point

## 🧾 Sample Use

Paste a news statement like:
```
"The unemployment rate has dropped to its lowest point in 50 years."
```
And the app will predict whether it's **REAL** or **FAKE** based on model inference.

## ✨ Author

**Shivang Singh Manhas**  
[LinkedIn](https://www.linkedin.com/in/shivangmanhas) | [GitHub](https://github.com/shivangmanhas)

---

📬 Feel free to connect, fork, or provide feedback!
