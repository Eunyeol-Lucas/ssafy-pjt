<template>
  <div>
    <h2>내가 본 영화 리스트</h2>
    <p v-if="!watchedMovieList.length">아직 본 영화가 없네요.</p>
    <p v-if="!watchedMovieList.length">검색창에 본 영화를 검색해보세요!</p>
    <div class="grid grid-cols-4 gap-4">
      <MovieCard
        v-for="movie in watchedMovieList"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

import MovieCard from "./MovieCard.vue";
export default {
  name: "WatchList",
  components: {
    MovieCard,
  },
  computed: {
    ...mapState(["watchedMovieList"]),
  },
};
</script>

<style></style>
