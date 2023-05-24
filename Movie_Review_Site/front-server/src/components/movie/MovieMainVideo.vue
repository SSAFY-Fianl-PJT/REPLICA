<template>
  <div class="movie-poster">
    <div class="movie-container"  
    @mouseover="showVideo = true"
    @mouseout="showVideo = false">
    
      <div class="gradient-overlay"></div>
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
      
      

      <blockquote class="bluejeans inform-container d-none d-lg-block">
        <h2><span class="Cbluejeans" style="font-weight:bolder;">{{randMovie.title}}</span><img class="information-img popover-img" :src="inforImg" alt="inform" style="width:30px;" @click="toMovieDetail"></h2>

        <div class="mv_genres-container" style="font-size: 20px;">
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
      </blockquote>
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
      inforImg: require('@/assets/inform.png'),
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
    },
    toMovieDetail(){
      this.$router.push({name: 'MovieViewTest',params : {id:this.randMovie.id}})
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
@import url('https://fonts.googleapis.com/css?family=Montez');
@import url(https://fonts.googleapis.com/css?family=Francois+One);
.movie-poster{
  position: relative;
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
  position: relative;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 700px;
  overflow: hidden;
  
 
}

.gradient-overlay{
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  pointer-events: none;
  background: linear-gradient(to bottom, rgb(78, 92, 170, 0), rgb(13, 13, 13, 0.95)); 
  z-index: 1;
}

.inform-container{
  position: absolute;
  bottom: 0;
  left: 0;
  z-index: 3;
  /* Additional style */
  width: 580px;
  padding-bottom: 20px;
  padding-left : 50px;
  color: #fff;
  margin-left:40px;
}


.ellipsis {
  display: block;
  overflow: hidden;
  /* white-space: nowrap;  */
  text-overflow: ellipsis; /* 텍스트가 너무 길면 ...으로 표시 */
  width: 500px; /* 너비를 조정하면서 최적의 값을 찾아보세요 */
}

.overview-container{
  margin-top: 10px;
  font-family: 'Francois One', sans-serif;
}
blockquote{
  display:block;
  background: rgb(13, 13, 13, 0);
  padding: 15px 20px 15px 45px;
  margin: 0 0 20px;
  position: relative;
  
  /*Font*/
  font-family: Georgia, serif;
  font-size: 14px;
  line-height: 1.2;
  color: #fff;

  /*Box Shadow - (Optional)*/
  -moz-box-shadow: 2px 2px 15px #ccc;
  -webkit-box-shadow: 2px 2px 15px #ccc;
  box-shadow: 2px 2px 15px #ccc;

  /*Borders - (Optional)*/
  border-left-style: solid;
  border-left-width: 15px;
  border-right-style: solid;
  border-right-width: 2px;  
  border-radius: 10px;  
}

blockquote::before{
  content: "\201C"; /*Unicode for Left Double Quote*/
  
  /*Font*/
  font-family: Georgia, serif;
  font-size: 60px;
  font-weight: bold;
  color: #fff;
  
  /*Positioning*/
  position: absolute;
  left: 10px;
  top:5px;
  
}

blockquote::after{
  /*Reset to make sure*/
  content: "";
}
blockquote a{
  text-decoration: none;
  background: #eee;
  cursor: pointer;
  padding: 0 3px;
  color: #c76c0c;
}
blockquote a:hover{
 color: #666;
}

blockquote em{
  font-style: italic;
}
blockquote.bluejeans{
  border-left-color: #5e9de6;
  border-right-color: #4b8ad6;
}
span.Cbluejeans{
  color:#4b8ad6;
}

.heading{
   font-family:Montez;
   text-align:center;
   font-size:30px;
}



blockquote h2{
  text-align:left;
  
  font-family: 'Francois One', sans-serif;
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

.information-img{
  margin-left: 15px;
}

.popover-img {
  position: relative;
  overflow: visible;
  z-index: 10;
}


.popover-img::after {
  content: "example"; /* 띄울 텍스트 */
  position: absolute;
  background-color: rgba(0, 0, 0, 0.6); /* 배경색 */
  color: #fff; /* 글자색 */
  padding: 5px;
  border-radius: 5px; /* 테두리 모서리 둥글게 */
  bottom: 100%; /* 이미지 위에 위치 */
  left: 50%; /* 가운데 위치 */
  transform: translate(-50%, 10px); /* 위치 조정 */
  white-space: nowrap; /* 텍스트 줄바꿈 방지 */
  opacity: 0; /* 처음에는 투명하게 */
  transition: opacity 0.3s ease; /* 애니메이션 효과 */
}

.popover-img:hover::after {
  opacity: 1; /* 마우스를 올리면 보이게 */
}
</style>