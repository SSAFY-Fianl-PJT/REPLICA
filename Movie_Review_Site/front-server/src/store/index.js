import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

// import axios from 'axios'
// import router from '../router'
// import { fetchArticles } from '@/api/article'
// import api from '@/api/base'

import userModule from '@/store/modules/user'
import articleModule from '@/store/modules/article'
import movieModule from '@/store/modules/movie'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths:['user.token']
    }),
  ],
  getters:{
    getData(state){
      return (key) =>{
        return state[key]
      }
    }
  },
  modules: {
    user: userModule,
    article : articleModule,
    movie : movieModule
  }
})
