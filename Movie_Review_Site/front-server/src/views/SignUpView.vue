<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username_signup">username : </label>
      <input type="text" id="username_signup" v-model="username" ><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1" @input="checkPassword"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2" @input="checkPassword">
      <div>
        <p :class="{'match': isPasswordMatch, 'mismatch': !isPasswordMatch}">
          {{ passwordMessage }}
        </p>
      </div>
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      isPasswordMatch: false
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
    passwordMessage() {
      if (!this.password1){
        return '비밀번호를 입력해주세요'
      }
      return this.isPasswordMatch ? '비밀번호가 일치합니다.' : '비밀번호가 일치하지 않습니다.'
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload).then(()=>{
        if (this.isLogin) {
          window.location.reload();
        }else{
          alert('아이디 혹은 비밀번호를 다시 입력하세요');
        }
      })
    },
    checkPassword() {
      console.log(this.password1, this.password2)
      console.log(this.password1 && this.password2)
      this.isPasswordMatch = (this.password1 === this.password2) && (this.password1 && this.password2)
    }
  }
}
</script>

<style scoped>
.match {
  color: green;
}

.mismatch {
  color: red;
}
</style>