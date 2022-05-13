import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const storage = {
  fetchWatchedMovieList() {
    let arr = [];
    if (localStorage.getItem("watchedMovieList")) {
      arr = JSON.parse(localStorage.getItem("watchedMovieList"));
    }
    return arr;
  },
  fetchWatchedMovieIdList() {
    let arr = [];
    if (localStorage.getItem("watchedMovieIdList")) {
      arr = JSON.parse(localStorage.getItem("watchedMovieIdList"));
    }
    return arr;
  },
};

export default new Vuex.Store({
  state: {
    watchedMovieList: storage.fetchWatchedMovieList(),
    searchedMovieList: [],
    watchedMovieIdList: storage.fetchWatchedMovieIdList(),
    isSearchedMovie: true,
  },
  getters: {},
  mutations: {
    setSearchKeyword(state, { target }) {
      state.keyword = target.value;
    },
    addMovieList(state, movie) {
      state.watchedMovieList = [...state.watchedMovieList, movie];
    },
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
    setRemainedSearchedMovieList(state, index) {
      if (index === undefined) return;
      this.commit("addWatchedMovieList", state.searchedMovieList[index]);
      state.searchedMovieList = state.searchedMovieList.filter(
        (movie, idx) => idx !== index
      );
    },
    addWatchedMovieList(state, movie) {
      state.watchedMovieList = [...state.watchedMovieList, movie];
      state.watchedMovieIdList = [...state.watchedMovieIdList, movie.id];
      localStorage.setItem(
        "watchedMovieList",
        JSON.stringify(state.watchedMovieList)
      );
      localStorage.setItem(
        "watchedMovieIdList",
        JSON.stringify(state.watchedMovieIdList)
      );
    },
  },
  actions: {
    async fetchWatchedMovie({ commit }, keyword) {
      if (!keyword.trim()) return;
      const SEARCH_URL = "search/movie";
      const params = {
        api_key: process.env.VUE_APP_API_KEY,
        language: "ko-KR",
        query: keyword,
      };
      try {
        const response = await axios.get(
          `${process.env.VUE_APP_TMDB_BASE_URL}${SEARCH_URL}`,
          { params }
        );
        commit("setSearchedMovieList", response.data.results);
      } catch (err) {
        console.log(err);
      }
    },
  },
  modules: {},
});
