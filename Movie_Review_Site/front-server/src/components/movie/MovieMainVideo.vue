<template>
  <div class="movie-poster">
    <p> 영상을 보여주는 페이지 입니다</p>
    <div class="image-container" >
      <img class="poster" :src=TestPoster alt="">
    </div>
  </div>
</template>

<script>
import TestPoster from '@/assets/TestPoster.png'
export default {
  name:'MainVideo',
  data(){
    return {
      TestPoster:TestPoster
    }
  }
}
</script>

<style>

.image-container {
  width: 100%; /* 원하는 이미지 컨테이너의 너비 설정 */
  height: 1000px; /* 원하는 이미지 컨테이너의 높이 설정 */
  overflow: hidden; /* 넘치는 이미지 부분을 숨기기 위해 overflow 속성 사용 */
}

.poster{
  width: 100%;
  height: auto; 
  object-fit: cover; 
}
</style>