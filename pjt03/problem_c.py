import requests
from pprint import pprint


def ranking():

    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko"
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    results = data.get('results')
    top_rank_movie_list = sorted(
        results, key=lambda x: x['vote_average'], reverse=True)
    return top_rank_movie_list[:5]


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
