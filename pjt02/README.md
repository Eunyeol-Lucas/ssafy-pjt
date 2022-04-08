# pjt02

# Python을 활용한 데이터 수집 II

**시행 날짜:** 2022.01.28 금

**개발환경:** vscode

**개발언어:** python 3.9.9 

**페어프로그래밍 팀원:** `남은열님 🧑🏻‍💻, 이진영님 🧑🏻‍💻`

**라이브러리:** json, pprint

**목표**

- python 기본 문법 실습
- 데이터 구조에 대한 분석과 이해
- 요청과 응답에 대한 이해
- API의 활용과 문서 분석

---

## 📄 파일 설명

### **1. problem_a.py**

- `request.get()` 메서드를 통해 요청한 api의 데이터를 받고 json 형태로 변형
- 데이터에서 딕셔너리의 `results` 키에 원하는 정보가 담겨있음.
__________________모든 과정에 반복되므로 이하 설명 생략______________
- `len()` 메서드를 통해 전달된 데이터 리스트의 길이를 출력

---

### 2. problem_b.py

- 딕셔너리 타입의 데이터 `results` key의 value에 해당하는 리스트의 요소인 딕셔너리에 존재하는 `vote_average` 키의 value를 확인
- value가 0 이상일 경우, 새로운 배열에 추가하여 출력

---

### 3. problem_c.py

- 딕셔너리 타입의 데이터의 `results` 의 value에 해당하는 리스트의 요소인 딕셔너리에 존재하는 `volt_average` key의 value를 기준으로 `results` 를 내림차순 정렬
- 슬라이싱을 통해 상위 5개의 요소를 출력

---

### 4. problem_d.py

- title을 params의 query에 추가하여 영화의 정보를 요청
- 딕셔너리 타입의 데이터의 `results` 가 존재하지 않는 경우 → `None` 반환
- `results` 에서 `movie_id`를 반환하여 새로운 path에  추가
- `get recommendation` 요청을 통해 결과를 반환
- 딕셔너리 타입의 데이터에서 `results` 키가 없는 경우 → `[]` 반환
- `results` 데이터의 value인 딕셔너리에서 `title` 의 value를 새로운 리스트에 담아 출력

---

### 5. problem_e.py

- title을 params의 query에 추가하여 영화의 정보를 요청
- 딕셔너리 타입의 데이터의 `results` 가 존재하지 않는 경우 → `None` 반환
- `results` 에서 `movie_id`를 반환하여 새로운 path에  추가
- 반환받은 데이터에서 `cast` key를 for문을 통해 순회하며 딕셔너리 타입의 value의 `cast_id` 가 10보다 작은 경우 cast_list에 추가
- 반환받은 데이터에서 `crew` key를 for문을 통해 순회하며 딕셔너리 타입의 value의 `department` 가  ``Directing` 인 경우 directing_list에 추가
- 두 리스트를 하나의 딕셔너리에 추가하여 출력

---

### 6. problem_f.py

- 네이버 영화 api를 통해 영화 정보를 얻어봄
- 네이버 영화는 `request.get` 요청시 header에 client_id 와 client_secret 이 필요
- query에 movie 단어를 포함할 경우 해당 단어가 강조되어 replace함수를 통해 해당 element 제거

---

## 🕹 Skill

### 1. value = dict.get(key)

딕셔너리 구조에서 value를 얻기 위해 `dict[key]` 구조를 활용할 경우, 해당 key에 대한 value가 없을 때 `Key Error` 가 발생하여 해당 코드가 들어가 있는 함수의 실행이 종료된다. 하지만 `dict.get(key, default value)` 의 경우 해당 key에 대한 value가 존재하지 않을 경우 get 함수의 두 번째 매개변수에 해당하는 `default value`값을 가져오거나, 지정하지 않을 경우 `None`이 나타나 해당 함수가 에러 없이 동작할 수 있도록 한다.

### 2. sorted(list, key = lambda)

리스트를 정렬하기 위해 해당 `sorted(list, key = func)` 를 이용하여 정렬. 함수의 재사용성이 적기 때문에 별도의 함수를 생성하는 대신 `lambda` 를 통해 함수를 만들어 해당 기준으로 리스트를 정렬하여 출력

```python
def ranking():

    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'eba1de962633cb7eb4cb4be4665bf5ba',
        'region': 'KR',
        'language': "ko"
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    results = data.get('results')
    top_rank_movie_list = sorted(
        results, key=lambda x: x['vote_average'], reverse=True)
    return top_rank_movie_list[:5]
```