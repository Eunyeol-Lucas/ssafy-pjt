from django.shortcuts import render
import requests
from pprint import pprint
import random

# Create your views here.

def index(request):
    BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
    movie_list =[]
    params = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko",
        "page": 1,
    }
    response  = requests.get(BASE_URL, params=params )
    data = response.json()
    if data.get("results"):
        movie_data = data.get("results")[:8]
        
        for i in movie_data:
            tmp ={
                "id": f'movie{i.get("id")}',
                "title": i.get("title"),
                "overview": i.get("overview"),
                "release_date": i.get("release_date"),
                "poster": f'https://image.tmdb.org/t/p/original{i.get("poster_path")}',
            }
            movie_list.append(tmp)
    context = {
        "movie_list": movie_list
    }
    return render(request, 'index.html', context)



def recommendations(request):
    recommendation_movie_list = []
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params1 = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko",
        'query': "쇼생크 탈출"
    }
    params2 = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko"
    }
    response = requests.get(BASE_URL+path, params=params1)
    data = response.json()
    results = data.get('results')
    
    if results:
        movie_id = results[0].get('id')
        if movie_id:
            recommendation_path = f'/movie/{movie_id}/recommendations'
            recommendation_response = requests.get(
                BASE_URL+recommendation_path, params=params2).json()
            recommendation_results = recommendation_response.get('results')
            if recommendation_results:
                for i in recommendation_results:
                    tmp = {
                        "title": i.get("title"),
                        "poster": f'https://image.tmdb.org/t/p/original{i.get("poster_path")}',
                        "site": f'https://www.themoviedb.org/movie/{i.get("id")}',
                        "release_date": i.get("release_date"),
                        "overview": i.get("overview"),
                        "vote": round(i.get("vote_average"), 1)
                    }
                    recommendation_movie_list.append(tmp)

    reccomended_movie = random.choice(recommendation_movie_list)
    context = {
        "movie": reccomended_movie
    }
    return render(request, 'recommendations.html', context)


def test():
    recommendation_movie_list = []
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params1 = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko",
        'query': "쇼생크 탈출"
    }
    params2 = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko"
    }
    response = requests.get(BASE_URL+path, params=params1)
    data = response.json()
    results = data.get('results')
    pprint(data)
    if results:
        movie_id = results[0].get('id')
        if movie_id:
            recommendation_path = f'/movie/{movie_id}/recommendations'
            recommendation_response = requests.get(
                BASE_URL+recommendation_path, params=params2).json()
            recommendation_results = recommendation_response.get('results')
            if recommendation_results:
                for i in recommendation_results:
                    tmp = {
                        "title": i.get("title"),
                        "poster": f'https://image.tmdb.org/t/p/original{i.get("poster_path")}',
                        "site": f'https://www.themoviedb.org/movie/{i.get("id")}',
                        "release_date": i.get("release_date"),
                        "overview": i.get("overview"),
                        "vote": round(i.get("vote_average"), 1)
                    }
                    recommendation_movie_list.append(tmp)

test()