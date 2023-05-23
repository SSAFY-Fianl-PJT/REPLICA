<template>
  <div class="review-information">
    <div v-if="article" class="review-container">
      <div class="review-detail-block">
        <div class="review-title-block">
          <div v-if="isEditing" @keyup.enter="updateArticle">
          제목 : <input v-model="editTitle" type="text"><br>
          </div>
          <div v-else>
            <h1>제목: {{ article?.title }}</h1>
          </div>
          <div>
            <p>{{ article.username }}</p>
          </div>
          <hr>
        </div>
        
        <div class="review-movie-inform-block">
          <p>영화: {{ article?.movie_title }}</p>
          <p>작성시간: {{ formatDate(article?.updated_at) }} <span v-if="article?.created_at !== article?.updated_at">(수정됨)</span></p>
        </div>
        <div class="review-content-block">
          <div v-if="isEditing" @keyup.enter="updateArticle">
            Content : <textarea v-model="editContent"></textarea>
          </div>
          <div v-else>
            <p>내용: {{ article?.content }}</p>
          </div>
        </div>
        <div class="review-ud-btns">
          <button v-if="!isEditing && isReviewAuthor" @click="startEditing">수정</button>
          <button v-else-if="isEditing && isReviewAuthor" @click="updateArticle">수정완료</button>
          <button v-if="isReviewAuthor" @click="deleteArticle">삭제</button>
        </div>
      </div>
      <hr>
      <div class="review-comments-blocks">
        <CommentingBox :review_id="article.id" @comment-added="handleCommentAdded"/>
        <hr>
        <CommentsList :review_id="article.id" :refresh="refresh"/> 
        
      </div>
    </div>

    <div v-if="movieDetail" class="reive-movie-inform">
      <MovieItem :item="movieDetail" />
    </div>
  </div>
</template>

<script>
import { getDetail, updateArticle, deleteArticle } from '@/api/article';
import { getMovie_Detail } from '@/api/movie';
import MovieItem from '@/components/movie/MovieItem.vue';

import CommentingBox from '@/components/community/CommentingBox'
import CommentsList from '@/components/community/CommentsList'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
      movieDetail: null,
      isEditing: false,
      editTitle: '',
      editContent: '',
      refresh: false,
    };
  },
  components: {
    MovieItem,
    CommentingBox,
    CommentsList 
  },
  async created() {
    let backdrop = document.querySelector('.modal-backdrop');
    if (backdrop) backdrop.parentNode.removeChild(backdrop);
    this.$store.dispatch('closeModal');
    await this.getArticleDetail();
    await this.getMovieDetail();
    console.log("아티클 확인",this.article)
  },
  computed: {
    isReviewAuthor() {
      // console.log("이거 왜 초장에 안나오냐",this.$store.state.user.info.username)
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
        const response = await getMovie_Detail(movieId);
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
    handleCommentAdded() {
        this.refresh = !this.refresh;
    },
  },
};
</script>

<style scoped>
.review-detail-block{
  margin: 10px;
  text-align: left;
  flex: 1;
  border: 3px solid whitesmoke;
  border-radius: 1rem;
}

.review-detail-block > .review-title-block
{
  display: flex;
  flex-direction: column;
  margin: 8px;
  text-align: left;
}
.review-title-block * {
  margin: 0;
  align-content: end;
}
.review-detail-block > .review-movie-inform-block
{
  display: flex;
  flex-direction: column;
  margin: 10px;
  text-align: left;
}
.review-detail-block > .review-content-block {
  display: flex;
  flex-direction: column;
  margin-top: 10px; 
  margin-bottom: 10px; 
  text-align: left;
}
.review-movie-inform-block * {
  margin: 0;
  align-content: end;
}

.review-ud-btns{
  margin-left: 0.5rem;
  margin-bottom: 0.5rem;
}

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
