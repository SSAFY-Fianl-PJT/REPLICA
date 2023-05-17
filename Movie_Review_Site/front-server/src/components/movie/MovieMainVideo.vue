<template>
  <div class="movie-poster">
    <div class="image-container" >
      <img class="poster" :src=TestPoster alt="">
    </div>
  </div>
</template>

<script>
import TestPoster from '@/assets/TestPoster.png'
// https://image.tmdb.org/t/p/w500/75aHn1NOYXh4M7L5shoeQ6NGykP.jpg
export default {
  name:'MainVideo',
  data(){
    return {
      TestPoster:TestPoster
    }
  },
  methods:{

  },
  computed:{

  }
}
</script>

<style>
.movie-poster{
  width: 100%;
}
.image-container {
  width: 100%; /*원하는 이미지 컨테이너의 너비 설정*/
  height: 700px; /*원하는 이미지 컨테이너의 최대 높이 설정*/
   /* 넘치는 이미지 부분을 숨기기 위해 overflow 속성 사용 */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.poster {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지가 요소를 완전히 덮도록 크기 조절 */
  object-position: 50% 15%; /* 이미지를 요소의 중앙에 위치 */
  
}
</style>