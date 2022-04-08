import requests
from pprint import pprint

client_id = "QktOmXbcaOk7XIQzt5za"
client_secret = "fJF5lJfUJ5"
headers = {"X-Naver-Client-Id": client_id,
           "X-Naver-Client-Secret": client_secret}


def solution(title):
    movie_list = []
    url = f'https://openapi.naver.com/v1/search/movie.json?query={title}'
    response = requests.get(url, headers=headers).json()
    for i in response.get('items'):
        title = i.get('title').replace('</b>', "").replace("<b>", "")
        rate = float(i.get('userRating'))
        movie_list.append((title, rate))
    return sorted(movie_list, key=lambda x: x[1], reverse=True)


pprint(solution("스파이더맨"))
pprint(solution("기생충"))
