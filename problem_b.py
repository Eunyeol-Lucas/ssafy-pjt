import json
from pprint import pprint


def movie_info(movie, genres):
    # # 여기에 코드를 작성합니다.
    movie_info_list = ['id', 'title', 'poster_path',
                       'vote_average', 'overview', 'genre_ids']
    movie_dict = {}
    genre_names = []
    for info in movie_info_list:
        if info == 'genre_ids':
            for i in info:
                for j in genres:
                    if j['id'] == i:
                        genre_names.append(j['name'])
            movie_dict['genre_names'] = genre_names
        else:
            movie_dict[info] = movie.get(info)
    return movie_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
