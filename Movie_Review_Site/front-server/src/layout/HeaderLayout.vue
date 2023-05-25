<template>
  <div class="header nav-bar">
      <after-login v-if="is_login"/>
      <before-login v-else/>
  </div>
</template>

<script>
import AfterLogin from '@/layout/components/AfterLogin.vue'
import BeforeLogin from '@/layout/components/BeforeLogin.vue'



export default {
  components:{
    AfterLogin,
    BeforeLogin
  },
  computed:{
    is_login(){
      return this.$store.getters.isLogin
    }
  }
}
</script>

<style >
.header{

  width: 100%;
  background-color: rgb(0, 0, 0, 0.95);
  background: linear-gradient( 
  to bottom, 
  
  rgba(98, 73, 235, 0.5) 0%, 
  rgba(30, 16, 95, 0.45) 15%, 
  rgba(27, 16, 90, 0.35) 50%, 
  rgba(81, 145, 219,0) 100%);

}
</style>