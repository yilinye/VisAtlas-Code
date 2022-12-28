import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import VisView from '../views/visView.vue'

const router = createRouter({
  // history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/vis',
      name: 'home',
      component: VisView
    },
    {
      path: '/',
      redirect: '/vis'
    }
  ]
})

export default router
