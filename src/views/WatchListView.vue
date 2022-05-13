<template>
  <div>
    <WatchListForm />
    <WatchList />
  </div>
</template>

<script>
import WatchListForm from "../components/WatchListForm.vue";
import WatchList from "../components/WatchList.vue";
export default {
  name: "App",
  components: {
    WatchListForm,
    WatchList,
  },
};
</script>

<style></style>
