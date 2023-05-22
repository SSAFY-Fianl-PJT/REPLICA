<template>
  <div>
  
  <div v-if="isLogin && get_username">
    <ProfileItem 
    :user="get_username"
    />
  </div>
  <div v-else>
    역기서 나가
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