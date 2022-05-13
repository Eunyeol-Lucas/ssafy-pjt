<template>
  <div>
    <WatchListForm />
    <SearchedMovieList />
    <WatchList />
  </div>
</template>

<script>
import WatchListForm from "../components/WatchListForm.vue";
import SearchedMovieList from "../components/SearchedMovieList.vue";
import WatchList from "../components/WatchList.vue";
export default {
  name: "App",
  components: {
    WatchListForm,
    SearchedMovieList,
    WatchList,
  },
};
</script>

<style></style>
