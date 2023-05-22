<template>
  <div class="review-information">
    <div class="review-datail-container">
      <h1>Detail</h1>
      {{ article.username }}
      <p>글 번호: {{ article?.id }}</p>
      <p>영화: {{ article?.movie_title }}</p>
      <p>작성시간: {{ formatDate(article?.updated_at) }} <span v-if="article?.created_at !== article?.updated_at">(수정됨)</span></p>
      <div v-if="isEditing" @keyup.enter="updateArticle">
        제목 : <input v-model="editTitle" type="text"><br>
        내용 : <textarea v-model="editContent"></textarea>
      </div>
      <div v-else>
        <p>제목: {{ article?.title }}</p>
        <p>내용: {{ article?.content }}</p>
      </div>
      <button v-if="!isEditing && isReviewAuthor" @click="startEditing">수정</button>
      <button v-else-if="isEditing && isReviewAuthor" @click="updateArticle">수정완료</button>
      <button v-if="isReviewAuthor" @click="deleteArticle">삭제</button>
    </div>

    <div v-if="movieDetail" class="reive-movie-inform">
      <MovieItem :item="movieDetail" />
    </div>
  </div>
</template>

<script>
import { getDetail, updateArticle, deleteArticle } from '@/api/article';
import { getMovieDetail } from '@/api/movie';
import MovieItem from '@/components/movie/MovieItem.vue';

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      movieDetail: null,
      isEditing: false,
      editTitle: '',
      editContent: '',
    };
  },
  components: {
    MovieItem,
  },
  async created() {
    await this.getArticleDetail();
    await this.getMovieDetail();
  },
  computed: {
    isReviewAuthor() {
      const loggedInUser = this.$store.state.user.info.username; // 로그인한 사용자 정보를 가져와야 함
      return this.article.username === loggedInUser;
    },
  },
  methods: {
    async getArticleDetail() {
      const articleId = this.$route.params.id;
      try {
        const response = await getDetail(articleId);
        this.article = response.data;
        this.editTitle = this.article.title;
        this.editContent = this.article.content;
      } catch (error) {
        console.error(error);
      }
    },
    async getMovieDetail() {
      const movieId = this.article.movie;
      try {
        const response = await getMovieDetail(movieId);
        this.movieDetail = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`;
    },
    startEditing() {
      this.isEditing = true;
    },
    async updateArticle() {
      const { id } = this.article;
      const { editTitle, editContent } = this;
      try {
        await updateArticle(id, { movie_title: this.article.movie_title ,title: editTitle, content: editContent });
        this.isEditing = false;
        await this.getArticleDetail();
      } catch (error) {
        console.error(error);
      }
    },
    async deleteArticle() {
      const { id } = this.article;
      try {
        await deleteArticle(id);
        // Redirect to another route or perform other actions after deletion
        this.$router.push({name: 'ArticleView'});
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.review-information {
  display: flex;
}

.review-datail-container {
  margin: 20px;
  text-align: left;
  flex: 1;
}

.reive-movie-inform {
  flex: 2;
}
</style>
