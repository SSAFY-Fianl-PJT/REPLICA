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
  max-height: 1000px; /* 원하는 이미지 컨테이너의 최대 높이 설정 */
  overflow: hidden; /* 넘치는 이미지 부분을 숨기기 위해 overflow 속성 사용 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.poster {
  max-width: 100%; /* 이미지의 최대 너비를 100%로 설정하여 컨테이너에 맞추기 */
  max-height: 100%; /* 이미지의 최대 높이를 100%로 설정하여 컨테이너에 맞추기 */
  object-fit: contain; /* 이미지를 컨테이너에 맞게 확대 또는 축소하여 표시 */
}
</style>