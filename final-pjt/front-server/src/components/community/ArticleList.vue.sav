<template>
  <div class="article-list-content">
    <div class="article-list">
      <ArticleListItem 
      v-for="(article) in articles" :key="article.created_at" :article="article"
      />
    </div>
    <div class="movie-list-at-community">
      
    </div>

  </div>

</template>

<script>
import ArticleListItem from '@/components/community/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  props:{
    articles : Array
  },
  computed: {
  }
}
</script>

<style scoped>
.article-list-content{
  display: flex;
  min-height: 1111px;
}

.article-list {
  display: flex;
  justify-content: space-around;
  flex-flow: wrap;
  text-align: start;
}
</style>
