<template>
  <div class="Review-Tag-Info">
    
    <h5>{{ article?.id }}</h5>
    <p>{{ article?.title }}</p>
    <router-link :to="{
      name: 'DetailView',
      params: {id: article?.id }}">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style scoped>
.Review-Tag-Info{
  margin: 30px;
}
</style>
