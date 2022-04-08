import json


def dec_movies(movies):

    # 여기에 코드를 작성합니다.
    dec_movies_list = []

    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movie_json = open('data/movies/'+str(id)+'.json', encoding='UTF8')
        movie_list = json.load(movie_json)
        release_month = movie_list.get('release_date')[5:7]
        if release_month == '12':
            dec_movies_list.append(title)
    return dec_movies_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))
