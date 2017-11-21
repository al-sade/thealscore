<template>
  <div>
    <input id="tas-search" type="search" v-model="artist" />
    <button @click="getScore">GO!</button>
    <h1>{{ }}</h1>

    <el-progress type="circle" :percentage="this._spotifyScore"></el-progress>

  </div>
</template>

<script>
/* eslint-disable */
  import axios from 'axios';
  import VueChart from 'vue-chart-js'


  export default {

  components: {
    VueChart
  },
  data () {
    return {
      artist: '',
      spotifyScore: '',
    }
  },
  methods: {
  getScore () {
      const path = "http://localhost:5000/artist/" + this.artist
      axios.get(path)
      .then(response => {
        this.spotifyScore = response.data.score['artists']['items'][0]['popularity']
      })
      .catch(error => {
        console.log(error)
      })
  },

  },
  created () {
  },
  computed: {
    _spotifyScore: function () {
      return this.spotifyScore ? parseInt(this.spotifyScore) : 0
    }
  }
}
</script>
