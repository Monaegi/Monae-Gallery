// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import app from './App'
import Router from 'vue-router'
import routes from './routes'

Vue.config.productionTip = false
Vue.prototype.axios = axios
Vue.use(Router)

const router = new Router({
  routes
})

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  template: '<app/>',
  components: { app }
})
