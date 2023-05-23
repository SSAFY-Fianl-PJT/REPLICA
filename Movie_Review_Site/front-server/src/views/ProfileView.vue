<template>
  <div>
  
  <div v-if="isLogin && get_username">
    <ProfileItem 
    :user="get_username"
    />
  </div>
  <div v-else>
  </div>
</div>
</template>

<script>
import ProfileItem from '@/components/community/ProfileItem'
export default {
    name : 'ProfileView',
    components:{
        ProfileItem
    },
    data(){
      return{
        user_name : null
      }
    },
    created(){
      let backdrop = document.querySelector('.modal-backdrop');
      if (backdrop) backdrop.parentNode.removeChild(backdrop);
      this.$store.dispatch('closeModal');
      
      this.user_name = this.$route.params.username
    },

    computed:{
        isLogin() {
          return this.$store.getters.isLogin // 로그인 여부
        },
        get_username() {
          
          return this.user_name
    }
  }
}
</script>

<style>

</style>