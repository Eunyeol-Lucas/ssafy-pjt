<template>
  <div id="app">
    <nav>
      <router-link :to="{name: 'home'}">Home</router-link> |
      <router-link :to="{name: 'random'}">Random</router-link>
      <router-link :to="{name: 'watchList'}"></router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>

</style>
