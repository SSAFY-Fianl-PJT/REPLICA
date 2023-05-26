<template>
  <div class="article-view-container">
    <h1 style="font-size:64px;"><center>커뮤니티 페이지</center></h1>
    <!-- <router-link :to="{ name: 'CreateView' }">리뷰 작성해줄 페이지</router-link> -->
    <!-- <router-link :to="{ name: 'CreateView' }">추천 페이지</router-link> -->
    <hr class="article-view-hr">

    <ArticleList :articles="getartic"/>
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  props:{

  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
    getartic(){
      return this.$store.state.article.articles
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'MainView' })
      }
      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동
    }
  },


}
</script>

<style scoped>
.article-view-container {
  padding: 0.25rem;
  
  margin: 0 auto;
  
  color: #ccc;
  text-align: justify;
  font-family: ruluko;
}



hr {
  width: auto;
  margin-top: 30px;
  margin-left: 5%;
  margin-right: 5%;
  border: 10px solid #43a1ff;
  color: black;
  border-radius: 10px;
  box-shadow: 0 0 10px #43a1ff;
  padding: 0;
  animation: glow 1.5s ease-in-out infinite;
  -webkit-animation: glow 1.5s ease-in-out infinite;
}

hr::after {
  content: '';
  position: absolute;
  border: 4px solid rgb(34, 34, 34);
  width: 80%;
  margin-top: -2px;
  margin-left: 4%;
  margin-right: 25%;
  border-radius: 2px;
  box-shadow: 0 0 3px black;
  animation: glowMinr 2s ease-in-out;
  -webkit-animation: glowMinor 2s ease-in-out infinite 
}

@keyframes glow {
  0%{box-shadow: 0 0 2px #43a1ff;}
  50%{box-shadow: 0 0 8px #43a1ff;}
  100%{box-shadow: 0 0 2px #43a1ff;}
}

@-webkit-keyframes glow {
  0%{box-shadow: 0 0 2px #43a1ff;}
  50%{box-shadow: 0 0 8px #43a1ff;}
  100%{box-shadow: 0 0 2px #43a1ff;}
}

@keyframes glowMinor {
  0%{box-shadow: 0 0 2px black;}
  50%{box-shadow: 0 0 8px black;}
  100%{box-shadow: 0 0 2px black;}
}

@-webkit-keyframes glowMinor {
  0%{box-shadow: 0 0 2px black;}
  50%{box-shadow: 0 0 8px black;}
  100%{box-shadow: 0 0 2px black;}
}

h1 {
  margin-top: 50px;
  text-shadow:0 0 15px #43a1ff;
  animation: blin 0.5s linear, glowh1 1.5s ease-in-out infinite;
  -webkit-animation: blin 0.5s linear, glowh1 1.5s ease-in-out infinite;
  color:#43a1ff;
}

@keyframes glowh1 {
  0%{text-shadow: 0 0 8px #43a1ff;}
  50%{text-shadow: 0 0 20px #43a1ff;}
  100%{text-shadow: 0 0 8px #43a1ff;}
}

@-webkit-keyframes glowh1 {
  0%{text-shadow: 0 0 8px #43a1ff;}
  50%{text-shadow: 0 0 20px #43a1ff;}
  100%{text-shadow: 0 0 8px #43a1ff;}
}

@keyframes blin {
  0%{transform:translate(-2px, -10px);}
  2%{transform:translate(0px, 0px);}
  40%{transform:translateY(4px) skew(10deg);}
  52%{transform:translateY(0px) skew(0deg);}
}

@-webkit-keyframes blin {
  0%{transform:translate(-2px, -10px);}
  2%{transform:translate(0px, 0px);}
  40%{transform:translateY(4px) skew(10deg);}
  52%{transform:translateY(0px) skew(0deg);}
  100%{transform:translateY(0px) skey(0deg);}
}
</style>
