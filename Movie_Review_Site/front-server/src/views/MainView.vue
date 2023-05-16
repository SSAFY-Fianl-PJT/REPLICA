<template>
  <div>
    <MainAfterLogin v-if="is_login"/>
    <MainBeforeLogin v-else/>
  </div>
</template>

<script>
import MainAfterLogin from '@/components/mainpage/MainAfterLogin'
import MainBeforeLogin from '@/components/mainpage/MainBeforeLogin'

export default {
  name : 'MainView',
  components:{
    MainAfterLogin,
    MainBeforeLogin
  },
  computed:{
    is_login(){
      return this.$store.getters.isLogin
    }
  }
}
</script>

<style>

</style>