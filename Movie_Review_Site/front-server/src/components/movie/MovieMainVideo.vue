<template>
  <div class="movie-poster">
    <div class="movie-container"  
      @mouseover="showVideo = true"
      @mouseout="showVideo = false">

      <div class="image-container" 
        v-if="randomMovie"

        :style="{ opacity: showVideo ? 0 : 1 }">
        <img class="poster" :src="moviePoster" alt="">
      </div>
      
      <div class="video-container" 
          v-if="randomMovie"

          :style="{ opacity: showVideo ? 1 : 0 }">
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
      <div class="inform-container d-none d-lg-block">
        <h3 style="font-weight: bold; text-align: left;">{{randMovie.title}}</h3>
        <div class="mv_genres-container">
          <div v-for="(mv_gener, idx) in randMovie.genres" :key='idx'>
            {{mv_gener.genre_name}}
          </div>
        </div>
        <div class="overview-container" style="text-align: left;" >
          <span v-if="randMovie.overview" class="ellipsis">
            {{slicedOverview}}
          </span>
          <span v-else> 영화를 보고 리뷰를 남겨주세요! </span>
        </div>

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
  props:{
    items:Array,
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
        try{
          this.$el.querySelector('.video-container').style.opacity = '2';
        }catch{
          this.$el.querySelector('.poster-container').style.opacity = '0';
        }
      } else {
        try{
          this.$el.querySelector('.video-container').style.opacity = '0';
        }catch{
          this.$el.querySelector('.poster-container').style.opacity = '2';
        }
      }
    },
  },
  computed:{
    randomMovie(){
      console.log("이거 돌아가냐")
      let randmv = null
      if (!this.items || this.items.length == 0){
        randmv =  _.sample(this.$store.state.movie.popular_movies)
      }
      else{
        
        randmv = _.sample(this.items)
      }
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
    },
    slicedOverview() {
    if (this.randMovie.overview && this.randMovie.overview.length > 100) {
      return this.randMovie.overview.slice(0, 150) + '...';
    } else {
      return this.randMovie.overview;
    }
  }
  }
}
</script>

<style scoped>
.movie-poster{
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}
.mv_genres-container{
  display: flex;
  flex-direction: row;
}
.mv_genres-container > div{
  margin-right: 15px;
}
.movie-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 700px;
  overflow: hidden;
  position: relative;
}
.inform-container{
  position: absolute;
  bottom: 0;
  left: 0;
  z-index: 3;
  /* Additional style */
  width: 550px;
  padding-bottom: 20px;
  padding-left : 50px;
  color: #fff;
  
}
.ellipsis {
  display: block;
  overflow: hidden;
  /* white-space: nowrap;  */
  text-overflow: ellipsis; /* 텍스트가 너무 길면 ...으로 표시 */
  width: 500px; /* 너비를 조정하면서 최적의 값을 찾아보세요 */
}

.image-container, .video-container {
  display: flex;
  position: absolute;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  transition: opacity 1s ease-in-out;
}


.movie-container:hover .image-container {
  opacity: 0;
}
.movie-container:hover .video-container {
  opacity: 1;
}

.video-iframe {
  width: 100%;
  height: 100%;
}
</style>