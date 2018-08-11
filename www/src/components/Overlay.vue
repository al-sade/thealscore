<template>
    <div id="overlay">
      <div id="artist-container">
        <el-button @click="closeOverlay" type="text">
                  <i class="el-icon-close"></i>
          </el-button>
        <component :is="platform" :summary="summary"></component>
      </div>
    </div>
</template>

<script>
  /* eslint-disable */
  import Spotify from './platforms/Spotify'
  import Deezer from './platforms/Deezer'

  export default {
    props: ['summary', 'platform'],
    components : {
      Spotify,
      Deezer
    },
    data() {
      return {
        artist: this.$route.params.artist
      }
    },
    methods: {
      closeOverlay() {
        this.$emit('closeOverlay');
      }
    }
  }
</script>

<style>
  #artist-container {
    background-color: greenyellow;
    position: fixed;
    width: 60%;
    height: 580px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
    border-radius: 5px;
    box-shadow: 1px 1px 1px #222;
  }

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

  button{
    float: right;
  }
</style>
