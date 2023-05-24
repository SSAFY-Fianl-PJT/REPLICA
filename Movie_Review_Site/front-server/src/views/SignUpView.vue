<template>
  <div class="sign-up-view-container">
    
    <form @submit.prevent="signUp" class="form">
      <input type="submit" value="SignUp" class="btn">

      <input type="text" id="username_signup" placeholder="Username" v-model="username" class="input" required><br>

      <input type="text" id="nickName" placeholder="Nickname" v-model="nickname" class="input" required><br>

      <input type="password" id="password1" placeholder="Password" v-model="password1" @input="checkPassword" class="input" required><br>

      <input type="password" id="password2" placeholder="Password Confirm" v-model="password2" @input="checkPassword" class="input" required>
      
      <div>
        <p v-if="passwordMessage || passwordMessage.length>0" :class="{'match': isPasswordMatch, 'mismatch': !isPasswordMatch}">
          {{ passwordMessage }}
        </p>
      </div>

      
    </form>
  </div>
</template>


<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      nickname: null,
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
      const nickname = this.nickname
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,
        nickname,
        password1, 
        password2
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
.btn {
  background-color: #0367a6;
  background-image: linear-gradient(90deg, #0367a6 0%, #008997 74%);
  border-radius: 20px;
  border: 1px solid #0367a6;
  color: #e9e9e9;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.form > .btn {
  margin-top: 1.5rem;
  margin-bottom: 1rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}

.form {
  background-color: #e9e9e9;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 3rem;
  height: 100%;
  text-align: center;
}

.input {
  background-color: #fff;
  border: none;
  padding: 0.9rem 0.9rem;
  margin: 1px 0;
  width: 100%;
}

.match {
  color: green;
}

.mismatch {
  color: red;
}
.sign-up-view-container{
  display: flex;
  margin: 10px;
  flex-direction: column;
  justify-content: center;
}
</style>