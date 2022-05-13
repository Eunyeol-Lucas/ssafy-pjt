<template>
  <div>
    <h2 v-if="searchedMovieList.length">관련된 영화</h2>
    <p v-if="!isSearchedMovie">검색어와 관련된 영화가 없습니다.</p>
    <ul class="grid grid-cols-4 gap-3">
      <MovieCard
        v-for="(movie, index) in searchedMovieList"
        :key="movie.id"
        :movie="movie"
        :index="index"
      />
    </ul>
  </div>
</template>

<script>
import MovieCard from "./MovieCard.vue";
import { mapMutations, mapState } from "vuex";
export default {
  name: "SearchedMovieList",
  components: {
    MovieCard,
  },
  methods: {
    ...mapMutations(["resetSearchedMovieList"]),
  },
  computed: {
    ...mapState(["searchedMovieList", "isSearchedMovie"]),
  },
};
</script>

<style></style>
