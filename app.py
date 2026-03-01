import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

st.title("🎬 Movie Recommendation System")

# Load dataset
movies_data = pd.read_csv("movies.csv")

# Fill missing values
movies_data = movies_data.fillna('')

# Combine important features
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# Convert text to vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Calculate similarity
similarity = cosine_similarity(feature_vectors)

movie_name = st.text_input("Enter your favourite movie name")

if st.button("Recommend"):

    list_of_all_titles = movies_data['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        st.error("Movie not found")
    else:
        close_match = find_close_match[0]

        index_of_the_movie = movies_data[movies_data.title == close_match].index[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.subheader("Movies Suggested For You:")

        for i, movie in enumerate(sorted_similar_movies[1:21]):
            index = movie[0]
            st.write(i+1, ".", movies_data.iloc[index]['title'])
