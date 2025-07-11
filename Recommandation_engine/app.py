import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Streamlit Page Config
st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommender Engine")
st.write("Find movies similar to your favorite ones using genres and content-based filtering.")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\SRK_CLASS\SRK_Class\Notes\16. Recommendation Engines\movies.csv")
    df.dropna(inplace=True)
    return df

df = load_data()

# Vectorize the genres
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(df['genres'])

# Compute similarity
similarity = cosine_similarity(feature_vectors)

# Input section
movie = st.text_input("Enter your Favorite Movie:", placeholder="e.g., The Dark Knight")

if movie:
    list_of_titles = df['title'].tolist()
    close_match = difflib.get_close_matches(movie, list_of_titles, n=1, cutoff=0.6)

    if close_match:
        matched_movie = close_match[0]
        st.success(f"Top match found: **{matched_movie}**")

        index_of_the_movie = df[df.title == matched_movie].index[0]
        similar_movies = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

        st.subheader("🎥 Recommended Movies:")
        for i, (index, score) in enumerate(sorted_similar_movies[1:11], start=1):  # skip the same movie itself
            recommended_title = df.iloc[index]['title']
            st.write(f"{i}. {recommended_title}")
    else:
        st.error("❌ Sorry, no close match found for the entered movie.")
