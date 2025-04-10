# Movie-Recommender-System
A Content-Based Movie Recommendation System built using Streamlit and the TMDb API. This web app recommends movies based on their similarity to a selected title using a cosine similarity matrix computed from movie features.

📷 Preview:
![image](https://github.com/user-attachments/assets/4cd3b705-b103-4349-97a3-c841c570a607)

🧠 How It Works
This project uses a content-based filtering approach to suggest similar movies based on:

Movie overviews

Genres

Keywords

Cast and crew

It calculates cosine similarity between vectorized movie features and recommends top similar titles.

🛠️ Built With
Python

Pandas / Numpy

Scikit-learn

Streamlit – for the web interface

TMDb API – for fetching posters and additional movie info

Pickle – for saving and loading preprocessed data and similarity matrices

🔧 Features
🔍 Select any movie and get top 5 similar movie recommendations

🎞️ Posters and titles fetched via TMDb API

🧮 Fast and efficient similarity computation using cosine similarity

⚡ Intuitive and interactive UI with Streamlit

📦 Installation
🔁 Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
🧱 Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
├── app.py                  # Streamlit app
├── movies.csv              # Movie metadata
├── similarity.pkl          # Precomputed similarity matrix
├── poster_fetch.py         # TMDb API calls for poster images
├── requirements.txt
└── README.md
🔑 API Key
This project uses the TMDb API to fetch movie posters.

📈 Future Improvements
Add user-based collaborative filtering

Search functionality for movies

Save user preferences with session state

Deploy on Streamlit Cloud / Render / Heroku
