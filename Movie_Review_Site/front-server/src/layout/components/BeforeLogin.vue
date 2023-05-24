<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <router-link :to="{ name: 'MainView' }">
        <img class="logo" :src="LogoImg" alt="Logo">
      </router-link>

    </div>
  </nav>
</template>

<script>
import LogoImg from '@/assets/Logo_.png'
export default {
  name:"Nav_B",
  data(){
    return {
      LogoImg : LogoImg
    }
  }
}
</script>

<style scoped>
.logo{
  /* background-color: #e3f2fd;   */
  width: 100px;
}
.nav-item{
  padding-top: 5px;
}
</style>