<template>
  <div id="spotify-container">
    <h1>hi from spotify</h1>
    <p>{{ summary }}</p>
  </div>
</template>

<script>

  export default {
    props: ['summary'],
    data () {
      return {

      }
    }
  }
</script>

<style scoped>
</style>
