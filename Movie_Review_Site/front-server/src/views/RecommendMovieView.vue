<template>
  <div>
    <div class="users-show-movie">
      <div class="recommend-tag d-none d-lg-block">
        <h2 style="font-weight: bold; text-align: left;">이 영화 어떠신가요?</h2>
      </div>
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
      console.log("resdata",res.data)
      this.recommended = res.data.movies


    }
  },
  computed:{
    recommendedMovieList(){
      return this.recommended
    }
  }
}
</script>

<style scoped>
.users-show-movie{
  display: flex;
  position: relative;
  
}
.recommend-tag{
  display: inline-block;
  position: absolute;
  
  margin-left:40px;
  margin-top: 20px;

  
}


.recommend-tag h2{
  color: #0080ffc0;
  border-bottom: 4px solid #a79600;
  padding-bottom: 5px;
  position: relative;
}

.recommend-tag h2:before{
/*     content: '';
    position: absolute;
    bottom: -20px;
    left: 50%;
    width: 20px;
    height: 20px;
    background: white;
    border-left: 4px solid #a79600;
   */
  content: ' ';
  position: absolute;
  width: 0;
  height: 0;
  right: 30px;
  bottom: -30px;
  border: 15px solid;
  border-color: #a79600 transparent transparent #a79600;
}

.recommend-tag h2:after{
/*     content: '';
    position: absolute;
    bottom: -20px;
    left: 49%;
    width: 15px;
    height: 31px;
    transform: rotate(51deg);
    border-right: 4px solid #a79600; */
    
  content: ' ';
  position: absolute;
  width: 0;
  height: 0;
  right: 27px;
  bottom: -20px;
  border: 15px solid;
  border-color: rgb(13, 13, 13, 0.95) transparent transparent rgb(13, 13, 13, 0.95);
}

</style>