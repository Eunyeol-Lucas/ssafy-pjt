# 사용자 인증기반 관계형 DB 설계

---

| **프로젝트 주제: Django와 SQLITE를 활용한 사용자 인증 관계형 DB 설계**

⏰ **시행 날짜:** 2022.04.15 금

🍀 **개발환경:** Visual Studio Code

👄 **개발언어:** html, css, python

📚 **라이브러리:** **부트스트랩 v5, Django 3.2**

**🛠 개발 도구** 

- Visual Studio Code
- Google Chrome Browser
- Bootstrap v5.0

🎯 **목표**

-  데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
-  Django web framework를 통한 데이터 조작
-  ORM(Obejct Relational Mapping)에 대한 이해
-  Django Authentication System에 대한 이해
-  Database many to one relationshop(1:N)에 대한 이해

---

## 📂 폴더구성

`특정 depth 까지만 출력: tree -L 1`

```
.
├── accounts							# 회원가입 및 로그인 등 유저 관리 앱
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── movies								# 영화관련 CRUD를 위한 앱
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pjt07									# 프로젝트 폴더
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── templates
    └── base.html

```

## 🏁 URL

|       URL 패턴       |                             역할                             |
| :------------------: | :----------------------------------------------------------: |
|       /movies/       |                  전체 영화 목록 페이지 조회                  |
|   /movies/create/    |                    단일 영화 데이터 저장                     |
|    /movies/<pk>/     |                  단일 영화 상세 페이지 조회                  |
| /movies/<pk>/update/ |                    단일 영화 데이터 수정                     |
| /movies/<pk>/delete/ |                    단일 영화 데이터 삭제                     |
|   /accounts/login/   | 로그인 페이지 조회 & 세션 데이터 생성 및 저장 <br />(로그인) |
|  /accounts/logout/   |               세션 데이터 삭제<br/> (로그아웃)               |
|  /accounts/signup/   | 회원 생성 페이지 조회 & 단일 회원 데이터 생성 <br />(회원가입) |
|  /accounts/delete/   |            단일 회원 데이터 삭제<br/> (회원탈퇴)             |
|  /accounts/update/   | 회원 수정 페이지 조회 & 단일 회원 데이터 수정 <br />(회원정보수정) |
| /accounts/password/  | 비밀번호 수정 페이지 조회 & 단일 비밀번호 데이터 수정<br/> (비밀번호변경) |

---

## 🏋🏻‍♂️ Django & SQLITE

### 1. settings

- pjt07 프로젝트에서 movies 앱 디렉토리와 accounts urls.py로 url 전달

  ```python
  from django.contrib import admin
  from django.urls import path,include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('movies/', include('movies.urls')),
      path('accounts/',include('accounts.urls')),
  ]
  
  ```

### 2. models.py 설계

- ORM을 통한 Movie app의 db 구조 설계

  - 커스텀 유저 모델을 통해 생성한 User 테이블을 각각 외래키로 등록하여 movie 및 comment table을 별도로 생성하였다. 
  - 이를 통해 1:1 relationship 뿐만아니라, 1:N relationship에 대한 이해할 수 있었다.
  - 참조되는 테이블의 데이터가 삭제한 경우, 참조한 테이블의 데이터에 즉각적으로 반영하기 위해 `on_delete=models.CASCADE` 케스케이드 방식이 필수적임을 배웠다.

  ```python
  from tkinter import CASCADE
  from django.conf import settings
  from django.db import models
  # Create your models here.
  class Movie(models.Model):
      title           = models.CharField(max_length=20)
      description     = models.TextField()
      user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      created_at      = models.DateTimeField(auto_now_add=True)
      updated_at      = models.DateTimeField(auto_now=True)
  
  class Comment(models.Model):
      content        = models.CharField(max_length=100)
      movie          = models.ForeignKey(Movie, on_delete=models.CASCADE)
      user           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      created_at     = models.DateTimeField(auto_now_add=True)
      updated_at     = models.DateTimeField(auto_now=True)
  ```

  Django 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않은 경우가 있기 때문에

  모델 클래스 User는 AbstractUser 모델 클래스를 상속받는 커스텀 모델을 사용

  ```python
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  # Create your models here.
  
  class User(AbstractUser):
      pass
  ```

### 3. forms.py 설계

- forms의 ModelForm을 활용한 input Form 클래스 생성하여 form 구성을 용이하게 하며, db에 데이터 전달을 위한 view.py에서 validation 기능 등 다양한 기능의 도움을 받을 수 있다.

  ```python
  from .models import Movie, Comment
  from django import forms
  
  class MovieForm(forms.ModelForm):
      class Meta:
          model = Movie
          fields = ('title', 'description', )
  
  class CommentForm(forms.ModelForm):
      class Meta:
          model = Comment
          fields = ('content',)
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

  ### accounts/forms.py

  User 모델의 추상화 클래스 상속에 따른 UserCreateForm 및 UserChangeForm을 통ㄹ해 완전한 커스텀 모델을 사용할 수 있게 됨.

  ```python
  from django import forms
  from django.contrib.auth import forms
  from django.contrib.auth.forms import UserCreationForm, UserChangeForm
  from django.contrib.auth import get_user_model
  
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model()
          fields = UserCreationForm.Meta.fields + ('email',)
  
  class CustomUserChangeForm(UserChangeForm):
      class Meta:
          model = get_user_model()
          fields = ('email','first_name','last_name',)
  
  ```

### 4. template

- movies/templates/movies/detail.html

  request.user.id와 해당 영화의 user_id 컬럼의 값이 일치할 경우에만, 수정 및 삭제 버튼을 보이도록 구현

  ```htnml
  {% if user == movie.user_id %}
  <a href="{% url 'movies:update' pk=movie.pk %} ">UPDATE</a>
  {% endif %}
  ```



----

## 🌏 어려운 점

### 1. 커스텀 모델 사용

- DB에 대한 학습의 부족으로 인해 커스텀 모델을 사용함에 있어 어려움을 겪었습니다. 핵심 기능중의 하나인 User table이 구현이 되어야, 다른 영화 및 코멘트 테이블 구현이 가능하기 때문에, 페어와 함께 본격적인 페어 프로그래밍 전, 학습하는 시간을 가졌습니다. 
  특정 클래스의 상속 및 메서드의 활용을 적절하게 하여 회원가입 및 유저 인증 기능을 구현하였습니다.

  ```python
  @require_http_methods(['GET','POST'])
  def signup(request):
      if request.user.is_authenticated:
          return redirect('movies:index')
  
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request,user)
              return redirect('movies:index')
      else:
          form = CustomUserCreationForm()
      
      context = {
          'form':form,
      }
      return render(request,'accounts/signup.html',context)
  ```

### 2. 사용자 인증기반 UI

- 글을 작성한 사람많이 해당 글에 대한 수정 및 삭제 권한을 부여 및 UI가 달라지도록 구현하고자 하였습니다. request.user를 이용하여 해당 글의 user_id와 일치 여부에 따른 렌더링을 구현하고자 하였지만, 지속적으로 실패하였습니다. 원인은 해당 변수가 객체 데이터를 가지고 있다는 것을 알게 되었다. 객체 데이터지만 출력에 따라 단일 원시값을 가지는 성향을 몰랐기 때문에 기능 구현에 어려움을 겪었지만, 교수님께서 알려주셔서 기능을 잘 구현할 수 있었습니다.

---

## 👨‍👦페어 프로그래밍 느낀점

- 백엔드에 대해 잘 모르는 편이라 페어프로그래밍을 함에 있어 누가 될 까봐,  시작하기 전에 많은 고민을 했었습니다. 하지만 함께 해준 강경은 페어께서 모르는 부분이 있다면 함께 즉흥적으로 스터디를 하며, 모르는 것들을 하나씩 해결해 나갈 수 있었습니다. 
  네비게이터가 되어 다른사람에게 설명을 해줄 때, 제가 자세히 모르는 부분을 오히려 더 명확히 알 수 있게 해주었습니다. 또한 드라이버로 페어의 향해에 몸을 맡기며, 놓치고 있던 코드들을 다시금 되짚어볼 수 있는 기회였습니다.
- 비록 모든 기능들을 제 시간에 구현하지는 못했지만, 페어프로그래밍을 통해 함께 성장할 수 있는 시간을 가졌습니다.





