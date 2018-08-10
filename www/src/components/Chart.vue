<template>
  <section class="charts">
    <vue-highcharts :options="pieOptions" ref="pieChart"></vue-highcharts>

  </section>
</template>

<script>
  /* eslint-disable */
  import VueHighcharts from 'vue2-highcharts'

  export default {
    components: {
      VueHighcharts
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
                    click: ({point}) => {
                      this.$emit('pieClicked', point.name);
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
