// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
import VueParticles from 'vue-particles'
import "@/assets/iconfont/iconfont.css";
import Axios from 'axios'
import Global from '../static/global'
import qs from 'querystring'// import login from './views/login/login'
// import home from './views/home/Home'


Vue.use(VueParticles)
Vue.use(ElementUI)
Vue.prototype.$axios=Axios
Vue.config.productionTip = false
Vue.prototype.Global = Global

/* eslint-disable no-new */
new Vue({
  el:'#app',
  router,
  components:{App},
  template: '<App/>'
})
