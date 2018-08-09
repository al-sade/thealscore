<template>
  <div id="artist-container">
    <p>summary: {{ summary[platform] }}</p>
    <p>summary: {{ platform }}</p>
<v-progress-linear
        background-color="pink lighten-3"
        color="pink lighten-1"
        value="15"
      ></v-progress-linear>

      <v-progress-linear
        background-color="blue-grey"
        color="lime"
        value="30"
      ></v-progress-linear>

      <v-progress-linear
        background-color="success"
        color="error"
        value="45"
      ></v-progress-linear>
  </div>
</template>

<script>
  /* eslint-disable */

  export default {
    props: ['summary', 'platform'],
    data() {
      return {
        test: 80,
        artist: this.$route.params.artist
      }
    }
  }
</script>

<style>
  #artist-container {
    background-color: greenyellow;
    position: fixed;
    width: 60%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
  }
</style>
