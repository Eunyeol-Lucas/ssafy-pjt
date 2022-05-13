<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'random' }">Random</router-link>
      <router-link :to="{ name: 'watchList' }"></router-link>
    </nav>
    <router-view />
  </div>
</template>
<script>
export default {
  data() {
    return {
      API_KEY: "eba1de962633cb7eb4cb4be4665bf5ba",
    };
  },
};
</script>

<style></style>
