<template>
  <div>
    <div class="users-show-movie">
      이 영화 어떠신가요?
      <movie-main-video :items="recommendedMovieList"></movie-main-video>
    </div>
    <div class="users-recommended-movie">
      
      
      <RecommendMovie :items="recommendedMovieList"/>
    </div>
  </div>
</template>

<script>
import RecommendMovie from '@/components/movie/RecommendMovie.vue';
import MovieMainVideo from '@/components/movie/MovieMainVideo.vue'
import {fetchRecommend} from '@/api/movie'

export default {
  name:'RecommendMovieView',
  components:{
    RecommendMovie,
    MovieMainVideo
  },
  data(){
    return {
      username : null,
      recommended : null,
    }
  },
  async created(){
    await this.$store.dispatch('get_usr_name')
    await this.recommendMovie()
  },
  methods:{
    async recommendMovie(){
      
      
      const username = this.$store.state.user.info.username
      this.username = username

      const res = await fetchRecommend({username})

      this.recommended = res.data

    }
  },
  computed:{
    recommendedMovieList(){
      return this.recommended
    }
  }
}
</script>

<style>

</style>