# Vue를 활용한 SPA 구현

| **프로젝트 주제: vue와 router를 활용하여 SPA를 구현한다.**

⏰ **시행 날짜:** 2022.05.13 금

**👬 페어: 남은열, 원재호**

🍀 **개발환경:** Visual Studio Code

👄 **개발언어:** html, css, javaScript

📚 **라이브러리:** Vue2, vue-router, vuex, axios, tailwindCSS

**🛠 개발 도구**

- Visual Studio Code
- Google Chrome Browser
- tmdb API

🎯 **목표**

- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Single File Component 구조에 대한 ㅍ
- vue-cli, vuex, vue-router 등 플러그인 활용

---

## 🌱 Router 구성

| path | Component | Description |
| --- | --- | --- |
| / | HomeView | 전체 영화 목록 페이지 |
| /random | RandomView | 랜덤 영화 추천 페이지 |
| /watch-list | /WatchListView | 개인 영화 목록 페이지 |

---

## 📂 폴더 구성

```bash
.
├── App.vue
├── assets
├── components
│   ├── MovieCard.vue            # 영화 카드 컴포넌트
│   ├── SearchedMovieList.vue    # 검색한 영화리스트 컴포넌트
│   ├── WatchList.vue            # 내가 본 영화 리스트 컴포넌트
│   └── WatchListForm.vue        # 검색 창 컴포넌트
├── input.css                    # tailwind To CSS
├── main.js
├── router
│   └── index.js
├── store
│   └── index.js
└── views
    ├── HomeView.vue
    ├── RandomView.vue
    └── WatchListView.vue
```

---

## 💪 기능

### **Home 페이지**

- **인기영화 디스플레이**

  - TMDB API '/movie/popular' 로 요청을 보내어 현재 인기있는 데일리 영화 리스트를 받아옵니다.

    ```jsx
    methods: {
        async fetchMovies() {
          const PATH = 'movie/popular'
          const API_KEY = process.env.VUE_APP_API_KEY
          const BASR_URL = process.env.VUE_APP_TMDB_BASE_URL + PATH
          const params = {
            api_key: API_KEY,
            language: 'ko',
            region: 'KR'
          }
          const response = await axios.get(BASR_URL, { params })
          this.movies = response.data.results
        }
      },
    ```

- **MovieCard**

  - 영화 각각의 정보를 카드형태에 담아 보여지게 됩니다.

  - 모든 영화의 이미지 크기, 비율을 고정하고 반응형웹에 맞춰 비율을 유지한체 이미지 크기가 변경됩니다.

  - 영화의 dedcription을 display: -webkit-box 를 사용하여 카드 기준에서 네줄이상 넘어가면 ... 을 붙여 생략하도록 했습니다.

    ```html
      <div ... >
        <div class="poster-wrapper">
          <img
            class="poster"
            :src="`${URL}${movie.poster_path}`"
            alt="Poster Image"
          />
        </div>
        <div class="px-6 py-4">
          <div class="font-bold text-xl mb-2">{{ movie.title }}</div>
          <p class="text-gray-700 text-base word">
            {{ movie.overview }}
          </p>
        </div>
      </div>
    <style>
      .poster-wrapper {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 150%;
        overflow: hidden;
      }
      .poster {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }
      .word {
      font-weight: bolder;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: normal;
      word-wrap: break-word;
      display: -webkit-box;
      -webkit-line-clamp: 4;
      -webkit-box-orient: vertical;
    }
    </style>
    ```

### **Random 페이지**

- __장르별 랜덤 영화 추천 기능__

  - 버튼을 누르면 사용자가 선택한 장르에 맞는 영화 목록을 받아와 랜덤한 영화 한개를 보여줍니다.

    ```jsx
    methods: {
        async fetchMovies() {
          const PATH = `discover/movie`
          const API_KEY = process.env.VUE_APP_API_KEY
          const BASR_URL = process.env.VUE_APP_TMDB_BASE_URL + PATH
          const params = {
            api_key: API_KEY,
            language: 'ko',
            with_genres: this.genre
          }
          const response = await axios.get(BASR_URL, { params })
          console.log(response)
          const result = _.sample(response.data.results)
          this.movie=result
          this.show=true
        },
        getGenre(e) {
          this.genre = e.target.value
          console.log(this.genre)
        }
      }
    ```

### WatchList 페이지

- **검색 기능**
    - TMDB API를 활용하여 검색어를 입력할 경우, TMDB 서버로 전송하여 해당 키워드와 관련된 영화 리스트를 가져옵니다.
    - Vuex를 통해 불러온 영화 리스트의 목록을 관리하며, **기존에 본 영화 리스트를 제외한 영화**만 view에 나타납니다.
      
        ```jsx
        mutations: {
            setSearchedMovieList(state, searchedMovieList) {
              const filteredMovieList = searchedMovieList.filter((movie) => {
                return !state.watchedMovieIdList.includes(movie.id);
              });
              state.searchedMovieList = filteredMovieList;
              state.isSearchedMovie = filteredMovieList.length !== 0;
            },
            resetSearchedMovieList(state) {
              state.searchedMovieList = [];
            },
        }
        ```
    
- **공통된 MovieCard 컴포넌트 사용**
    - 관련된 영화 리스트가 나타날 경우 클릭 시 **내가 본 영화 리스트**에 저장됩니다.
    - 컴포넌트를 재활용하여 중복되는 코드를 줄일 수 있었습니다.
    - 카드 컴포넌트를 재활용하기 위해 props 속성을 이용하여 해당 props를 전달 해주었을 때 추가적인 method를 실행시키도록 하였습니다.
      
        ```jsx
        // MovieCard.vue
        
        // ... 생략
        <div
            v-if="movie"
            class="max-w-sm rounded overflow-hidden shadow-lg"
            @click="setRemainedSearchedMovieList(index)"
          >
        
        // ... 생략
        
        methods: {
            ...mapMutations(["setRemainedSearchedMovieList"]),
          },
        
        // ... 생략
        
        // store.index.vue
        setRemainedSearchedMovieList(state, index) {
              if (index === undefined) return;
              this.commit("addWatchedMovieList", state.searchedMovieList[index]);
              state.searchedMovieList = state.searchedMovieList.filter(
                (movie, idx) => idx !== index
              );
            },
        ```
    
- 로컬 스토리지 활용
    - 로그인 및 서버 기능을 별도로 구현하지 않았기 때문에 내가 본 영화를 저장하기 위해 localStorage를 활용하였습니다.

---

## 🌏  구현 페이지

### Home

![2022-05-14_1](Project KingEY 70089696cf3340109946a833430eea1a/2022-05-14_1.png) 

### Random Page

![2022-05-14_2](Project KingEY 70089696cf3340109946a833430eea1a/2022-05-14_2.png)

### WatchList Page

1. 검색
    - 영화를 검색하고, 카드를 클릭할 경우 내가 본 영화 리스트로 이동
    
    ![May-13-2022 18-36-04.gif](Project%20KingEY%2070089696cf3340109946a833430eea1a/May-13-2022_18-36-04.gif)
    
2. 내가 본 영화 리스트에 있는 영화는 검색 결과에 나타나지 않음.
   
    ![May-13-2022 18-36-43.gif](Project%20KingEY%2070089696cf3340109946a833430eea1a/May-13-2022_18-36-43.gif)
    
3. 존재하지 않은 영화일 경우 안내 문구 등장
   
    ![May-13-2022 18-37-06.gif](Project%20KingEY%2070089696cf3340109946a833430eea1a/May-13-2022_18-37-06.gif)
    

---

## 🚨 문제 및 해결

- **경위**
    - 사용자가 이미 본 영화일 경우, 해당 영화를 검색해도 관련 영화 목록에 나타지 않도록 구현고자 함.
    - TMDB API를 통해 전달받은 데이터는 배열 내 객체로 존재하기 때문에, filter 또는 includes를 통해 이미 본 영화 리스트에 있는 영화의 경우 fitering을 하고자 함.
- **문제**
  
    ```jsx
    searchedMovieList.filter((movie) => {
            return !state.watchedMovieList.includes(movie);
          });
    ```
    
    - 위와 같은 코드로 데이터를 비교하여 필터링을 하고자 하였으나, 필터링이 되지 않는 문제가 발생
- **이유**
    - 이것은 객체 끼리의 비교이기 때문에 filter 또는 includes를 사용해도 엄격한 일치 연산자(`===`)의 경우 `false` 로 나타나게 됨.
- **해결방법**
    - 영화의 id를 저장하는 배열을 추가 생성하여 state로 관리하며, 추가적으로 영화와 비교할 경우, 해당 영화 id와 id 저장 리스트끼리 비교하여 filtering을 진행
      
        ```jsx
        setSearchedMovieList(state, searchedMovieList) {
              const filteredMovieList = searchedMovieList.filter((movie) => {
                return !state.watchedMovieIdList.includes(movie.id);
              });
              state.searchedMovieList = filteredMovieList;
              state.isSearchedMovie = filteredMovieList.length !== 0;
            },
        addWatchedMovieList(state, movie) {
              state.watchedMovieList = [...state.watchedMovieList, movie];
              state.watchedMovieIdList = [...state.watchedMovieIdList, movie.id];
        }
        ```