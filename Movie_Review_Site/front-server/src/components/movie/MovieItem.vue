<template>
  <div>
    <div class="movie-poster-container">
      {{ item.title }}
      <div class="image-container" :style="backgroundImageStyle">
 
      </div>
    </div>
    <div class="information-block">
      <div class="movie-summary">
        <div class="summary">
          <span>
            {{ item.overview }}
          </span>
        </div>
        <div class="release_date">
          <span>개봉날짜 : </span>
          <span>
            {{ item.release_date }}
          </span>
        </div>
      </div>
      <div class="movie-inform">
        <div class="movie-actors">
          <span>출연진 : </span>
          <span v-for="(actor, idx) in item.actors" :key="idx">
            {{ actor }}|
          </span>
        </div>
        <div class="movie-genre">
          <span>장르 : </span>
          <span v-for="(genre, idx) in item.genres" :key="idx">
            {{ genre.genre_name }}|
          </span>
        </div>
        <div class="movie-score">
          <div class="TMDB-popularity">
            <span>TMDB 스코어 : </span>
            <span>
              {{ item.popularity }}
            </span>
          </div>
          <div class="TMDB-score">
            <span>TMDB 평점 : </span>
            <span>
              {{ item.score_average }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const MOVIE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name:'MovieItem',
  props:{
    item:Object
  },
  data(){
    return {
      // MoviePoster : null,
    }
  },
  methods:{
    
  },
  async created(){
    console.log("짜잔",this.item)
  },
  computed:{
    randomMovie(){
      return this.$store.movie.state.movies
    },

    backgroundImageStyle(){
      return {
        background: `linear-gradient(
          to bottom,
          rgba(255,255,255,0) 10%,
          rgba(255,255,255,0.5) 25%,
          rgba(255,255,255,0.7) 40%,
          rgba(255,255,255,1) 50%
        ), url(${MOVIE_URL + this.item.poster_path})`,
        backgroundSize: `cover`,
        backgroundRepeat: 'no-repeat',
      }
    }
  }
}
</script>

<style scoped>
.movie-poster-container{
  width: 100%;
}
.image-container {
  width: 100%; /*원하는 이미지 컨테이너의 너비 설정*/
  height: 700px; /*원하는 이미지 컨테이너의 최대 높이 설정*/
   /* 넘치는 이미지 부분을 숨기기 위해 overflow 속성 사용 */

  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;  

  object-position: 50% 0%; /* 이미지를 요소의 중앙에 위치 */
}


</style>