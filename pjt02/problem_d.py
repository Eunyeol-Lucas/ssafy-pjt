from inspect import Parameter
import requests
from pprint import pprint


def recommendation(title):

    # 여기에 코드를 작성합니다.
    recommendation_movie_list = []
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
        'language': "ko"
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    results = data.get('results')
    if results:
        if len(results) == 1:
            movie_id = results[0].get('id')
        # '그래비티' 영화가 1번 인덱스에 있기 때문에 if else로 id를 분기
        else:
            movie_id = results[1].get('id')

        if movie_id:
            recommendation_path = f'/movie/{movie_id}/recommendations'
            recommendation_response = requests.get(
                BASE_URL+recommendation_path, params=params2).json()
            recommendation_results = recommendation_response.get('results')
            if recommendation_results:
                for i in recommendation_results:
                    recommendation_movie_list.append(i.get('title'))
                return recommendation_movie_list
            return []
    return None


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
