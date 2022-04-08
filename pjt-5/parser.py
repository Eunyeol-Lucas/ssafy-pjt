import requests
from pprint import pprint


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt05.settings")
import django
django.setup()

from movies.models import Movie

def get_movie_data():
    BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko",
        "page": 1,
    }
    genres = [{"id":28,"name":"Action"},{"id":12,"name":"Adventure"},{"id":16,"name":"Animation"},{"id":35,"name":"Comedy"},{"id":80,"name":"Crime"},{"id":99,"name":"Documentary"},{"id":18,"name":"Drama"},{"id":10751,"name":"Family"},{"id":14,"name":"Fantasy"},{"id":36,"name":"History"},{"id":27,"name":"Horror"},{"id":10402,"name":"Music"},{"id":9648,"name":"Mystery"},{"id":10749,"name":"Romance"},{"id":878,"name":"Science Fiction"},{"id":10770,"name":"TV Movie"},{"id":53,"name":"Thriller"},{"id":10752,"name":"War"},{"id":37,"name":"Western"}]
    movie_list = []
    response  = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get("results"):
        movie_data = data.get("results")[:20]

        for i in movie_data:
            for genre in genres:
                if genre["id"] == int(i.get("genre_ids")[0]):
                    movie_genre = genre["name"]
                    break
            tmp = {
                "title" : i.get("title"),
                "poster" : f'https://image.tmdb.org/t/p/original{i.get("poster_path")}',
                "genre" : movie_genre,
                "description" : i.get("overview"),
                "score" : i.get("vote_average"),
                "audience" : i.get("popularity"),
                "release_date" : i.get("release_date")
            }
            movie_list.append(tmp)
    # pprint(movie_list)
    return movie_list

        
if __name__=='__main__':
    movie_dict = get_movie_data()

    for k in movie_dict:
        movie = Movie()
        movie.title = k["title"]
        movie.release_date = k["release_date"]
        movie.poster_url = k["poster"]
        movie.genre = k["genre"]
        movie.description = k["description"]
        movie.score = k["score"]
        movie.audience = k["audience"]

        movie.save()