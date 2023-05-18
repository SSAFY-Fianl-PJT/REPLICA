<template>
  <div>
    <movie-main-video></movie-main-video>
    <movie-list></movie-list>
  </div>

</template>

<script>
import MovieMainVideo from '@/components/movie/MovieMainVideo.vue'
import MovieList from '@/components/movie/MovieList.vue';

export default {
  name:'MovieMainPage',
  components:{
    MovieMainVideo,
    MovieList
  }
}
</script>

<style>

</style>