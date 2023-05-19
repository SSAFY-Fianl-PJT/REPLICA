<template>
  <div class="movie-list">
    <p>무비 리스트를 보여줍니다...</p>
    <p>임의로 정렬했음 - [알고리즘이 현재 없습니다.]</p>
    <MovieContent  v-if="popularmovies  && popularmovies.length > 0" :items="popularmovies"/>


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
    await this.$store.dispatch('getMovies')
    // console.log("무비랭킹",this.popularmovies) // 영화에 대한 정보 
  },
  computed:{
    popularmovies(){
      // console.log("값",this.$store.state)
      let total_movies = this.$store.state.movie.popular_movies
      return total_movies.slice(0,10)
    },
  }
}
</script>

<style scoped>
.movie-list{
  width: auto;
  
}
</style>