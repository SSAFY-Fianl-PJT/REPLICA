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
  min-height: 680px;
  margin-left: 5%;
  margin-right: 5%;
}

.article-list {
  display: flex;
  justify-content: flex-start;
  align-content: flex-start;
  flex-flow: wrap;
  text-align: start;

}
</style>
