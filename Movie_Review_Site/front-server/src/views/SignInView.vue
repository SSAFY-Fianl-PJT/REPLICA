<template>
  <div>
    <h1>Sign In Page</h1>
    <form @submit.prevent="login">
      <label for="username_signin">username : </label>
      <input type="text" id="username_signin" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload).then(()=>{

        if (this.isLogin) {
          window.location.reload();
        }else{
          alert('아이디 혹은 비밀번호를 다시 입력하세요');
        }
        
        // this.$router.push({ name: 'MainView' });
      })

    }
  }
}
</script>
