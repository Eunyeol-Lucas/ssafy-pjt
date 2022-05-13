<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'random' }">Random</router-link> |
      <router-link :to="{ name: 'watchList' }">WatchList</router-link>
    </nav>
    <router-view />
  </div>
</template>
<script>
export default {

  mounted() {
    console.log(process.env.VUE_APP_API_KEY);
  },
};
</script>

<style></style>
