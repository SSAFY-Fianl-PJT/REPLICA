import { fetchMovies, fetchSearchMovies, getMovie_Detail } from '@/api/movie'
// import _ from 'lodash'

export default {
  state : {
    popular_movies: [],
    upcoming_movies: [],
    wishlist: [],
    
    movie_detail : null,
    search_results : [],
    search_target : null,
  },
  getters:{

  },
  mutations:{
      GET_MOVIES(state, movies) {
          const {popular_movies, upcoming_movies, wishlist} = movies
          console.log(movies)
          state.popular_movies = popular_movies
          state.upcoming_movies = upcoming_movies
          state.wishlist = wishlist

      },
      SEATCH_RESULT(state, results){
        console.log("검색결과 ", results)
        state.search_results = results
      },
      SEATCHING(state, name){
        state.search_target = name
      },
      GET_DETAIL(state,data){
        state.movie_detail = data
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
      },
      getMV_Detail(context, movie_id){
        
        getMovie_Detail(movie_id)
        .then((res) =>{
          context.commit('GET_DETAIL',res.data)
        })
      }
  }
}