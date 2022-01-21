# 0121 PJT01

# Python을 활용한 데이터 수집 I

시행 날짜: 2022.01.21 금

개발환경: vscode

개발언어: python 3.9.9 

페어프로그래밍 팀원: 🦾`남은열님, 이재상님` 🐬🐬

라이브러리: json, pprint

목표: python 기본 문법 실습

파일 입출력에 대한 이해

데이터 구조에 대한 분석과 이해

데이터를 가공하고 JSON 형태로 저장

---

## 📄 파일 설명

### **1. problem_a.py**

- 파이썬을 활용한 딕셔너리 `dictionary` 내의 필요한 데이터 추출
- 추출한 데이터를 바탕으로 딕셔너리 `dictionary` 반환

---

### 2. problem_b.py

- 파이썬을 활용한 딕셔너리 `dictionary` 내의 필요한 데이터 추출
- 딕셔너리 `dictionary` 의 `value` 를 활용하여, 새로운 딕셔너리에 접근

---

### 3. problem_c.py

- 파이썬을 활용한 딕셔너리 `dictionary` 내의 필요한 데이터 추출
- 반복문을 활용하여, 리스트 `list` 내의 딕셔너리에 접근

---

### 4. problem_d.py

- 파이썬을 활용한 `.json` 파일 데이터 추출
- 딕셔너리 `dictionary` 의 `value` 를 활용하여, `.json` 파일에 접근할 문자열 `string`을 형성
- 조건문 `if` 을 활용하여, 필요한 결과를 반환

---

### 5. problem_e.py

- 파이썬을 활용한 `.json` 파일 데이터 추출
- 딕셔너리 `dictionary` 의 `value` 를 활용하여, `.json` 파일에 접근할 문자열 `string`을 형성
- 조건문 `if` 과 문자열 `string` 인덱싱을 활용하여, 필요한 결과를 반환

---

## 🕹 Skill

### 1. value = dict.get(key)

딕셔너리 구조에서 value를 얻기 위해 `dict[key]` 구조를 활용할 경우, 해당 key에 대한 value가 없을 때 `Key Error` 가 발생하여 해당 코드가 들어가 있는 함수의 실행이 종료된다. 하지만 `dict.get(key, default value)` 의 경우 해당 key에 대한 value가 존재하지 않을 경우 get 함수의 두 번째 매개변수에 해당하는 `default value`값을 가져오거나, 지정하지 않을 경우 `None`이 나타나 해당 함수가 에러 없이 동작할 수 있도록 한다.

### 2. list를 활용한 간결한 코드

최초 코드 작성시 `value = dict.get(key)` 와 같은 형태로 코드를 작성하였지만, `dict.get()` 등 코드의 중복을 줄이고 직관성을 높이기 위해 `list`와 `for문` 통해 코드를 줄일 수 있었다.

```python
def movie_info(movies):

    # 여기에 코드를 작성합니다.
    movie_info_list = ['id', 'title', 'poster_path',
                        'vote_average', 'overview', 'genre_ids']
		for info in movie_info_list:
				movie_dict = {}
				movie_dict[info] = movie.get(info)
```

### 3. index slicing vs datetime()

`yyyy-mm-dd` 형태의  문자열을 통해서 연, 월, 일 정보를 얻고자 할때, [:4], [5:7], [9:] 형태로 slicing해서 사용할 수 있을 것이다.

```python
a = '2022-01-21'
print(a[:4]) # 2022
print(a[5:7]) # 01
print(a[9:]) # 21
```

but,  `datetime` 모듈을 사용하면, 날짜 관련 정보를 다양하게 활용할 수 있을 것이다.

```python
from datetime import date
a = date.fromisoformat('2022-01-21')
print(a.year) # 2022
print(a.month) # 1
print(a.day) # 21
```