<template>
  <div class="comments-list-container">
    <div class="comment-data-holder" v-if="get_commentlist && get_commentlist.length > 0">
      <div class="comment-wrapper" v-for="item in get_commentlist" :key="item.created_at">
        <div class="review-content-block">
          <div v-if="isEditingComment === item.id" @keyup.enter="updateComment(item)">
            <textarea v-model="editContent[item.id]"></textarea>
          </div>
          <div v-else>
            <p>{{ item?.content }}  -  {{ item?.username }} </p>
            <!-- <p>{{ item?.username }}</p> -->
            <p>작성시간: {{ formatDate(item?.updated_at) }} <span v-if="item?.created_at !== item?.updated_at">(수정됨)</span></p>
          </div>
        </div>
        <div class="review-ud-btns">
          <button v-if="isEditingComment !== item.id && isCommentAuthor(item)" @click="startEditing(item.id)">
            수정
          </button>
          <button v-else-if="isEditingComment === item.id && isCommentAuthor(item)" @click="updateComment(item)">
            수정완료
          </button>
          <button v-if="isCommentAuthor(item)" @click="deleteComment(item)">
            삭제
          </button>
        </div>
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
    this.getCommentList();
  },
  watch: {
    refresh() {
      this.getCommentList();
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
.comments-list-container {
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
}
</style>
