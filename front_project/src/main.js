// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import app from './App'
import Router from 'vue-router'


Vue.config.productionTip = false
Vue.prototype.axios = axios

const scheduler = app.components.scheduler

const routes = [
  {path: '/scheduler', component: scheduler}
]

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
