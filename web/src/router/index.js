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
    component: () => import('@/components/EnterPosition.vue')
  },
  {
    path: '/chooseTag',
    name: 'ChooseTag',
    component: () => import('@/components/ChooseTag.vue')
  },
  {
    path: '/routes',
    name: 'Routes',
    component: () => import('@/components/Routes.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
