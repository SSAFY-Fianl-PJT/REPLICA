<!-- views/CreateView.vue -->

<template>
  <div>
    <br>
    <hr>
    <h3>리뷰 작성</h3>
    <form @submit.prevent="createArticle" class="form-container">
      <div class="input-groups-of-review">
        <div class="input-group">
          <label for="title">제목 : </label>
          <input class="width-input" type="text" id="title" v-model.trim="title">
        </div>
        <div class="input-group">
          <label for="content">내용 : </label>
          <input class="width-input" type="text" id="content"  v-model="content">
        </div>
      </div>
      <div class="submit-group">
        <button type="submit" class="btn btn-info submit-button" id="submit">작성</button>
      </div>
    </form>
    <br>
  </div>
</template>

<script>
import {fetchCreate} from '@/api/article'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  props:{
    movie_title: String
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const movie_title = this.mv_title

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }

      fetchCreate({ title, content, movie_title})
      .then(() => {
        // console.log(res)
        // this.$router.push({name: 'ArticleView'})
        this.refreshPage()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    refreshPage() {
      this.$router.go(); // 현재 라우트를 다시 로드
    }
  },
  computed:{
    mv_title(){
      return this.movie_title.trim()
    }
  }
}
</script>

<style scoped>
.form-container{
  display: flex;
  align-items: center;
  justify-content: center;
}

.input-groups-of-review {
  display: flex;
  flex-direction: column;
  width: 50%;
  
}

.input-group{
  justify-content: flex-end;
}

.width-input {
  width: 80%;
}

.input-group {
  flex: 1;
}


.submit-group {
  display: flex;
  align-items: flex-start;
}

</style>