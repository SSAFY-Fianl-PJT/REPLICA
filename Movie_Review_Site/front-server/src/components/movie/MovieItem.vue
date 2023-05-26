<template>
    <div class="movie-poster-container container">
      <hr class="hr-1">
      <div class="image-container"  ref="imageContainer">
        <div class="poster-img">
          <img :src="getPoster" alt="영화포스터">
        </div>

        <div class="information-block">
          
          <div class="movie-title-reldate">
            <div class="movie-title">
              {{ item.title }} 

              <div class="liked-btn-container">
                <div class="btn" :class="{ 'active': isZZIMM }" @click="wantThisMovie">
                  <span v-if="isZZIMM">찜 취소</span>
                  <span v-else>찜하기</span>
                  <div class="dot"></div>
                </div>
              </div>
            </div>
            
            <div >
              {{ item.release_date }}
            </div>
          </div>

          <div class="movie-summary">
              <div class="summary"  style="max-height: 200px; overflow: hidden;">
                <span>
                  {{ item.overview }}
                </span>
              </div>
              <div class="release_date">
                

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
                    <div style="max-height: 60px; overflow: hidden;">
                    <span v-for="(actor, idx) in item.actors" :key="idx">
                      {{ actor }}{{ idx !== item.actors.length - 1 ? ' |' : '' }}
                    </span>
                    </div>
                  </td>
                </tr>
                <tr>
                  <th>장르</th>
                  <td>
                    <div style="max-height: 60px; overflow: hidden;">
                      <span v-for="(genre, idx) in item.genres" :key="idx">
                        {{ genre.genre_name }}{{ idx !== item.genres.length - 1 ? ' |' : '' }}
                      </span>
                    </div>
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

    <div class="Movie-Review-Page" >
      {{ item.id }} {{ item.title }}
      <review-view :movie_id="item.id"/>
      <hr class="hr-1">
      <create-view :movie_title="item.title" :movie_id="item.id"/>
    </div>

    <hr class="hr-1">
    <div class="Related-movie-Page">


    </div>
      <div v-if="item.related_movies" id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button v-if="item.related_movies[0]" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button v-if="item.related_movies[1]" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button v-if="item.related_movies[2]" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
          <button v-if="item.related_movies[3]" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
          <button v-if="item.related_movies[4]" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
        </div>
        <div class="carousel-inner related-genre-movie">
          <div v-if="item.related_movies[0]" class="carousel-item active">
            <img :src="'https://image.tmdb.org/t/p/w500' + item.related_movies[0].poster_path" class="d-block img-thumbnail" :alt="item.related_movies[0].title">
          </div>
          <div v-if="item.related_movies[1]" class="carousel-item">
            <img :src="'https://image.tmdb.org/t/p/w500' + item.related_movies[1].poster_path" class="d-block img-thumbnail" :alt="item.related_movies[1].title">
          </div>
          <div v-if="item.related_movies[2]" class="carousel-item">
            <img :src="'https://image.tmdb.org/t/p/w500' + item.related_movies[2].poster_path" class="d-block img-thumbnail" :alt="item.related_movies[2].title">
          </div>
          <div v-if="item.related_movies[3]" class="carousel-item">
            <img :src="'https://image.tmdb.org/t/p/w500' + item.related_movies[3].poster_path" class="d-block img-thumbnail" :alt="item.related_movies[3].title">
          </div>
          <div v-if="item.related_movies[4]" class="carousel-item">
            <img :src="'https://image.tmdb.org/t/p/w500' + item.related_movies[4].poster_path" class="d-block img-thumbnail" :alt="item.related_movies[4].title">
          </div>

        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
  </div>



</template>

<script>
import ReviewView from '@/views/ReviewView.vue'
import CreateView from '@/views/CreateView.vue'
import {WishList, MyWishList} from '@/api/movie'
const MOVIE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name:'MovieItem',
  props:{
    item:Object
  },
  data(){
    return {
      MoviePoster : null,
      isLiked : false,
      my_wish_list : []
    }
  },
  components:{
    ReviewView,
    CreateView
  },
  methods: {
    async wantThisMovie() {
      const movie_id = this.item.id;

      await WishList({ movie_id }).then((res) => {
        console.log(res.data.message);
        if (res.data.message.includes('찜 목록에서 제거했습니다')) {
          this.isLiked = false;
        } else {
          this.isLiked = true;
        }
      });

      const user_name = this.$store.state.user.info.username;
      await this.searchMyWishList({ user_name });
    },
    async searchMyWishList({ user_name }) {
      const res = await MyWishList({ user_name });
      console.log("찜",res.data)
      this.my_wish_list = res.data;
      this.check_is_liked();
    },
    async check_is_liked() {
      console.log( "이것의 결과", this.my_wish_list.some((movie) => movie.movie_id === this.item.id))
      this.isLiked = this.my_wish_list.some((movie) => movie.movie_id === this.item.id);
    }
  },
  async created(){
    const user_name = this.$store.state.user.info.username
    await this.searchMyWishList({user_name})
    await this.check_is_liked()
  },
  computed:{
    getPoster(){
      return MOVIE_URL + this.item.poster_path
    },
    isZZIMM() {
      try{
        return this.my_wish_list.some((movie) => movie.movie_id === this.item.id);
      }catch{
        return false
      }
    },


  }
}
</script>

<style scoped>
.movie-poster-container{
  display: flex;
  flex-direction: column;
  background-color: rgba(0, 0, 0, 0.541);
  
}

.image-container {
  flex:1;

  min-height: 700px;
  height: auto;
   

  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
  overflow: hidden;  
  object-position: 50% 0%; /* 이미지를 요소의 중앙에 위치 */
  
}

.poster-img img{
  
  border-radius: 15px;
}

.information-block {

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex: 1;
}
.movie-title-reldate{
  position: relative;
  margin-left: 10px;

  text-align: left;

}
.movie-title-reldate > .movie-title {
  font-size: 1.5em; /* 원하는 사이즈로 조정하세요 */
  font-weight: bold;
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
  height: 350px;
}
.table-text{
  display: flex;
  align-items: center;
}

.table td, .table th {
  max-height: 60px;
  overflow: hidden;
}
hr {
  background-color: #fff;
  padding: 0;
  margin: 10px;
}

hr.hr-1 {
  border: 0;
  height: 1px;
  background-image: linear-gradient(to right, rgba(255, 255, 255, 1), rgba(0, 0, 0, 0.75), rgba(255, 255, 255, 1));
}



.liked-btn-container {
  position: absolute;
  left: 0;
  top: -65px;
  box-sizing: border-box;
  }
.liked-btn-container:before, .liked-btn-container:after {box-sizing: border-box;}

.liked-btn-container {
  display: flex;
  justify-content: flex-start;
  
  flex-flow: wrap;
  font-size: 20px;
  font-family: 'Titillium Web', sans-serif;
}
h1 {
  color: #fff;
  font-size: 2.5rem;
  margin-top: 6rem; 
}
.liked-btn-container .btn {
  position: relative;
  margin: 0 auto;
  width: 8em;
  color: #78bcff;
  border: .15em solid #78bcff;
  border-radius: 5em;
  text-transform: uppercase;
  text-align: center;
  font-size: 1em;
  line-height: 2em;
  cursor: pointer;  
}
.dot {
  content: '';
  position: absolute;
  top: 0;
  width: calc(6em*.2);
  height: 100%;
  border-radius: 100%;
  transition: all 300ms ease;
  display: none;
}
.liked-btn-container .dot:after {
  content: '';
  position: absolute;
  left: calc(50% - .2em);
  top: -.4em;
  height: .8em;
  width: .8em;
  background: #78bcff;
  border-radius: 1em;
  border: .25em solid #fff;
  box-shadow: 0 0 .7em #fff,
        0 0 2em #78bcff;
}
.liked-btn-container .btn.active .dot,
.liked-btn-container .btn:focus .dot {
  animation: atom 2s infinite linear;
  display: block;
}
@keyframes atom {
  0% {transform: translateX(0) rotate(0);}
  30%{transform: translateX(calc(7em - calc(6.5em*.2))) rotate(0);}
  50% {transform: translateX(calc(7em - calc(6.5em*.2))) rotate(180deg);}
  80% {transform: translateX(0) rotate(180deg);}
  100% {transform: translateX(0) rotate(360deg);}
}



.carousel-inner{
  display: flex;
  justify-content: center;
}

</style>