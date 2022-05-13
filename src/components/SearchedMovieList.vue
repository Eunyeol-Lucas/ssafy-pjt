<template>
  <ul class="grid grid-cols-4">
    <MovieCard
      v-for="movie in searchedMovieList"
      :key="movie.id"
      :movie="movie"
    />
  </ul>
</template>

<script>
import MovieCard from "./MovieCard.vue";
import { mapState } from "vuex";
export default {
  name: "SearchedMovieList",
  components: {
    MovieCard,
  },
  computed: {
    ...mapState(["searchedMovieList"]),
  },
};
</script>

<style></style>
