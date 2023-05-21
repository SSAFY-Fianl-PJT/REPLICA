<template>
  <div v-if="isLogin && get_username">
    <ProfileItem 
    :user="get_username"
    />
  </div>
  <div v-else>
    역기서 나가
  </div>

</template>

<script>
import ProfileItem from '@/components/ProfileItem'
export default {
    name : 'ProfileView',
    components:{
        ProfileItem
    },
    deta(){

    },
    created(){
        this.$store.dispatch('get_usr_name');

    },

    computed:{
        isLogin() {
          return this.$store.getters.isLogin // 로그인 여부
        },
        get_username() {
            if (!this.$store.state.user.info) return false
            return this.$store.state.user.info.username 
        },
    }
}
</script>

<style>

</style>