<template>
  <div id="artist-container">
    <p>Artist Name: {{artist}}</p>
  </div>
</template>

<script>
  /* eslint-disable */

  export default {
    data() {
      return {
        artist: this.$route.params.artist
      }
    }
  }
</script>

<style>

</style>
