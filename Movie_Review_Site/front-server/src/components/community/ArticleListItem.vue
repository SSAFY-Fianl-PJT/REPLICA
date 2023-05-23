<template>
  <div class="Review-Tag-Info">
    <div class="card" style="width: 18rem;">
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
        <h6 class="card-subtitle mb-2 text-muted">{{ article?.movie_title }}</h6>
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
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  methods:{
  }
}
</script>

<style scoped>
.Review-Tag-Info{
  margin: 30px;
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
</style>
