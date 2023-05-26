<template>
  <div :style="backgroundImageStyle">
    <MovieMain/>
  </div>
</template>

<script>
import MovieMain from '@/components/movie/MovieMain.vue'
export default {
  name:'MainPage_A',
  components:{
    MovieMain,
  },
  computed: {
    backgroundImageStyle(){
      return {
        background: `linear-gradient(
          to bottom,
          rgba(255,255,255,0) 10%,
          rgba(0,0,0,0.1) 25%,
          rgba(0,0,0,0.2) 40%,
          rgba(0,0,0,0.4) 50%,
          rgba(0,0,0,0.6) 70%
        ), url(${require('@/assets/Main_.png')})`,
        backgroundSize: `auto`,
        backgroundRepeat: 'repeat',
        top:'0',
        height:'100%',
      }
    },
  }
}
</script>

<style>

</style>