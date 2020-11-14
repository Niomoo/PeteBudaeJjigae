import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/positioning',
    name: 'Positioning',
    component: () => import('@/components/Positioning.vue')
  },
  {
    path: '/positioning/enterPosition',
    name: 'EnterPosition',
    component: () => import('@/components/Positioning/EnterPosition.vue')
  },
  {
    path: '/positioning/getPosition',
    name: 'GetPosition',
    component: () => import('@/components/Positioning/GetPosition.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
