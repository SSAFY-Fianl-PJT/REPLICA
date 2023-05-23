<template>
  <div class="comments-list-container">
    <div class="comment-data-holder" v-if="get_commentlist && get_commentlist.length >0">
        <div class="comment-wrapper" v-for="(item) in get_commentlist" :key="item.created_at"> 
        <div class="review-content-block">
          <div v-if="isEditingComment" @keyup.enter="updateComment(item)">
            Content : <textarea v-model="editContent"></textarea>
          </div>
          <div v-else>
            <p>{{ item?.content }}</p>
            <p>{{ item?.username}}</p>
          </div>
          <!-- <p>작성시간: {{ formatDate(item?.updated_at) }} <span v-if="item?.created_at !== item?.updated_at">(수정됨)</span></p> -->
        </div>
        <div class="review-ud-btns">
          <button v-if="!isEditingComment && isCommentAuthor(item)" @click="startEditing(item)">수정</button>
          <button v-else-if="isEditingComment && isCommentAuthor(item)" @click="updateComment(item)">수정완료</button>
          <button v-if="isCommentAuthor(item)" @click="deleteComment(item)">삭제</button>
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
import {getComments, updateComment, deleteComment } from '@/api/article'
export default {
    name:'CommentList',
    props:{
        review_id: {
            type: Number,
            required: true
        },
        refresh: Boolean,
        comment : Object,
    },
    data(){
        return{
            commentlist : [],
            isEditingComment : false,
            editContent: '',
        }
    },
    async created(){
        await this.$store.dispatch('get_usr_name');
        this.getCommentList();
    },
    watch: {
        refresh() {
            console.log("이거 오나?")
            this.getCommentList();
        },
    },
    methods:{
        async getCommentList(){
            const res = await getComments(this.review_id)
            console.log('댓글', res.data)
            this.commentlist = res.data
            console.log(this.commentlist)
        },
        formatDate(dateString) {
            if (!dateString) return '';
            const date = new Date(dateString);
            return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`;
        },
        startEditing() {
            this.isEditingComment = true;
        },
        async updateComment(item) {
            // const updatedComment = {
            //     review_id : this.review_id,
            //     comment_id: item.id,
            //     editContent: this.editContent
            //     }
            try {
                await updateComment({ review_id: this.review_id, comment_id: item.id, editContent: this.editContent });
                this.isEditingComment = false;
                await this.getCommentList();
                
            } catch (error) {
                console.error(error);
            }
        },
        async deleteComment(item) {
            const deletedComment = {
                review_id : this.review_id,
                comment_id: item.id,
                }
            try {
                console.log(deletedComment.comment_id)
                await deleteComment(deletedComment);
                // Redirect to another route or perform other actions after deletion
                this.$router.push({name: 'DetailView'});
            } catch (error) {
                console.error(error);
            }
        },
        isCommentAuthor(item) {
            const loggedInUser = this.$store.state.user.info.username;
            console.log(this.$store.state.user.info)
            console.log(item) // 로그인한 사용자 정보를 가져와야 함
            return item.username === loggedInUser;
    },
    },
    computed:{
        get_commentlist(){
            return this.commentlist
        },
    }
}
</script>

<style scoped>
.comments-list-container{
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

.comment-wrapper {
  background-color: #f2f2f2;
  border-radius: 0.5rem;
  margin: 5px;
  padding: 10px;
}

.comment-wrapper p {
  margin: 0;
}

</style>