<template>
  <div class="comments-list-container">

      <div class="comment-data-holder" v-if="get_commentlist && get_commentlist.length > 0">

        <div class="comment-wrapper" v-for="item in get_commentlist" :key="item.created_at">
          <blockquote>
            <div v-if="isEditingComment === item.id" @keyup.enter="updateComment(item)" style="text-align: left; margin-left:20px;">
              <textarea v-model="editContent[item.id]" style="width: 95%;"></textarea>
            </div>
            <div v-else>
              <p style="font-size:20px;">{{ item?.content }}</p>
            </div>
            <cite v-if="item?.username">작성자 : {{ item?.username }}</cite>
            <cite>작성시간: {{ formatDate(item?.updated_at) }} <span v-if="item?.created_at !== item?.updated_at">(수정됨)</span></cite>
            <div class="comment-ud-btns">
              <button class="ud-btn purple mini" v-if="isEditingComment !== item.id && isCommentAuthor(item)" @click="startEditing(item.id)">수정</button>
              <button class="ud-btn purple mini" v-else-if="isEditingComment === item.id && isCommentAuthor(item)" @click="updateComment(item)">수정완료</button>
              <button class="ud-btn purple mini" v-if="isCommentAuthor(item)" @click="deleteComment(item)">삭제</button>
            </div>
          </blockquote>
        </div>
      </div>
      <div v-else>
        <div class="comment-wrapper">
          <p style="margin-top:0; margin-bottom:0;">덧글이 없습니다! 덧글을 달아주세요~</p>
        </div>
      </div>
  </div>

</template>

<script>
import { getComments, updateComment, deleteComment } from '@/api/article';

export default {
  name: 'CommentList',
  props: {
    review_id: {
      type: Number,
      required: true,
    },
    refresh: Boolean,
    comment: Object,
  },
  data() {
    return {
      commentlist: [],
      isEditingComment: null,
      editContent: {},
    };
  },
  async created() {
    await this.$store.dispatch('get_usr_name');
    await this.getCommentList();
  },
  watch: {
    async refresh() {
      await this.getCommentList();
    },
  },
  methods: {
    async getCommentList() {
      const res = await getComments(this.review_id);
      console.log('댓글', res.data)
      this.commentlist = res.data;
    },
    startEditing(commentId) {
      this.isEditingComment = commentId;
      this.editContent[commentId] = this.commentlist.find(item => item.id === commentId).content;
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`;
    },
    async updateComment(item) {
      const updatedComment = {
        review_id: this.review_id,
        comment_id: item.id,
        editContent: this.editContent[item.id],
      };
      try {
        await updateComment(updatedComment);
        this.isEditingComment = null;
        await this.getCommentList();
      } catch (error) {
        console.error(error);
      }
    },
    async deleteComment(item) {
      const deletedComment = {
        review_id: this.review_id,
        comment_id: item.id,
      };
      try {
        await deleteComment(deletedComment);
        this.$router.go();
      } catch (error) {
        console.error(error);
      }
    },
    isCommentAuthor(item) {
      const loggedInUser = this.$store.state.user.info.username;
      return item.username === loggedInUser;
    },
  },
  computed: {
    get_commentlist() {
      return this.commentlist;
    },
  },
};
</script>

<style scoped>
/* .comments-list-container {
  display: flex;
  justify-content: center;
}

.comment-wrapper {
  border: 2px solid white;
  border-radius: 0.5rem;
  margin: 3px;
  padding: 5px;
  font-weight: bold;
}

.comment-wrapper p {
  margin: 0;
}

.comment-wrapper.editing {
  background-color: #f2f2f2;
  border-radius: 0.5rem;
  margin: 5px;
  padding: 10px;
} */

.comment-data-holder{
  max-height: 1569px;
  overflow-y: scroll;
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
.comment-ud-btns{
  display: flex;
  flex-direction: column;
  position: absolute;
  bottom: 0;
}
.ud-btn{
  margin-top: 4px;
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

.comment-wrapper{
  width:480px;
  margin:50px auto;
}

.comment-wrapper blockquote{
  position:relative;
  border-top:1px solid #7A87B0;
  border-bottom:1px solid #7A87B0;
  padding:10px;
  margin: 0 10px 0;
}
.comment-wrapper blockquote p{
  text-align: left;
  margin-left:35px;
}
.comment-wrapper blockquote:before{
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
.comment-wrapper blockquote:after{
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
.comment-wrapper blockquote cite {
  display: block;
  padding-right:30px;
  font-size: 1.2rem;
  text-align: right;
  color: #808080;
}
</style>
