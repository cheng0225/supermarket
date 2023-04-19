// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import store from './store'

Vue.config.productionTip = false

import './assets/css/样式1.css'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)


import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
Vue.use(Buefy)

/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  // store,
  render: h => h(App)
}).$mount('#app')