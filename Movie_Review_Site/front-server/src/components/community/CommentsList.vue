<template>
  <div class="comments-list-container">
    <div class="comment-data-holder" v-if="get_commentlist && get_commentlist.length >0">
        <div class="comment-wrapper" v-for="(item) in get_commentlist" :key="item.created_at"> 
            {{item}}
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
import {getComments} from '@/api/article'
export default {
    name:'CommentList',
    props:{
        review_id: {
            type: Number,
            required: true
        },
        refresh: Boolean,
    },
    data(){
        return{
            commentlist : []
        }
    },
    created(){
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
            this.commentlist = res.data
        }
    },
    computed:{
        get_commentlist(){
            return this.commentlist
        }
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

</style>