<template>
  <nav class="navbar navbar-expand-lg" >
    <div class="container-fluid">
      <router-link :to="{ name: 'MainView' }">
        <img class="logo" :src="LogoImg" alt="Logo">
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav d-flex justify-content-around w-100">
          <li class="nav-item drop-down">
            <router-link :to="{ name: 'MainView' }">홈</router-link>
          </li>
          <li class="nav-item drop-down">
            <router-link :to="{ name: 'ArticleView' }">영화</router-link>
          </li>
          <li class="nav-item drop-down">
            <router-link :to="{ name: 'MovieViewTest' }">영화모달 테스트페이지</router-link>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              YOU
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">프로필</a></li>
              <li><a class="dropdown-item disabled" href="#">설정</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" @click="logOut">로그아웃</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <div class="container-fluid">
              <form class="d-flex" role="search" @submit.prevent="searchMovies">
                <input class="form-control me-2" type="search" v-model="searchQuery" placeholder="Search Movie" aria-label="Search">
                <button class="btn btn-outline-primary" type="submit">Search</button>
              </form>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import LogoImg from '@/assets/Logo_.png'
export default {
  name:"Nav_A",
  data(){
    return {
      LogoImg : LogoImg,
      searchQuery: ''
    }
  },
  methods:{
    logOut(){
      this.$store.dispatch('logout').then(()=>{
        this.$router.push({ name: 'MainView' });
      })
    },
    searchMovies() {
      // 검색 기능 구현을 위한 로직을 작성합니다.
      // 검색어는 this.searchQuery를 사용하여 접근할 수 있습니다.
      this.$store.dispatch('searchMovies', this.searchQuery).then(()=>{
        
      })
      this.searchQuery = ''

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
.drop-down{
  padding-top: 15px;
}
</style>