<template>
  <div>
    <p>무비 메인페이지 입니다.</p>
    <movie-main-video></movie-main-video>
  </div>
</template>

<script>
import MovieMainVideo from '@/components/movie/MovieMainVideo.vue'

export default {
  name:'MovieMainPage',
  components:{
    MovieMainVideo
  }
}
</script>

<style>

</style>