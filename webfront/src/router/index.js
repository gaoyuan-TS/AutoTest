import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import login from '@/views/login/login'
import home from '@/views/home/home'
import one from '@/components/one.vue'
import two from '@/components/two.vue'



Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '/',
      component:login

    },

    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/home',
      name: 'home',
      component: home,
      children: [
        {
          path: '/one',
          name: 'one',
          component:one
        },
        {
          path: '/two',
          name: 'two',
          component: two
        }
      ]
    }
  ]
})
