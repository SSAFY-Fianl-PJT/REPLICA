<template>
  <div id="app">
    <header-layout/>
    <router-view/>
    <footer-layout/>
  </div>
</template>


<script>
import HeaderLayout from '@/layout/HeaderLayout.vue'
import FooterLayout from '@/layout/FooterLayout.vue';
export default{
  components:{
    HeaderLayout,
    FooterLayout
  }
}
</script>


<style>
#app {
  background-color: rgb(0, 0, 0, 0.95);
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #c0d3e6;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #5c9af1;
}

nav a.router-link-exact-active {
  color: #e0eefc;
}
</style>
