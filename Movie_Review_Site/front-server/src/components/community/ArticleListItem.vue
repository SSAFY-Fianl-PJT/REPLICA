<template>
  <div class="Review-Tag-Info">
    <div class="card" :style="backgroundImageStyle">
      <div class="card-overlay"></div>
      <div class="card-body">
        <div class="card-movie-title">
          <h5 class="card-title" style="font-weight: bold;">{{ article?.title }} : </h5>
          <router-link :to="{
            name: 'MovieViewTest',
            params: {id: article?.movie }}">
            [영화 상세]
          </router-link>
          <hr>
        </div>
        <h6 class="card-subtitle mb-2 text-muted" style="color: white !important;">{{ article?.movie_title }}</h6>
        <p class="card-text ellipsis">{{ article?.content }}</p>
        <div class="card-link">
          <router-link class="dropdown-item" 
            :to="{ name: 'DetailView',
            params: {id: article?.id }}">
            [리뷰 상세]
          </router-link>
          
          <router-link class="dropdown-item" 
            :to="{ name: 'ProfileView', 
            params: { username: article?.username } }">
            [프로필]</router-link>

        </div>

      </div>
    </div>

  </div>
</template>

<script>
import {getMovie_Detail} from '@/api/movie'
const MOVIE_URL = 'https://image.tmdb.org/t/p/w500'
export default {
  name: 'ArticleListItem',
  data(){
    return{
      movie_poster : null
    }
  },
  props: {
    article: Object,
  },
  async created(){
    const res = await getMovie_Detail(this.article.movie)
    this.movie_poster = res.data.poster_path
  },
  methods:{
  },
  computed:{
    backgroundImageStyle(){
      return {
        background: `linear-gradient(
          to bottom,
          rgba(0,0,0,0.75) 10%,
          rgba(0,0,0,0.3) 25%,
          rgba(0,0,0,0.5) 40%,
          rgba(0,0,0,0.3) 75%,
          rgba(0,0,0,0.75) 90%
        ), url(${MOVIE_URL + this.movie_poster})`,
        backgroundSize: `contain`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        width: '18rem',
      }
    },
  },
}
</script>

<style scoped>
.Review-Tag-Info{
  margin: 30px;
  max-height: 300px;
  
}
.card-movie-title{
  display: flex;
  flex-wrap: wrap;
}

.dropdown-item{
  text-align: center;
}
.card-link{
  display: flex;
  justify-content: space-around;
}

.ellipsis {
  /* 텍스트가 넘칠 경우 생략 부분을 표시할 스타일 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.card{
  color: white;
  box-shadow: 0px 0px 50px  rgba(152, 174, 213, 0.3);
  border-radius: 15px;
}
.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.1);  /* Semi-transparent black overlay */
  z-index: 1;  /* Make sure the overlay is on top of the background image */
  pointer-events: none;
}

</style>
