import json
from pprint import pprint


def max_revenue(movies):

    # 여기에 코드를 작성합니다.
    max_revenue_movie_title = ""
    max_rev = 0
    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movie_json = open('data/movies/'+str(id)+'.json', encoding='UTF8')
        movie_list = json.load(movie_json)
        revenue = movie_list.get('revenue')
        if revenue > max_rev:
            max_rev = revenue
            max_revenue_movie_title = title
    return max_revenue_movie_title


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    pprint(max_revenue(movies_list))
