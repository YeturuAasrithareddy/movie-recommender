from flask import Flask, render_template, request
from recommender import recommend_by_genre, recommend_by_liked_movie

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Recommend by genre
@app.route("/by-genre", methods=["POST"])
def by_genre():
    genre = request.form.get("genre")
    movies = recommend_by_genre(genre)
    return render_template("results.html", movies=movies, title=f"Top {genre.title()} Movies")

# Recommend by liked movie
@app.route("/by-movie", methods=["POST"])
def by_movie():
    movie_title = request.form.get("movie_title")
    movies = recommend_by_liked_movie(movie_title)
    return render_template("results.html", movies=movies, title=f"Movies Similar to {movie_title}")

if __name__ == "__main__":
    app.run(debug=True)