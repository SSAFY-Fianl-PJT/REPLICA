<template>
  <div>
    <div class="users-show-movie">
      이 영화 어떠신가요?
    </div>
    <div class="users-recommended-movie">
      
      
      <RecommendMovie :items="recommendedMovieList"/>
    </div>
  </div>
</template>

<script>
import RecommendMovie from '@/components/movie/RecommendMovie.vue';
// import MovieContent from '@/components/movie/MovieContent.vue'
import {fetchRecommend} from '@/api/movie'

export default {
  name:'RecommendMovieView',
  components:{
    RecommendMovie,
    // MovieContent
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