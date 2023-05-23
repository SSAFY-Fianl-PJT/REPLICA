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
            <router-link :to="{ name: 'RecommendMovieView' }">영화 추천</router-link>
          </li>
          <li class="nav-item drop-down">
            <router-link :to="{ name: 'ArticleView' }">커뮤니티 페이지</router-link>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              {{ usr_nickname }}
            </a>
            <ul class="dropdown-menu profile-text">
              <li>
                <router-link class="dropdown-item" :key="$route.fullPath"
                :to="{ name: 'ProfileView', params: { username: usr_name } }">프로필</router-link>
              </li>
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
      searchQuery: '',
      usr_nickname : null,
      usr_name : null
    }
  },
  async created(){
    await this.$store.dispatch('getMovies')
    await this.$store.dispatch('get_usr_name')
    await this.$store.dispatch('get_profile', this.$store.state.user.info.username)
    console.log("이게뭐양 ㅠㅠ",this.$store.state.user.info)
   this.usr_name = this.$store.state.user.info.username
   this.usr_nickname = this.$store.state.user.info.nickname
  },
  methods:{
    logOut(){
      this.$store.dispatch('logout').then(()=>{
        this.$router.push({ name: 'MainView' });
      })
    },
    searchMovies() {
      // 검색 기능 구현을 위한 로직을 작성합니다.
      // push 한 다음에 검색할 수 있도록 작업하는게 더 좋지 않을까
      if (this.searchQuery){
        
        this.$router.push({ name: 'SearchView', query: { q: this.searchQuery }})
        .catch((err) => {
          console.warn(err)
        });

      }else{
        alert('검색해주세요ㅕ')
      }
      this.searchQuery = ''

    },
  },
  computed:{
    get_usr(){
            try {
                
                // console.log("이게 말이되나",this.$store.state.user.profile)
                return this.$store.state.user.profile
            } catch(err) {
            console.log(err)
            return "없습니다."
            }
    },
    get_nickname(){
      return this.get_usr.nickname || '...'
    }
  }
}
</script>

<style scoped>
.profile-text{
  color: black;
}


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