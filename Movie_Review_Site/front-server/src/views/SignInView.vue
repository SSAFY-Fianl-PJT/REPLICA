<template>
  <div class="sign-in-view-container">
    <form @submit.prevent="login" class="form">
      <input type="submit" value="Sign in" class="btn">
      
      <input type="text" id="username_signin" placeholder="Username" v-model="username" class="input" required><br>

      
      <input type="password" id="password" placeholder="Password" v-model="password" class="input" required><br>

      
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
  margin: 0.5rem 0;
  width: 100%;
}

.sign-in-view-container{
  display: flex;
  margin: 10px;
  flex-direction: column;
  justify-content: center;
}
</style>