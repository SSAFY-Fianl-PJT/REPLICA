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
  position: absolute;
  width: 100%;
  background-color: rgb(0, 0, 0, 0.95);
  background: linear-gradient( 
  to bottom, 
  rgba(0,0,0,1) 0%, 
  rgba(0,0,0,0.95) 15%, 
  rgba(0,0,0,0.85) 50%, 
  rgba(0,0,0,0) 100%);

}
</style>