<template>
  <div class="movie-poster">
    <div class="image-container" >
      <img class="poster" :src=TestPoster alt="">
    </div>
  </div>
</template>

<script>
// import TestPoster from '@/assets/TestPoster.png'
// https://image.tmdb.org/t/p/w500
// const MOVIE_URL = process.env.VUE_APP_IMG_URL
const MOVIE_URL = 'https://image.tmdb.org/t/p/w500'
export default {
  name:'MainVideo',
  data(){
    return {
      TestPoster : null,
      randMovie : null
    }
  },
  methods:{

  },
  async created(){
    await this.$store.dispatch('getMovies')
    this.randMovie = this.randomMovie
    console.log("이게뭐야",this.randMovie)
    this.TestPoster = this.moviePoster
  },
  computed:{
    randomMovie(){
      return this.$store.state.movie.movies
    },

    moviePoster(){
      return MOVIE_URL + this.randomMovie[0].poster_path
    }
  }
}
</script>

<style>
.movie-poster{
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
}

.poster {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지가 요소를 완전히 덮도록 크기 조절 */
  object-position: 50% 15%; /* 이미지를 요소의 중앙에 위치 */
  
}
</style>