import requests
from pprint import pprint


def credits(title):

    # 여기에 코드를 작성합니다.
    cast_id_less_10_list = []
    directing_list = []
    credits_dict = {'cast': cast_id_less_10_list, 'crew': directing_list}
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko",
        'query': title
    }
    params2 = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko",
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    if data.get('results'):
        movie_id = data.get('results')[0].get('id')
        if movie_id:
            credits_path = f'/movie/{movie_id}/credits'
            credits_response = requests.get(
                BASE_URL+credits_path, params=params2).json()
            for i in credits_response.get('cast'):
                if i.get('cast_id') < 10:
                    cast_id_less_10_list.append(i.get('name'))
            for i in credits_response.get('crew'):
                if i.get('department') == "Directing":
                    directing_list.append(i.get('name'))
            return credits_dict
    return None


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
