# README.md

# 프레임워크를 활용한 CRUD 웹 페이지 구현

---

> **프로젝트 주제: Django와 Bootstrap을 활용한 CRUD 웹 페이지 구현"**

⏰ **시행 날짜:** 2022.03.11 금

🍀 **개발환경:** Visual Studio Code

👄 **개발언어:** html, css, python

📚 **라이브러리:** **부트스트랩 v5, Django 3.2, requests**

**⚒ 개발 도구** 

- Visual Studio Code
- Google Chrome Browser
- Bootstrap v5.0

🎯 **목표**

-  데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
-  Django web framework를 통한 데이터 조작
-  ORM(Obejct Relational Mapping)에 대한 이해
-  관리자 페이지를 통한 데이터 관리

---

## 📂 폴더구성

`특정 depth 까지만 출력: tree -L 1`

```
.
├── README.md
├── README.pdf
├── db.sqlite3
├── manage.py	
├── movies								# app 이름
├── parser.py             # tmdb 데이터를 불러오는 파일
├── pjt05									# 프로젝트 이름
├── requirements.txt
├── templates		
└── venv									
```



---

## 🏁 URL

| URL 패턴             | 역할                         |
| -------------------- | ---------------------------- |
| /movies/             | 전체 영화 목록 페이지 조회   |
| /movies/new/         | 새로운 영화 작성 페이지 조회 |
| /movies/create/      | 단일 영화 데이터 저장        |
| /movies/<pk>/        | 단일 영화 상세 페이지 조회   |
| /movies/<pk>/edit    | 기존 영화 수정 페이지 조회   |
| /movies/<pk>/update/ | 단일 영화 데이터 수정        |
| /movies/<pk>/delete/ | 단일 영화 데이터 삭제        |

tmdb data 불러오기

https://beomi.github.io/gb-crawling/posts/2017-03-01-HowToMakeWebCrawler-Save-with-Django.html

---

## 🏋🏻‍♂️ Django & Bootstrap

### 1. settings

- pjt05 프로젝트에서 movies 앱 디렉토리의 urls.py로 url 전달

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('movies/', include("movies.urls"))
  ]
  ```

### 2. models.py 설계

- ORM을 통한 db 구조 설계

  ```python
  from django.db import models
  
  # Create your models here.
  class Movie(models.Model):
      title           = models.CharField(max_length=20)
      audience        = models.IntegerField()
      release_date    = models.DateField(auto_now=False, auto_now_add=False)
      genre           = models.CharField(max_length=30)
      score           = models.FloatField()
      poster_url      = models.TextField()
      description     = models.TextField()
  
  
  ```

  

### 3. tmdb api 요청 및 저장

- tmdb 인기 영화 데이터 요청 및 sqlite db에 data 저장

  ```python
  import requests
  from pprint import pprint
  
  
  import os
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt05.settings")
  import django
  django.setup()
  
  from movies.models import Movie
  
  def get_movie_data():
      BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
      params = {
          'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
          'region': 'KR',
          'language': "ko",
          "page": 1,
      }
      genres = [{"id":28,"name":"Action"},{"id":12,"name":"Adventure"},{"id":16,"name":"Animation"},{"id":35,"name":"Comedy"},{"id":80,"name":"Crime"},{"id":99,"name":"Documentary"},{"id":18,"name":"Drama"},{"id":10751,"name":"Family"},{"id":14,"name":"Fantasy"},{"id":36,"name":"History"},{"id":27,"name":"Horror"},{"id":10402,"name":"Music"},{"id":9648,"name":"Mystery"},{"id":10749,"name":"Romance"},{"id":878,"name":"Science Fiction"},{"id":10770,"name":"TV Movie"},{"id":53,"name":"Thriller"},{"id":10752,"name":"War"},{"id":37,"name":"Western"}]
      movie_list = []
      response  = requests.get(BASE_URL, params=params)
      data = response.json()
      if data.get("results"):
          movie_data = data.get("results")[:20]
  
          for i in movie_data:
              for genre in genres:
                  if genre["id"] == int(i.get("genre_ids")[0]):
                      movie_genre = genre["name"]
                      break
              tmp = {
                  "title" : i.get("title"),
                  "poster" : f'https://image.tmdb.org/t/p/original{i.get("poster_path")}',
                  "genre" : movie_genre,
                  "description" : i.get("overview"),
                  "score" : i.get("vote_average"),
                  "audience" : i.get("popularity"),
                  "release_date" : i.get("release_date")
              }
              movie_list.append(tmp)
      # pprint(movie_list)
      return movie_list
  
          
  if __name__=='__main__':
      movie_dict = get_movie_data()
  
      for k in movie_dict:
          movie = Movie()
          movie.title = k["title"]
          movie.release_date = k["release_date"]
          movie.poster_url = k["poster"]
          movie.genre = k["genre"]
          movie.description = k["description"]
          movie.score = k["score"]
          movie.audience = k["audience"]
  
          movie.save()
  ```

### 4. 전체 영화 목록 조회 템플릿 (index.html)

- 데이터베이스에 존재하는 모든 영화의 목록을 표시

- index.html에는 적절한 HTML 요소를 사용하여 영화 제목 및 평점을 표시하며, [자세히 보기] 버턴을 클릭 시 해당 영화의 상세 조회 페이지로 이동

  ![스크린샷 2022-03-11 17.43.51](README.assets/스크린샷 2022-03-11 17.43.51.png)

### 5. 영화 상세 정보 페이지 (detail.html)

- 모든 사이트를 반응형에 맞추어 구현
- 특정 영화의 상세 정보를 표시
- 해당 영화의 수정 및 삭제 버튼을 표시
- [LOGO]를 클릭할 경우 index.html로 이동
- [EDIT] 버튼을 클릭할 경우 편집 페이지로 이동
- [DELETE] 버튼을 클릭할 경우 해당 게시물이 삭제
- ![스크린샷 2022-03-11 17.44.23](README.assets/스크린샷 2022-03-11 17.44.23.png)

### 6. 영화 작성 페이지 (new.html)

- 영화 작성 Form을 표시
- Form에 작성한 정보는 제출(submit)시, 영화 데이터를 저장하는 URL로 요청과 함께 전송
- [LOGO]를 클릭할 경우 index.html로 이동
- ![스크린샷 2022-03-11 17.47.03](README.assets/스크린샷 2022-03-11 17.47.03.png)

### 7. 영화 수정 페이지 (edit.html)

- 영화 수정 Form을 표시
- Form에는 기존 영화 데이터를 출력
- Form에 작성한 정보는 제출(submit)시, 영화 데이터를 수정하는 URL로 요청과 함께 전송
- [LOGO]를 클릭할 경우 index.html로 이동
- ![스크린샷 2022-03-11 17.47.53](README.assets/스크린샷 2022-03-11 17.47.53.png)