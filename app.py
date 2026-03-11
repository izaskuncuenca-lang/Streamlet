import streamlit as st
import pandas as pd

df = pd.read_csv('movies_clean.csv')

st.title('🎬 Movie Dataset Explorer')

all_genres = sorted(set(
    genre
    for genres in df['genres'].dropna()
    for genre in genres.split('|')
    if genre != '(no genres listed)'
))

selected_genre = st.selectbox('Select a genre:', all_genres)

filtered = df[df['genres'].str.contains(selected_genre, regex=False)]

st.write(f'### Movies in: {selected_genre}')
st.write(f'{len(filtered)} movies found')
st.dataframe(filtered[['Title', 'Year', 'genres']])
