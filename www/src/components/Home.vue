<template>
  <div>
    <input id="tas-search" type="search" v-model="artist" />
    <button @click="getScore">GO!</button>
    <h1>{{ this.score }}</h1>
  </div>
</template>

<script>
/* eslint-disable */
  import axios from 'axios';
export default {

  data () {
    return {
      artist: '',
      score: ''
    }
  },
  methods: {
  getScore () {
      const path = "http://localhost:5000/artist/" + this.artist
      axios.get(path)
      .then(response => {
        this.score = response.data.score['artists']['items'][0]['popularity']
      })
      .catch(error => {
        console.log(error)
      })
  }
  },
  created () {
  }
}
</script>
