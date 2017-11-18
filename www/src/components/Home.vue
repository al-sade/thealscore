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
      randomNumber: 0,
      artist: '',
      score: '7'
    }
  },
  methods: {
  getScore () {
      const path = "http://localhost:5000/artist/" + this.artist
      axios.get(path)
      .then(response => {
        console.log(response.data)
        this.score = response.data
      })
      .catch(error => {
        console.log(error)
      })
  },
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
      this.randomNumber = this.getRandomInt(1, 100)
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
      .then(response => {
        this.randomNumber = response.data.randomNumber
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    this.getRandom()
  }
}
</script>
