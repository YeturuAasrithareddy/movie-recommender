import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

GENRES = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "romance": 10749,
    "sci-fi": 878,
    "thriller": 53,
    "animation": 16,
    "fantasy": 14,
    "mystery": 9648
}

def get_movies_by_genre(genre_name):
    try:
        genre_name = genre_name.lower()
        if genre_name not in GENRES:
            return []
        genre_id = GENRES[genre_name]
        url = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": API_KEY,
            "with_genres": genre_id,
            "sort_by": "vote_average.desc",
            "vote_count.gte": 1000
        }
        response = requests.get(url, params=params)
        movies = response.json().get("results", [])
        return movies[:5]
    except Exception as e:
        print(f"Error fetching by genre: {e}")
        return []

def get_movies_by_title(title):
    try:
        url = f"{BASE_URL}/search/movie"
        params = {
            "api_key": API_KEY,
            "query": title
        }
        response = requests.get(url, params=params)
        movies = response.json().get("results", [])
        return movies[:1]
    except Exception as e:
        print(f"Error searching title: {e}")
        return []

def get_similar_movies(movie_id):
    try:
        url = f"{BASE_URL}/movie/{movie_id}/similar"
        params = {"api_key": API_KEY}
        response = requests.get(url, params=params)
        movies = response.json().get("results", [])
        return movies[:5]
    except Exception as e:
        print(f"Error fetching similar: {e}")
        return []

def recommend_by_genre(genre):
    movies = get_movies_by_genre(genre)
    results = []
    for movie in movies:
        results.append({
            "title": movie.get("title", "Unknown"),
            "rating": round(movie.get("vote_average", 0), 1),
            "overview": movie.get("overview", "No description available.")[:150] + "...",
            "year": movie.get("release_date", "N/A")[:4] if movie.get("release_date") else "N/A"
        })
    return results

def recommend_by_liked_movie(title):
    found = get_movies_by_title(title)
    if not found:
        return []
    movie_id = found[0]["id"]
    similar = get_similar_movies(movie_id)
    results = []
    for movie in similar:
        results.append({
            "title": movie.get("title", "Unknown"),
            "rating": round(movie.get("vote_average", 0), 1),
            "overview": movie.get("overview", "No description available.")[:150] + "...",
            "year": movie.get("release_date", "N/A")[:4] if movie.get("release_date") else "N/A"
        })
    return results