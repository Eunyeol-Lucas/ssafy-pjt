import json
from pprint import pprint


def movie_info(movies, genres):

    # 여기에 코드를 작성합니다.
    movie_info_list = ['id', 'title', 'poster_path',
                        'vote_average', 'overview', 'genre_ids']
    all_movies = []
    for movie in movies:
        movie_dict = {}
        for info in movie_info_list:
            if info == "genre_ids":
                tmp = []
                for genre in genres:
                    if genre.get('id') in movie.get(info):
                        tmp.append(genre.get('name'))
                    movie_dict['genre_names'] = tmp
            else:
                movie_dict[info] = movie.get(info)
        all_movies.append(movie_dict)
    return all_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
