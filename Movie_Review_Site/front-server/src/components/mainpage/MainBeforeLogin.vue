<template>
  <div id="main-page" :style="{backgroundImageStyle}">

    <ModalButton target="Sign-Up"/>
    <ModalDialog target="Sign-Up">
      <SignUpView/>
    </ModalDialog>

    <ModalButton target="Sign-In"/>
    <ModalDialog target="Sign-In">
      <SignInView/>
    </ModalDialog>

    <img :src="MainImg" alt="이미지">
  </div>
</template>

<script>
import MainImg from '@/assets/Main_.png'
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import SignInView from '@/views/SignInView'
import SignUpView from '@/views/SignUpView'

export default {
  name : 'MainPage_B',
  components:{
    ModalDialog,
    ModalButton,
    SignInView,
    SignUpView
  },
  data(){
    return{
      name1 : "Sign-In",
      name2 : "Sign-Up",

      MainImg : MainImg
    }
  },
  methods:{
    pairing(taget){
      return taget
    },
  },
  computed: {
    backgroundImageStyle() {
      console.log(this.MainImg)
      return `background-image: url(${this.MainImg});`
    }
  }
}
</script>

<style scoped>

  .main-page {
    width: 100%;
    height: 100vh;
    background-image: url('@/img/Main_img_large.jpg'),
    url('@/img/Main_img_large.jpg');
    background-size: cover;
    background-position: center;
  }
</style>