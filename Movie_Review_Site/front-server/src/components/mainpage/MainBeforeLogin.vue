<template>

<div id="SignPage"  :style="backgroundImageStyle">

  <div class="accountactions">
    <div class="ModalGroup">

      <figure class="SignPageBtn">
        <ModalButton target="Sign-up"/>
      </figure>

      <ModalDialog target="Sign-up">
        <SignUpView/>
      </ModalDialog>


    </div>

    <div class="ModalGroup">

      <figure class="SignPageBtn">
        <ModalButton target="Sign-In"/>
      </figure>

      <ModalDialog target="Sign-In">
        <SignInView/>
      </ModalDialog>

    </div>
  </div>

</div>

</template>

<script>
import MainImg_ from '@/assets/Main_.png'
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'

import SignInView from '@/views/SignInView'
import SignUpView from '@/views/SignUpView'

export default {
  name : 'MainPage_B',
  components:{
    ModalButton,
    ModalDialog,
    SignUpView,
    SignInView
  },
  data(){
    return{
      name1 : "Sign-Up",
      name2 : "Sign-In",

      MainImg : MainImg_
    }
  },
  methods:{
    pairing(taget){
      return taget
    },
  },
  computed: {
    backgroundImageStyle(){
      return {
        background: `linear-gradient(
          to bottom,
          rgba(255,255,255,0) 10%,
          rgba(0,0,0,0.1) 25%,
          rgba(0,0,0,0.2) 40%,
          rgba(0,0,0,0.4) 50%,
          rgba(0,0,0,0.6) 70%
        ), url(${require('@/assets/Main_.png')})`,
        backgroundSize: `auto`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
      }
    },
    items(){
      return [{id: 1, name : this.name1}, {id: 2, name : this.name2}]
    }
  }
}
</script>

<style scoped>

#SignPage{
  min-height: 1000px;
  height:auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.ModalGroup{
  width: 200px;
  height: 300px;
}

.SignPageBtn{
  display: flex;
  justify-content: center;
  align-items: center;
  
}

.accountactions{
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 75%;
}
.accountactions > .ModalGroup > figure{
  transition: transform 0.3s ease-in-out;
  width: 100%; height: 100%;
  background-color: rgba(60, 48, 228, 0.671);
  border: 3px solid black;
  border-radius: 50px;
}

.accountactions > .ModalGroup:hover > figure{
  transform: scale(1.5);
}
</style>