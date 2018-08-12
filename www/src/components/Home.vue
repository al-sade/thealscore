<template>
  <div id="home">
        <h1>The Al Score</h1>
    <el-input class="tas-search" type="search" v-model="artist">
          <el-button slot="append" icon="el-icon-search" @click="getSummary"></el-button>
    </el-input>

      <el-collapse-transition>
      <keep-alive>
        <chart v-if="showPie" ref="chart" :score="_grades" @pieClicked="pieClicked($event)"></chart>
      </keep-alive>
    </el-collapse-transition>

    <transition name="el-fade-in-linear">
      <overlay :summary="_platformSummary" :platform="platform" v-if="showOverlay" @closeOverlay="closeOverlay">
      </overlay>
    </transition>
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
        score: [],
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
            this.score = this.summary;
            this.showPie = true;
          })
          .catch(error => {
            console.log(error)
          })
      },
      pieClicked(e) {
        this.showOverlay = true;
        this.showPie = false;
        this.platform = e.toLowerCase();
      },
      closeOverlay () {
        this.showOverlay = false;
        this.showPie = true;
      }
    },
    computed: {
      _grades(){
        let grades = [];

        try {
          grades['spotify'] = this.summary['spotify']['spotify_score']['popularity'];
        } catch (err){
          console.log(err)
        }
        return grades;
      },
      _platformSummary () {
        if (this.platform) {
          return this.summary[this.platform]
        }
        return '';
      }
    }
  }
</script>

<style scoped>
    .el-input {
      width: 400px;
    }

</style>
