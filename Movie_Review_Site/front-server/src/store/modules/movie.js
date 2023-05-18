import { fetchMovies /*, getMovie_Detail*/ } from '@/api/movie'
// import _ from 'lodash'

export default {
  state : {
      movies: [],
      test_movie : null
  },
  getters:{

  },
  mutations:{
      GET_MOVIES(state, movies) {
          state.movies = movies
          state.test_movie = movies[0]
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