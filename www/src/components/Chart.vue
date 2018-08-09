<template>
  <section class="charts">
    <vue-highcharts :options="pieOptions" ref="pieChart"></vue-highcharts>

    <GlobalEvents @keyup="pieClicked"/>
  </section>
</template>

<script>
  /* eslint-disable */
  import VueHighcharts from 'vue2-highcharts'
  import GlobalEvents from 'vue-global-events'

  export default {
    components: {
      VueHighcharts,
      GlobalEvents
    },
    props: ['score', 'show'],

    data() {
      return {
        pieOptions:
          {
            chart: {
              type: "pie",
              options3d: {
                enabled: false,
                alpha: 45
              }
            },
            plotOptions: {
              pie: {
                innerSize: 100,
                depth: 45
              },
              series: {
                cursor: 'pointer',
                point: {
                  events: {
                    click: function () {
                      let e = new KeyboardEvent('keyup',{'keyCode':32,'which':32, 'key': this.name});
                      document.dispatchEvent(e);
                    }
                  }
                }
              }
            },
            series: [
              {
                name: "Platform Score",
                data: [
                  ["Spotify", 3],
                  ["Deezer", 1]
                ]
              }
            ]
          }
      }
    },
    methods: {
      pieClicked(e){
        this.$emit('pieClicked', e.key);
      }
    },
    watch: {
      score: function (value) {
        const that = this;
        that.$refs.pieChart.chart.series[0].setData([
          ["Spotify", this.score.spotify],
          ["Deezer", 100 - this.score.spotify]])
      }
    }
  }
</script>

<style>

</style>
