import requests
from pprint import pprint


def vote_average_movies():

    # 여기에 코드를 작성합니다.
    popular_movie_list = []
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko"
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    for i in data.get('results'):
        if i.get('vote_average') >= 8:
            popular_movie_list.append(i)
    return popular_movie_list


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
