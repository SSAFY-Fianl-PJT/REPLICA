<template>
  <div class="movie-list">

    <h3>💥현재 인기 영화💥</h3>
    <MovieContent  v-if="popularmovies  && popularmovies.length > 0" :items="popularmovies"/>
    <h3>개봉 예정 영화 Comming Soon</h3>
    <MovieContent  v-if="upcomingmovies  && upcomingmovies.length > 0" :items="upcomingmovies"/>
    <h3>🙆‍♀️내가 찜한 영화🙆‍♂️</h3>
    <MovieContent  v-if="wishlist  && wishlist.length > 0" :items="wishlist"/>
  </div>
</template>


<script>
import MovieContent from '@/components/movie/MovieContent.vue';

export default {
  name:"MovieList",
  components:{
    MovieContent
  },
  methods:{

  },
  async created(){
    // await this.$store.dispatch('getMovies')
    // console.log("무비랭킹",this.popularmovies) // 영화에 대한 정보 
  },
  computed:{
    popularmovies(){
      console.log("유명")
      return this.$store.state.movie.popular_movies
    },
    upcomingmovies(){
      console.log("개봉예정")
      return this.$store.state.movie.upcoming_movies
    },
    wishlist(){
      console.log("위시")
      console.log(this.$store.state.movie.wishList)
      return this.$store.state.movie.wishList
    },
  }
}
</script>

<style scoped>
.movie-list{
  width: auto;
  margin-top: 30px;
}
</style>