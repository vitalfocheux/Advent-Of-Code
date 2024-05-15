import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/Advent-Of-Code/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/Advent-Of-Code/2015',
    name: '2015',
    component: () => import('../views/y2015.vue')
  },
  {
    path: '/Advent-Of-Code/2015/1',
    name: '2015-1',
    component: () => import('../views/2015/d01.vue')
  },
  {
    path: '/Advent-Of-Code/2016',
    name: '2016',
    component: () => import('../views/y2016.vue')
  },
  {
    path: '/Advent-Of-Code/2017',
    name: '2017',
    component: () => import('../views/y2017.vue')
  },
  {
    path: '/Advent-Of-Code/2018',
    name: '2018',
    component: () => import('../views/y2018.vue')
  },
  {
    path: '/Advent-Of-Code/2019',
    name: '2019',
    component: () => import('../views/y2019.vue')
  },
  {
    path: '/Advent-Of-Code/2020',
    name: '2020',
    component: () => import('../views/y2020.vue')
  },
  {
    path: '/Advent-Of-Code/2021',
    name: '2021',
    component: () => import('../views/y2021.vue')
  },
  {
    path: '/Advent-Of-Code/2022',
    name: '2022',
    component: () => import('../views/y2022.vue')
  },
  {
    path: '/Advent-Of-Code/2023',
    name: '2023',
    component: () => import('../views/y2023.vue')
  },
]

for (let i = 2; i <= 25; i++) {
  let route = {
    path: `/Advent-Of-Code/2015/${i}`,
    name: `2015-${i}`,
    component: () => import(`../views/2015/d${String(i).padStart(2, '0')}.vue`)
  };
  routes.push(route);
}

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router