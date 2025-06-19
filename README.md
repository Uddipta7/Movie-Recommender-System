# 🎬 Movie Recommender System

A **Content-Based Movie Recommendation System** built with **Python**, **Streamlit**, and the **TMDb API**. This web app recommends movies based on their similarity to a selected title using cosine similarity computed from movie metadata.

---

## 🖼️ Preview

![image](https://github.com/user-attachments/assets/4cd3b705-b103-4349-97a3-c841c570a607)

---

## 🧠 How It Works

This app uses **content-based filtering** to suggest movies similar to the one you select by analyzing:

- 🎞️ Movie overviews  
- 🧩 Genres & keywords  
- 🧑‍🎤 Cast and crew  

Cosine similarity is calculated on vectorized features to find and rank the most similar titles.

---

## 🛠️ Built With

- 🐍 Python  
- 📊 Pandas / NumPy  
- 🤖 Scikit-learn  
- 🌐 Streamlit – for the interactive web interface  
- 🎥 TMDb API – for fetching movie posters and metadata  
- 🧃 Pickle – for saving and loading processed data & similarity matrix

---

## ✨ Features

- 🔍 Select any movie and get **top 5 similar recommendations**
- 📸 Fetch **movie posters** and titles via TMDb API
- ⚡ Efficient **cosine similarity-based** ranking
- 🧑‍💻 Clean and **interactive UI** built with Streamlit

--

## 📦 Installation
🔁 Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```
🧱 Install Requirements
```bash
pip install -r requirements.txt
```
▶️ Run the App
```bash
streamlit run app.py
```
## 📁 Project Structure
```bash
├── app.py                  # Streamlit app
├── movies.csv              # Movie metadata
├── similarity.pkl          # Precomputed similarity matrix
├── poster_fetch.py         # TMDb API calls for poster images
├── requirements.txt
└── README.md
```

## 🔑 API Key
This project uses the TMDb API to fetch movie posters.


