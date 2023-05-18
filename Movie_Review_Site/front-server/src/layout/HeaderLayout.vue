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
  background: linear-gradient( 
  to bottom, 
  rgba(255,255,255,0), 
  rgba(255,255,255,0.4), 
  rgba(255,255,255,1), 
  blue );

}
</style>