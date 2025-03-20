import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=4f7c6d06bc953daea7c2ef7c18219364&language=en-US'
    response = requests.get(url)
    data = response.json()

    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    else:
        return "https://via.placeholder.com/150"



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters



movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.set_page_config(page_title="Movie Recommender", layout="wide")


st.markdown("""
    <style>
        /* Page Background */
        body {
            background-color: #121212;
        }

        /* Main Title */
        .title {
            text-align: center;
            font-size: 65px; 
            color: #ffffff;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 30px;
        }

        /* Select a Movie Label */
        .selectbox-label {
            font-size: 28px; /* Increased size */
            font-weight: bold;
            color: #f4f4f4;
            margin-bottom: 10px;
        }

        /* Recommendation Button */
        .recommend-button {
            display: block;
            width: 100%;
            background-color: #e50914;
            color: white;
            font-size: 28px; /* Increased size */
            font-weight: bold;
            border-radius: 10px;
            padding: 14px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }

        .recommend-button:hover {
            background-color: #ff1a1a;
            transform: scale(1.05);
        }

        /* Movie Container */
        .movie-container {
            text-align: center;
            transition: all 0.3s ease-in-out;
        }

        /* Movie Poster Hover Effect */
        .movie-container:hover {
            transform: scale(1.1);
            box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.5);
            border-radius: 15px;
        }

        /* Movie Title */
        .movie-title {
            font-size: 20px; /* Increased size */
            font-weight: bold;
            color: #ffffff;
            margin-top: 10px;
            text-transform: uppercase;
        }
    </style>
""", unsafe_allow_html=True)



st.markdown('<p class="title"> <h1>🎬 Movie Recommendation System </h1></p>', unsafe_allow_html=True)


st.markdown('<p class="selectbox-label">📽️ Select a Movie:</p>', unsafe_allow_html=True)


selected_movie = st.selectbox("", movies['title'].values)


if st.button('🔍 Show Recommendation', key="recommend_button"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)


    cols = st.columns(5)

    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.markdown(f'<div class="movie-container">', unsafe_allow_html=True)
            st.image(poster, use_container_width=True)  # ✅ Fixed the issue
            st.markdown(f'<p class="movie-title">{name}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
