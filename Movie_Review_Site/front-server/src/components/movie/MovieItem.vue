<template>
    <div class="movie-poster-container">
      <hr>
      <div class="image-container"  ref="imageContainer">
        <div class="poster-img">
          <img :src="getPoster" alt="영화포스터">
        </div>

        <div class="information-block">
          
          <div class="movie-title-reldate">
            <div class="movie-title">
              {{ item.title }}  
              <button v-if="isZZIMM" class="ZZIM" @click="wantThisMovie()">영화 찜 취소</button>
              <button v-else class="ZZIM" @click="wantThisMovie()">영화 찜하기</button>
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
      <hr>
      <create-view :movie_title="item.title" :movie_id="item.id"/>
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
      this.my_wish_list = res.data;
      this.check_is_liked();
    },
    async check_is_liked() {
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
      return this.my_wish_list.some((movie) => movie.movie_id === this.item.id);
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
</style>