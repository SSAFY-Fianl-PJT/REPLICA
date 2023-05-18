<template>
  <div>
    <div class="movie-poster-container">
      
      <div class="image-container" :style="backgroundImageStyle" ref="imageContainer">
        <div class="movie-box" >
          ㅇㅇ?
        </div>
        <div class="movie-title">
          {{ item.title }}
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
              <div>
               
              </div>
            </div>
            <div class="movie-inform">
            <table class="table table-striped table-bordered border-Light table-dark table-hover table-text" >
              <tbody>
                <tr>
                  <th>출연진</th>
                  <td>
                    <span v-for="(actor, idx) in item.actors" :key="idx">
                      {{ actor }}{{ idx !== item.actors.length - 1 ? ' |' : '' }}
                    </span>
                  </td>
                </tr>
                <tr>
                  <th>장르</th>
                  <td>
                    <span v-for="(genre, idx) in item.genres" :key="idx">
                      {{ genre.genre_name }}{{ idx !== item.genres.length - 1 ? ' |' : '' }}
                    </span>
                  </td>
                </tr>
                <tr>
                  <th>TMDB <br>스코어</th>
                  <td>{{ item.popularity }}</td>
                </tr>
                <tr>
                  <th>TMDB 평점</th>
                  <td>{{ item.score_average }}</td>
                </tr>
              </tbody>
            </table>
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
  methods: {
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
          rgba(255,255,255,0.1) 25%,
          rgba(255,255,255,0.2) 40%,
          rgba(0,0,0,1) 50%
        ), url(${MOVIE_URL + this.item.poster_path})`,
        backgroundSize: `contain`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
      }
    }
  }
}
</script>

<style scoped>
.movie-poster-container{
  width: 100%;
  display: flex;
  flex-direction: column;
}
.image-container {

  width: 100%; /*원하는 이미지 컨테이너의 너비 설정*/
  min-height: 700px;
  height: auto;
   

  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  overflow: hidden;  
  object-position: 50% 0%; /* 이미지를 요소의 중앙에 위치 */
}

.information-block {

  display: flex;
  justify-content: space-between;
  width: 100%;
}

.movie-title {
  margin-left: 10px;
  width: 100%;
  text-align: left;
  font-weight: bold;
  font-size: 1.5em; /* 원하는 사이즈로 조정하세요 */
}

.summary{
  text-align: left;

}

.movie-summary,
.movie-inform {
  margin: 10px;
  flex: 1;
}

.movie-box{
  background-color: rgba(255, 235, 205, 0.541);
  width: 100%;
  height: 350px;
}
.table-text{
  display: flex;
  align-items: center;
}
</style>