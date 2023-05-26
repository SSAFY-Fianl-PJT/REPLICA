<template>
  <div class="review-information">
    <div v-if="article" class="review-container d-block">
      <div class="close-review-btn" style="font-size:48px;" @click="gotoDetail">
        &#10008;
      </div>
      
    <div class="review-block-container">
      <div class="lavander review-block">
          <div v-if="isEditing" @keyup.enter="updateArticle" style="text-align:left; ">
            <input v-model="editTitle" type="text" ><br>
            <p style="text-align:left;">영화 : {{ article?.movie_title }}</p>
          </div>
          <div v-else>

            <h2><span class="Clavander">{{ article?.title }}</span> -
              <img v-if="article" :src="require('@/assets/STAR' + Math.floor(article.rating) + '.png')" style="margin-left: 5px;" :alt="`${Math.floor(article.rating)}`">
              <span class="like-btn" v-if="!check_isLiked"  @click="give_Like">♡</span>
              <span class="like-btn" v-if="check_isLiked" @click="give_Like" style="color:red;">♥</span><span class="like-btn"> {{article.likes_count}} </span>
            </h2>  
            <p style="text-align:left;">영화 : {{ article?.movie_title }}</p>
          </div>
        <code>
          <div v-if="isEditing" @keyup.enter="updateArticle" style="text-align:left; ">
            <textarea v-model="editContent" type="text" style="width:300px; height:60px"></textarea>
          </div>
          <div v-else>
            <p style="text-align:left; font-size:16px;">{{ article?.content }}</p>
          </div>
        </code>
        <div class="review-ud-btns">
          <button class="ud-btn purple mini" v-if="!isEditing && isReviewAuthor" @click="startEditing">수정</button>
          <button class="ud-btn purple mini" v-else-if="isEditing && isReviewAuthor" @click="updateArticle">수정완료</button>
          <button class="ud-btn purple mini" v-if="isReviewAuthor" @click="deleteArticle">삭제</button>
        </div>
        <div class="writer-form">
          <cite style="font-family:FontAwesome;">작성자 : {{ article.username }}</cite>
          <cite style="font-family:FontAwesome;">작성시간: {{ formatDate(article?.updated_at) }} <span v-if="article?.created_at !== article?.updated_at">(수정됨)</span></cite>
        </div>
      </div>
    </div>
      <hr class="hr-1">
      <div class="review-comments-blocks">
        <CommentingBox :review_id="article.id" @comment-added="handleCommentAdded"/>
        <hr class="hr-1">
        <CommentsList :review_id="article.id" :refresh="refresh"/> 
        
      </div>
    </div>

    <div v-if="movieDetail" class="reive-movie-inform d-none d-lg-block">
      <MovieItem :item="movieDetail" />
    </div>
  </div>
</template>

<script>
import { getDetail, updateArticle, deleteArticle, giveLike } from '@/api/article';
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
  watch: {
    '$route.params.id'(newQuery) {
      this.search_target = newQuery;
      console.log("ㅎ", this.search_target)
      // 변경되면 재탐색하는 함수 실행
      this.reNew()
    }
  },
  async created() {
    let backdrop = document.querySelector('.modal-backdrop');
    if (backdrop) backdrop.parentNode.removeChild(backdrop);
    await this.$store.dispatch('get_usr_name')
    this.$store.dispatch('closeModal');
    await this.getArticleDetail();
    await this.getMovieDetail();
    this.usr_name = this.$store.state.user.info.username
  },
  computed: {
    isReviewAuthor() {
      // console.log("이거 왜 초장에 안나오냐",this.$store.state.user.info.username)
      console.log(this.article.username)
      
      const loggedInUser = this.$store.state.user.info.username; // 로그인한 사용자 정보를 가져와야 함
      return this.article.username === loggedInUser;
    },
    getUSR(){
      return this.$store.state.user.profile.id
    },
    check_isLiked(){
      
      if(this.article.likes){
        console.log(this.article.likes.some((usrs => usrs === this.getUSR)))
        return this.article.likes.some((usrs => usrs === this.getUSR))
      }
      else{
        return false
      }
    }
  },
  methods: {
    async give_Like(){
      if (this.article.likes && this.check_isLiked){
        await giveLike(this.article.id)
        this.article.likes = this.article.likes.filter(user => user !== this.getUSR); 
        this.article.likes_count--;
        return false
      }else{
        await giveLike(this.article.id)
        this.article.likes.push(this.getUSR);
        this.article.likes_count++;
        return true
      }
    },
    gotoDetail(){
      // console.log(this.article)
      this.$router.push({name:'MovieViewTest', params:{id:this.article.movie}})
    },
    reNew(){
      this.$router.go();
    },
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
        await updateArticle(id, { movie_title: this.article.movie_title ,title: editTitle, content: editContent, rating: this.article.rating });
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
@import url('https://fonts.googleapis.com/css?family=Montez');
@import url(https://fonts.googleapis.com/css?family=Francois+One);

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

.review-detail-block{
  margin: 10px;
  text-align: left;
  flex: 1;
  border: 3px solid whitesmoke;
  border-radius: 1rem;
}
.review-container{
  position: relative; 
  width: auto;
}

.close-review-btn{
  position: absolute;
  right: 0;
}

.sample3 > .review-title-block
{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 8px;
  text-align: left;
}
.review-title-block * {
  margin-left: 15px;

  display: flex;
  justify-content: space-between;
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
  justify-content: center;
  width: 100%;
}

.review-datail-container {
  margin: 20px;
  text-align: left;
  flex: 1;
}
.review-comments-blocks{
  
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.reive-movie-inform {
  flex: 2;
}


.review-ud-btns{
  display: flex;
  flex-direction: row;
  position: absolute;
  bottom: 0;
  left: 0;
}
.ud-btn{
  font-family:'FontAwesome' !important;
  margin-left: 4px;
  margin-bottom: 4px;
}

.ud-btn.mini{
  padding: 4px 12px;  
  font-size: 12px;
}

.ud-btn.purple {background-color: rgb(143, 143, 214);}

.ud-btn {
  color: white; 
  padding: 15px 25px;
  display: inline-block;
  border: 1px solid rgba(0,0,0,0.21);
  border-bottom-color: rgba(0,0,0,0.34);
  text-shadow:0 1px 0 rgba(0,0,0,0.15);
  box-shadow: 0 1px 0 rgba(255,255,255,0.34) inset, 
              0 2px 0 -1px rgba(0,0,0,0.13), 
              0 3px 0 -1px rgba(0,0,0,0.08), 
              0 3px 13px -1px rgba(0,0,0,0.21);
}
.ud-btn:active {
  top: 1px;
  border-color: rgba(0,0,0,0.34) rgba(0,0,0,0.21) rgba(0,0,0,0.21);
  box-shadow: 0 1px 0 rgba(255,255,255,0.89),0 1px rgba(0,0,0,0.05) inset;
  position: relative;
}

.sample3{
  width:480px;
  margin:50px auto;
}

.sample3 blockquote{
  position:relative;
  border-top:1px solid #7A87B0;
  border-bottom:1px solid #7A87B0;
  padding:10px;
  margin: 0 10px 0;
}
.sample3 blockquote p{
  text-align: left;
  margin-left:35px;
}
.sample3 blockquote:before{
  position:absolute;
  background-color:rgb(13, 13, 13, 0.95);
  color:#7A87B0;
  font-family:'FontAwesome';
  content: "\201C";
  line-height:1;
  text-align:center;
  top:-30px;
  left:-10px;
  padding:10px;
  font-size:50px;
}
.sample3 blockquote:after{
  position:absolute;
  right:-10px;
  bottom:-40px;
  background-color:rgb(13, 13, 13, 0.95);
  padding:10px;
  color:#7A87B0;
  font-family:'FontAwesome';
  content:"\201C";
  line-height:1;
  text-align:center;
  font-size:50px;
}
.sample3 blockquote cite {
  display: block;
  padding-right:30px;
  font-size: 1.2rem;
  text-align: right;
  color: #808080;
}

.review-block-container{
  width:480px;
  margin:50px auto;
}

.review-block{
  display:block;
  background: #fff;
  /* background: rgb(13, 13, 13, 0.95); */
  padding: 15px 20px 15px 45px;
  margin: 0 20px 20px;
  position: relative;
  
  /*Font*/
  font-family: Georgia, serif;
  font-size: 14px;
  line-height: 1.2;
  color: #666;

  /*Box Shadow - (Optional)*/
  -moz-box-shadow: 2px 2px 15px #ccc;
  -webkit-box-shadow: 2px 2px 15px #ccc;
  box-shadow: 2px 2px 15px #ccc;

  /*Borders - (Optional)*/
  border-left-style: solid;
  border-left-width: 15px;
  border-right-style: solid;
  border-right-width: 3px; 
  border-radius: 10px;   
}

.review-block::before{
  content: "\201C"; /*Unicode for Left Double Quote*/
  
  /*Font*/
  font-family: Georgia, serif;
  font-size: 60px;
  font-weight: bold;
  color: #999;
  
  /*Positioning*/
  position: absolute;
  left: 10px;
  top:5px;
  
}

.review-block::after{
  /*Reset to make sure*/
  content: "";
}

.review-block.lavander{
  border-left-color: rgb(143, 143, 214);
  border-right-color: rgb(143, 143, 214);
}

span{
  font-weight:bolder;
}
span.Clavander{
  color:rgb(143, 143, 214);
}
h2{
  text-align:left;
  font-size:24px;
  font-family: 'Francois One', sans-serif;
}

.writer-form{
  display: flex;
  flex-direction: column;
  text-align: right;
  font-weight:bolder;
}

code{
  color:#270d2e;
  font-size:16px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
.like-btn{
  text-align: end;
  float: right;
}
</style>
