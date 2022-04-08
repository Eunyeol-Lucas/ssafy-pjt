# 프레임워크를 활용한 CRUD 웹 페이지 구현

---

| **프로젝트 주제: Django와 Bootstrap을 활용한 CRUD 웹 페이지 구현"**

⏰ **시행 날짜:** 2022.04.08 금

🍀 **개발환경:** Visual Studio Code

👄 **개발언어:** html, css, python

📚 **라이브러리:** **부트스트랩 v5, Django 3.2, requests**

**🛠 개발 도구** 

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
├── db.sqlite3
├── manage.py
├── movies					# app 이름
├── parser.py				# tmdb 데이터 불러오는 파일
├── pjt06						# 프로젝트 이름
├── templates
└── venv
```

## 🏁 URL

|       URL 패턴       |            역할            |
| :------------------: | :------------------------: |
|       /movies/       | 전체 영화 목록 페이지 조회 |
|   /movies/create/    |   단일 영화 데이터 저장    |
|    /movies/<pk>/     | 단일 영화 상세 페이지 조회 |
| /movies/<pk>/update/ |   단일 영화 데이터 수정    |
| /movies/<pk>/delete/ |   단일 영화 데이터 삭제    |

tmdb data 불러오기

https://beomi.github.io/gb-crawling/posts/2017-03-01-HowToMakeWebCrawler-Save-with-Django.html

---

## 🏋🏻‍♂️ Django & Bootstrap

### 1. settings

- pjt06 프로젝트에서 movies 앱 디렉토리의 urls.py로 url 전달

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
  from os import scandir
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

### 3. forms.py 설계

- forms의 ModelForm을 활용한 input Form 클래스 생성

  ```python
  from django import forms
  from .models import Movie
  
  class MovieForm(forms.ModelForm):
      class Meta:
          model = Movie
          fields = ('title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')
  
  ```

- Django Form에서 라벨에 자동으로 콜론이 붙는 기능 제거

  ``` python
  class MovieForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.label_suffix = "" 
  ```

- Form에서 select 태그를 적용하기 위한 데이터 저장 및 widget 사용

  ```python
  
  class MovieForm(forms.ModelForm):
      GENRE_A = '코미디'
      GENRE_B = '공포'
      GENRE_C = '로맨스'
      GENRE_CHOICES = [
          ("", 'Please Choose the Genre'),
          (GENRE_A, '코미디'),
          (GENRE_B, '공포'),
          (GENRE_C, '로맨스'),
      ]
      genre = forms.ChoiceField(
          label="Genre",
          choices=GENRE_CHOICES,
          widget=forms.Select(
              attrs={
                  "class":"form-select",
              }
          )
      )
  ```

  

### 3. tmdb api 요청 및 저장

- tmdb 인기 영화 데이터 요청 및 sqlite db에 data 저장(parser.py)

  ```python
  import requests
  from pprint import pprint
  
  
  import os
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt06.settings")
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

----

## 🌏 완성된 페이지

### 1. 전체 영화 목록 조히 템플릿 (index.html)

- 데이터 베이스에 존재하는 모든 영화 목록을 표시

- 해당 영화 제목을 누를 경우 해당 영화의 상세 페이지로 이동

- [CREATE] 버튼을 누를 경우, 새로운 영화를 등록할 수 있다.

- require_safe 메서드를 통해, get 또는 HEAD method만 허용하도록 요구

  ```python
  @require_safe
  def index(request):
      movie_list = Movie.objects.order_by('-pk')
      context = {
          'movie_list': movie_list,
      }
      return render(request, 'movies/index.html', context)
  ```

<img src="README.assets/스크린샷 2022-04-08 16.27.56.png" alt="스크린샷 2022-04-08 16.27.56" style="zoom:80%;" />

### 2. 새 영화 등록 페이지(create.html)

- 메인 페이지에서 [CREATE] 버튼을 누를 경우 /movies/create/ 페이지로 이동

- require_http_methods(['GET', 'POST']) 메서드를 통해 GET 또는 POST 메서드만 접근 허용

  ```python
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == "POST":
          form = MovieForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('movies:index')
      else:
          form = MovieForm()
      context = {
          'form' : form
      }
      return render(request, 'movies/create.html', context)
  ```

  <img src="README.assets/스크린샷 2022-04-08 16.26.40.png" alt="스크린샷 2022-04-08 16.26.40" style="zoom:80%;" />

### 3. 영화 상세 페이지 (detail.html)

- 메인 페이지에서 영화 제목을 클릭할 경우 이동하는 페이지
- UPDATE 버튼을 누를 경우, 수정을 위한 /movies/\<int:pk\>/update 페이지로 이동
- DELETE 버튼을 누를 경우, 해당 영화 정보를 삭제하기 위한 POST 요청
- BACK 버튼을 누를 경우, 메인 페이지로 이동

<img src="README.assets/스크린샷 2022-04-08 16.29.02.png" alt="스크린샷 2022-04-08 16.29.02" style="zoom:80%;" />

### 4. 수정 페이지 (update.html)

- 기존의 저장된 영화 데이터를 불러와 form 내에 렌더링
- 원하는 항목의 데이터를 수정할 수 있다.

<img src="README.assets/스크린샷 2022-04-08 16.32.53.png" alt="스크린샷 2022-04-08 16.32.53" style="zoom:80%;" />

