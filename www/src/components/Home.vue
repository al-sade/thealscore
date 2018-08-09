<template>
  <div>
    <input class="tas-search" type="search" v-model="artist"/>
    <button class="tas-search" @click="getSummary">GO!</button>

    <chart v-if="showPie" ref="chart" :score="grades" @pieClicked="pieClicked($event)"></chart>

    <div id="overlay" v-show="showOverlay">
      <button @click="showOverlay = !showOverlay">close</button>
    </div>
    <overlay :summary="summary" :platform="platform" v-show="showOverlay"></overlay>
  </div>
</template>

<script>
  /* eslint-disable */
  import axios from 'axios'
  import Chart from './Chart'
  import Overlay from './Overlay'

  export default {
    components: {
      chart: Chart,
      overlay: Overlay
    },
    data() {
      return {
        dataFormat: 'json',
        artist: 'u2',
        platform: '',
        summary: [],
        grades:[],
        spotifyScore: '',
        showPie: false,
        showOverlay: false
      }
    },
    methods: {
      getSummary() {
        const path = "http://localhost:5000/artist/" + this.artist;
        axios.get(path)
          .then(res => {
            this.summary = res.data.summary;
            this.setGrades(this.summary);
            this.showPie = true;
          })
          .catch(error => {
            console.log(error)
          })
      },
      setGrades(summary){
        this.grades['spotify'] = summary.spotify.popularity;
      },
      pieClicked(e) {
        this.showOverlay = true;
        this.platform = e.toLowerCase();
      }
    }
  }
</script>

<style scoped>
    #overlay {
        position: fixed; /* Sit on top of the page content */
        width: 100%; /* Full width (cover the whole page) */
        height: 100%; /* Full height (cover the whole page) */
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5); /* Black background with opacity */
        z-index: 1; /* Specify a stack order in case you're using a different order for other elements */
        cursor: pointer; /* Add a pointer on hover */
    }
</style>
