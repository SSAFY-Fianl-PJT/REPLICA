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
  state:{
    isModalOpen: false,
  },
  getters:{
  },
  mutations:{
    CLOSE_MODAL(state) {
      state.isModalOpen = false;
    },
    OPEN_MODAL(state) {
      state.isModalOpen = true;
    },
  },
  actions:{
    closeModal(context) {
      console.log("두과자")
      context.commit('CLOSE_MODAL');
    },
    openModal(context) {
      console.log("드루와")
      context.commit('OPEN_MODAL');
    },
  },
  modules: {
    user: userModule,
    article : articleModule,
    movie : movieModule
  }
})
