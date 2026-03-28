from recommender import recommend_by_genre, recommend_by_liked_movie

print("=== Movies by Genre (Action) ===")
movies = recommend_by_genre("action")
for m in movies:
    print(f"{m['title']} ({m['year']}) - Rating: {m['rating']}")

print("\n=== Movies Similar to Inception ===")
movies = recommend_by_liked_movie("Inception")
for m in movies:
    print(f"{m['title']} ({m['year']}) - Rating: {m['rating']}")