import Vue from 'vue'
import VueRouter from 'vue-router'

import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'


import MainView from '@/views/MainView'
import SignUpView from '@/views/SignUpView'
import SignInView from '@/views/SignInView'
import MovieViewTest from '@/views/MovieViewTest'
import SearchView from '@/views/SearchView'

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
    path: '/search',
    name: 'SearchView',
    component: SearchView,
    beforeEnter: (to, from, next) => {
      if (to.path === '/search') {
        next();
      } else {
        next({ name: 'SearchView' });
      }
    }
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
