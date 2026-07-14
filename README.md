# X Sentiment Analysis

This repository contains a complete end-to-end Machine Learning project that predicts the sentiment of a tweet (Positive or Negative). It includes a Jupyter Notebook for data preprocessing and model training, and a Streamlit web application for real-time inference.

## Live Demo
`https://ml-model-x-sentiment-analysis-anhvw.streamlit.app/`

## Tech Stack
* **Language:** Python
* **Web Framework:** Streamlit
* **Machine Learning:** Scikit-Learn (TF-IDF Vectorization, Classification)
* **NLP Processing:** NLTK (Stopwords removal, Porter Stemmer), Regular Expressions (`re`)
* **Data Manipulation:** Pandas

## Project Structure
* `x-sentiment-analysis.ipynb`: The core notebook containing data exploration, text cleaning (regex, stemming), TF-IDF vectorization, and model training.
* `app.py`: The Streamlit application script that loads the saved model and provides a user interface for live predictions.
* `trained_model.sav`: The pickled machine learning model (and vectorizer).
* `requirements.txt`: List of Python dependencies required to run the web app.
* `.gitignore`: Ensures large datasets and private API keys (like `kaggle.json`) are not uploaded to GitHub.

## Dataset
[Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)