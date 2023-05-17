import { fetchMovies /*, getMovie_Detail*/ } from '@/api/movie'
// import _ from 'lodash'

export default {
  state : {
      movies: [],
      random_movie : null
  },
  mutations:{
      GET_MOVIES(state, movies) {
          state.movies = movies
      },
  },
  actions:{
      async getMovies(context) {
        
        await fetchMovies()
          .then((res) => {
            context.commit('GET_MOVIES', res.data)
          })
          .catch((err) => {
          console.log(err)
          })
      },
  }
}