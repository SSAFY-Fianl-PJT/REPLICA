import { fetchMovies, fetchSearchMovies /*, getMovie_Detail*/ } from '@/api/movie'
// import _ from 'lodash'

export default {
  state : {
    popular_movies: [],
    upcomming_movies: [],
    wishlist: [],
    test_movie : null,
    search_results : [],
    search_target : null,
  },
  getters:{

  },
  mutations:{
      GET_MOVIES(state, movies) {
          const {popular_movies, upcoming_movies, wishlist} = movies
          state.popular_movies = popular_movies
          state.upcoming_movies = upcoming_movies
          state.wishlist = wishlist
          state.test_movie = movies[0]
      },
      SEATCH_RESULT(state, results){
        console.log("검색결과 ", results)
        state.search_results = results
      },
      SEATCHING(state, name){
        state.search_target = name
      }
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
      async searchMovies(context, items){
        console.log("찾는중 슈댕..",items)
        const search_results =  await fetchSearchMovies({title: items})
        context.commit('SEATCH_RESULT', search_results)
        context.commit('SEATCHING', items)
      }
  }
}