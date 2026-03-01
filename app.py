import streamlit as st
import pandas as pd
import pickle
import difflib
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
movies_data = pd.read_csv(os.path.join(BASE_DIR, "movies.csv"))


st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter your favourite movie name:")

if st.button("Recommend"):

    list_of_all_titles = movies_data['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        st.error("Movie not found. Please check spelling.")
    else:
        close_match = find_close_match[0]

        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.success(f"Movies suggested for you based on '{close_match}':")

        i = 1
        for movie in sorted_similar_movies:
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]

            if i < 30:
                st.write(f"{i}. {title_from_index}")

                i += 1




