<template>
  <div>
    <p>무비 리스트를 보여줍니다...</p>
    <p>임의로 정렬했음 - [알고리즘이 현재 없습니다.]</p>
    <MovieContent :items="rankedMovies"/>


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
          console.log("하위",this.rankedMovies)
      }
  },
  async created(){
    await this.$store.dispatch('getMovies')
    console.log("무비랭킹",this.rankedMovies) // 영화에 대한 정보 
  },
  computed:{
    rankedMovies(){
      let total_movies = this.$store.state.movie.movies
      return total_movies.slice(0,10)
    },
  }
}
</script>

<style>

</style>