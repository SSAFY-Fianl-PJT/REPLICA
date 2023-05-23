<template>
  <div class="movie-list">
    <p>무비 리스트를 보여줍니다...</p>
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
      handler(){
          console.log("하위",this.popularmovies)
      }
  },
  async created(){
    // await this.$store.dispatch('getMovies')
    // console.log("무비랭킹",this.popularmovies) // 영화에 대한 정보 
  },
  computed:{
    popularmovies(){

      return this.$store.state.movie.popular_movies
    },
    upcomingmovies(){
      return this.$store.state.movie.upcoming_movies
    },
    wishlist(){
      return this.$store.state.movie.wishlist
    },
  }
}
</script>

<style scoped>
.movie-list{
  width: auto;
  
}
</style>