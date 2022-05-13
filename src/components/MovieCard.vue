<template>
  <li v-if="movie" class="hover:scale-105 transition-all">
    <div class="rounded-xl border-2">
      <div class="h-44 overflow-hidden rounded-t-lg">
        <img
          :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
          :alt="movie.title"
          width="400"
          class="w-full"
        />
      </div>
      <div class="overflow-hidden h-48">
        <p>{{ movie.title }}</p>
        <p class="text-ellipsis overflow-hidden">{{ movie.overview }}</p>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: {
      type: Object,
      required: false,
    },
  },
};
</script>

<style></style>
