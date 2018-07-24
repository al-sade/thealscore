// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
/* eslint-disable */

import Vue from 'vue'
import App from './App'
import router from './router'


new Vue({
  el: '#app',
  router,
  template: '<App/>',
  render: h => h(App)
});
