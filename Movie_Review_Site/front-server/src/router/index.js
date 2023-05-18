import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import SignInView from '@/views/SignInView'
import MovieViewTest from '@/views/MovieViewTest'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView 
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/signin',
    name: 'SignInView',
    component: SignInView
  },
  {
    path: '/test',
    name: 'MovieViewTest',
    component: MovieViewTest
  },

  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  
  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView
  },
  
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
export default router
