<template>
  <div class="article-list-content">
    <div class="article-list">
      <ArticleListItem 
      v-for="(article) in articles" :key="article.created_at" :article="article"
      />
    </div>
    <div class="movie-list-at-community">
      하위
    </div>

  </div>

</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

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
  
}

.article-list {
  display: flex;
  flex-flow: wrap;
  text-align: start;
}
</style>
