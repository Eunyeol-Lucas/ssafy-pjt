<template>
  <div class="mx-auto">
    <form @submit.prevent="getMovieList">
      <label for="watch-list-input"></label>
      <input
        class="border-2 rounded-lg border-red-400 bg-red-500 w-96"
        type="text"
        id="watch-list-input"
        v-model="keyword"
      />
      <button
        type="button"
        class="bg-blue-500 rounded-lg w-11 h-8"
        @click="getMovieList"
      >
        검색
      </button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";
export default {
  name: "WatchListForm",
  data() {
    return {
      keyword: "",
    };
  },
  methods: {
    ...mapMutations(["setSearchKeyword"]),
    ...mapActions(["fetchWatchedMovie"]),
    clearInput() {
      this.keyword = "";
    },
    getMovieList() {
      this.fetchWatchedMovie(this.keyword);
      this.clearInput();
    },
  },
};
</script>

<style></style>
