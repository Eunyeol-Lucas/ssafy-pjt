<template>
  <div class="w-auto my-5 relative">
    <form @submit.prevent="getMovieList" class="mx-auto w-full">
      <label for="watch-list-input"></label>
      <input
        class="border-2 rounded-full h-11 bg-gray-100 w-full border-none focus:outline-none focus:bg-gray-200 transition px-10"
        type="text"
        id="watch-list-input"
        v-model="keyword"
      />
      <button
        type="button"
        class="bg-gray-400 w-16 h-11 absolute right-0.5 rounded-r-full"
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
