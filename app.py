import streamlit as st
import pandas as pd
import difflib
import pickle
import os

st.title("🎬 Movie Recommendation System")

# Load dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
movies_data = pd.read_csv(os.path.join(BASE_DIR, "movies.csv"))

# Load similarity file (only if exists)
try:
    similarity = pickle.load(open("similarity.pkl", "rb"))
except:
    st.error("similarity.pkl file not found!")
    st.stop()

movie_name = st.text_input("Enter your favourite movie name")

if st.button("Recommend"):

    list_of_all_titles = movies_data['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        st.error("Movie not found")
    else:
        close_match = find_close_match[0]

        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.subheader("Movies Suggested For You:")

        for i, movie in enumerate(sorted_similar_movies[1:21]):
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            st.write(i+1, ".", title_from_index)
