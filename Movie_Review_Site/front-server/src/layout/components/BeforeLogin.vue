<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <router-link :to="{ name: 'MainView' }">
        <img class="logo" :src="LogoImg" alt="Logo">
      </router-link>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav d-flex justify-content-around w-100">
          <li class="nav-item">
            <router-link :to="{ name: 'MainView' }">Home </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'ArticleView' }">아티클</router-link>
          </li>
        </ul>
      </div>
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
  width: 100px;
}
.nav-item{
  padding-top: 5px;
}
</style>