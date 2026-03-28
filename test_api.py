import requests

# Paste your API key here
API_KEY = "f0378f12edd73fcd3918167bd6601254"

# Fetch popular movies
url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"
response = requests.get(url)
data = response.json()

# Print first movie title
print("Connected! First popular movie:", data["results"][0]["title"])