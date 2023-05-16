<template>
  <div id="header">
    <div>
      <after-login v-if="false"/>
      <before-login v-else/>
    </div>
  </div>
</template>

<script>
import AfterLogin from '@/layout/components/AfterLogin.vue'
import BeforeLogin from '@/layout/components/BeforeLogin.vue'



export default {
  components:{
    AfterLogin,
    BeforeLogin
  }
}
</script>

<style>

</style>