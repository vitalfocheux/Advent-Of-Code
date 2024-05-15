import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/Advent-Of-Code/2015/1',
    name: '2015-1',
    component: () => import('../views/2015/d01.vue')
  },
  {
    path: '/Advent-Of-Code/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/Advent-Of-Code/2015',
    name: '2015',
    component: () => import('../views/2015/y2015.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router