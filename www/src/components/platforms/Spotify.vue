<template>
  <div id="spotify-container">
    <h1>spotify</h1>
    <a :href="_summary['url']">link to page</a>
    <p>Number of followers: {{ _summary.followers }}</p>
    <ul>
      <li v-for="genre in _summary.genres">{{ genre }}</li>
    </ul>
    <h2>{{ _summary.name}}</h2>
    <h1>score: {{ _summary.popularity }}</h1>

      <el-carousel indicator-position="outside">
        <el-carousel-item v-for="key,imgSrc in _summary.images" :key="key">
              <img :src="imgSrc" class="image">
        </el-carousel-item>
      </el-carousel>

  </div>
</template>

<script>

  export default {
    props: ['summary'],
    data () {
      return {

      }
    },
    computed: {
        _summary () {
          let data = this.summary;
          let res = {};

          if (data){
            res['url'] = data['external_urls']['spotify'];
            res['followers'] = data['followers']['total'];
            res['genres'] = data['genres'];
            res['name'] = data['name'];
            res['popularity'] = data['popularity'];
            res['images'] = data['images'].map(x => x.url);
          }

          return res;
        }
      }
  }
</script>

<style scoped>
</style>
