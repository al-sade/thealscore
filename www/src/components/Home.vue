<template>
  <div>
    <h1>Home page</h1>

    <input class="tas-search" type="search" v-model="artist"/>
    <button class="tas-search" @click="getScore">GO!</button>
    <p>spotify score: {{spotifyScore}}</p>
    <chart ref="chart"></chart>
  </div>
</template>

<script>
  /* eslint-disable */
  import axios from 'axios';

  export default {
    components: {
      "chart": require("./Chart.vue").default
    },
    data() {
      return {

        dataFormat: 'json',
        artist: '',
        spotifyScore: '',
        showPie: false,

      }
    },
    methods: {
      getScore() {
        const path = "http://localhost:5000/artist/" + this.artist
        axios.get(path)
          .then(response => {
            this.spotifyScore = response.data.score;
            this.showPie = true;
            console.log(this.spotifyScore)
          })
          .catch(error => {
            console.log(error)
          })
      },

    },
    created() {
    },
    computed: {
      _spotifyScore: function () {
        return this.spotifyScore ? parseInt(this.spotifyScore) : 0
      }
    }
  }
</script>

<style>

</style>
