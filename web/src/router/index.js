import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ChooseTag from '../components/ChooseTag.vue'

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
    component: ChooseTag
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
