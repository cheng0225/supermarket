import Vue from 'vue'
import Router from 'vue-router'

import login from '@/views/users/login'
import index from '@/views/users/index'
import register from '@/views/users/register'

import things from '@/views/home/things'
import merchants from '@/views/home/merchants'
import logs from '@/views/home/logs'

import map from '@/views/home/map'


Vue.use(Router)

// 多余跳转控制台报错解决
//获取原型对象上的push函数
const originalPush = Router.prototype.push
//修改原型对象中的push方法
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}


export default new Router({
  // mode: 'history',
  routes: [
    // users
    {
      path: '/users/index',
      component: index
    },
    {
      path: '/users/login',
      component: login
    },
    {
      path: '/users/register',
      component: register
    },

    //  home
    {
      path: '/home/things',
      component: things
    },
    {
      path: '/home/merchants',
      component: merchants
    },
    {
      path: '/home/logs',
      component: logs
    },
    {
      path: '/map',
      component: map
    }
  ]
})
