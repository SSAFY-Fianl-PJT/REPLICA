<template>
  <div class="movie-poster">
    <div class="image-container"  
      @mouseover="showVideo = true"
      @mouseout="showVideo = false">

      <div v-if="randomMovie"
            v-show="!showVideo">
        <img class="poster" :src="moviePoster" alt="">
      </div>
      
      <div class="video-container" v-show="showVideo" v-if="randomMovie">
        <iframe 
          class="video-iframe"
          :src="'https://www.youtube.com/embed/'+ randVideo + '?controls=0&autoplay=1&fs=0&showinfo=0&modestbranding=1&rel=0&enablejsapi=1'"
          showinfo=0
          frameborder="0"
          allowfullscreen
          modestbranding=1
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          >
        </iframe>
      </div>
    </div>
  </div>
</template>

<script>
// import TestPoster from '@/assets/TestPoster.png'
import _ from 'lodash'
// import api from '@/api/utubeapi'
// https://image.tmdb.org/t/p/w500
// const MOVIE_URL = process.env.VUE_APP_IMG_URL
// const YTB_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// const YOUTUBE_API_KEY = 'AIzaSyBlNSqg-9WQraWKrdqLdMqh-L0umq_73eA'
const MOVIE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name:'MainVideo',
  data(){
    return {
      TestPoster : null,
      randMovie : null,
      randVideo : '',
      showVideo: false,
    }
  },
  async created(){
    // const data = {
    //   q:"코코몽",
    //   part : 'snippet',
    //   type : 'video',
    //   regionCode:"KR",
    //   maxResults: 5,
    // }
    // const res = await api.get('',{params: data})
    // console.log(res.data)
    // 유튜브 영상 바로실행 https://www.youtube.com/watch?v=rdbNfNAWtQo
  },

  methods:{
    async get_movie_teaser(movie){
      let title = movie.title
      const data = {
          q:`${title} 티저`,
          part : 'snippet',
          type : 'video',
          regionCode:"KR",
          maxResults: 1,
        }
      console.log(data)
      // const res = await api.get('',{params: data})
      // console.log(res.data.items[0].id.videoId)
      // i_XHHfr8yB0
      // rMJ8qLe6q3A
        this.randMovie = movie
        this.randVideo = 'i_XHHfr8yB0'
    }
  },
  watch: {
    showVideo(newVal) {
      if (newVal) {
        this.$el.querySelector('.video-container').style.opacity = '2';
        this.$el.querySelector('.poster-container').style.opacity = '0';
      } else {
        this.$el.querySelector('.video-container').style.opacity = '0';
        this.$el.querySelector('.poster-container').style.opacity = '2';
      }
    },
  },
  computed:{
    randomMovie(){
      let randmv =  _.sample(this.$store.state.movie.popular_movies)
      if (randmv){
        console.log(randmv)
        this.get_movie_teaser(randmv)
      }
      return randmv
    },
    randomVideo(){

      return this.randVideo
    },
    moviePoster(){
      return MOVIE_URL + this.randomMovie.poster_path
    }
  }
}
</script>

<style scoped>
.movie-poster{
  width: auto;
}
.image-container {
  position: relative;
  width: auto; /*원하는 이미지 컨테이너의 너비 설정*/
  height: 700px; /*원하는 이미지 컨테이너의 최대 높이 설정*/
   /* 넘치는 이미지 부분을 숨기기 위해 overflow 속성 사용 */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.poster-container {
  position: relative;
  z-index: 1;
  transition: opacity 2s ease-in-out; /* Add transition effect */
}

.video-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  opacity: 0; /* Start hidden */
  transition: opacity 2s ease-in-out; /* Add transition effect */
}
.video-iframe {
  width: 100%;
  height: 100%;
}
</style>