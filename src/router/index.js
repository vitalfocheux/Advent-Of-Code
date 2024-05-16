import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/Advent-Of-Code/',
    name: 'Home',
    component: () => import('../views/Home.vue')
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

for (let i = 1; i <= 25; i++) {
  let route = {
    path: `/Advent-Of-Code/2016/${i}`,
    name: `2016-${i}`,
    component: () => import(`../views/2016/d${String(i).padStart(2, '0')}.vue`)
  };
  routes.push(route);
}

for(let i = 2015; i <= 2023; i++) {
  let route = {
    path: `/Advent-Of-Code/${i}`,
    name: `${i}`,
    component: () => import(`../views/y${i}.vue`)
  };
  routes.push(route);

  for(let j = 1; j <= 25; j++) {
    let subroute = {
      path: `/Advent-Of-Code/${i}/${j}`,
      name: `${i}-${j}`,
      component: () => import(`../views/${i}/d${String(j).padStart(2, '0')}.vue`)
    };
    routes.push(subroute);
  }
}

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router