import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

// import axios from 'axios'
// import router from '../router'
// import { fetchArticles } from '@/api/article'
// import api from '@/api/base'

import userModule from '@/store/modules/user'
import articleModule from '@/store/modules/article'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths:['user.token']
    }),
  ],
  modules: {
    user: userModule,
    article : articleModule
  }
})
