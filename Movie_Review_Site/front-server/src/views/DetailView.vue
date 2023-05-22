<template>
  <div class="review-information">

    <div class="review-datail-container">
      <h1>Detail</h1>
      {{article.username}}
      <p>글 번호 : {{ article?.id }}</p>
      <p>영화 : {{ article?.movie_title }}</p>
      <p>작성시간 : {{ formatDate(article?.updated_at) }} <span v-if="article?.created_at !== article?.updated_at">(수정됨)</span> </p>
      <p>제목 : {{ article?.title }}</p>
      <p>내용 : {{ article?.content }}</p>
      <!-- <p>작성시간 : {{ article?.created_at }}</p> -->
    </div>
  
    <div v-if="movie_detail" class="reive-movie-inform">
      <MovieItem :item="movie_detail"/>
    </div>
  </div>

</template>

<script>
import {getDetail} from '@/api/article'
import MovieItem from '@/components/movie/MovieItem.vue'
import {getMovie_Detail} from '@/api/movie'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      mv_dtail:null
    }
  },
  components:{
    MovieItem
  },
  async created() {
    await this.getArticleDetail()
    await this.getMovieDetail()
  },
  methods: {
    async getArticleDetail() {

      await getDetail(this.$route.params.id)
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`;
    },
    async getMovieDetail(){
      await getMovie_Detail(this.article.movie)
      .then((res) =>{
        console.log("이건 왜 안나옴",res)
        this.mv_dtail = res.data
      })
    }
  },
  computed:{
    movie_detail(){
      return this.mv_dtail
    }
  }

}
</script>

<style scoped>
.review-information{
  display: flex;
  
}
.review-datail-container {
  margin: 20px;
  text-align: left;
  flex:1;
}
.reive-movie-inform{
  flex:2;
}
</style>
