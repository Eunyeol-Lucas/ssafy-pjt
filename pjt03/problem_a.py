import requests
from pprint import pprint


def popular_count():

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
    cnt = len(data.get('results'))
    return cnt


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    pprint(popular_count())
    # => 20
