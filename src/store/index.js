import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    watchedMovieList: [],
    searchedMovieList: [],
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
      console.log(searchedMovieList);
      state.searchedMovieList = searchedMovieList;
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
