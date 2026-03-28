import streamlit as st
from recommender import recommend_by_genre, recommend_by_liked_movie

# Page settings
st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="centered"
)

# Custom styling
st.markdown("""
    <style>
    .main { background-color: #0a0a0f; }
    h1 { color: #f5c842; text-align: center; }
    .movie-card {
        background: #111118;
        border: 1px solid #222;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎬 CineMatch")
st.markdown("<p style='text-align:center;color:#888'>Your personal movie recommendation system</p>", unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["Find by Genre", "Find by Movie You Like"])

# Tab 1 — Genre
with tab1:
    st.subheader("Pick a Genre")
    genre = st.selectbox(
        "Select a genre",
        ["Action", "Comedy", "Drama", "Horror", 
         "Romance", "Sci-Fi", "Thriller", 
         "Animation", "Fantasy", "Mystery"]
    )
    if st.button("Get Recommendations 🎬", key="genre_btn"):
        with st.spinner("Finding perfect movies for you..."):
            movies = recommend_by_genre(genre.lower())
        if movies:
            st.success(f"Top {genre} Movies!")
            for movie in movies:
                with st.container():
                    st.markdown(f"### {movie['title']} ({movie['year']})")
                    st.markdown(f"⭐ **Rating:** {movie['rating']}/10")
                    st.markdown(f"📖 {movie['overview']}")
                    st.divider()
        else:
            st.error("No movies found. Try a different genre!")

# Tab 2 — Liked Movie
with tab2:
    st.subheader("Enter a Movie You Love")
    movie_title = st.text_input(
        "Movie name",
        placeholder="e.g. Inception, The Dark Knight..."
    )
    if st.button("Get Recommendations 🎬", key="movie_btn"):
        if movie_title:
            with st.spinner("Finding similar movies..."):
                movies = recommend_by_liked_movie(movie_title)
            if movies:
                st.success(f"Movies similar to {movie_title}!")
                for movie in movies:
                    with st.container():
                        st.markdown(f"### {movie['title']} ({movie['year']})")
                        st.markdown(f"⭐ **Rating:** {movie['rating']}/10")
                        st.markdown(f"📖 {movie['overview']}")
                        st.divider()
            else:
                st.error("No movies found. Try a different title!")
        else:
            st.warning("Please enter a movie name first!")