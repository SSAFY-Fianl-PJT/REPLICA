import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import SignInView from '@/views/SignInView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView 
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
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path === from.path) {
    next(false); // 중복 경로 이동을 취소합니다.
  } else {
    next(); // 다른 경로로의 이동을 허용합니다.
  }
});

export default router
