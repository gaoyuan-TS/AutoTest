import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import login from '@/views/login/login'
import home from '@/views/home/home'




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
          component: () => import('../components/one.vue')
        },
        {
          path: '/two',
          name: 'two',
          component: () => import('../components/one.vue')
        }
      ]
    }
  ]
})
