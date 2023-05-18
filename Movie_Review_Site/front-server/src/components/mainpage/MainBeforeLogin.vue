<template>

<div id="SignPage">

  <div class="accountactions">
    <div class="ModalGroup">

      <figure>
        <ModalButton target="Sign-up"/>
      </figure>

      <ModalDialog target="Sign-up">
        <SignUpView/>
      </ModalDialog>

    </div>

    <div class="ModalGroup">

      <figure>
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
    backgroundImageStyle() {
      console.log(this.MainImg)
      return `background-image: url(${this.MainImg});`
    },
    items(){
      return [{id: 1, name : this.name1}, {id: 2, name : this.name2}]
    }
  }
}
</script>

<style scoped>

#SignPage{
  height: 100px;
  display: flex;
  justify-content: space-around;
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
  border: 3px solid black;
}

.accountactions > .ModalGroup:hover > figure{
  transform: scale(1.5);
}
</style>