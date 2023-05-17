<template>
  <div>
    <ModalForm :Comps="items" :useSlots="true">

      <template v-slot:Sign-Up>
        <SignUpView/>
      </template>
      
      <template v-slot:Sign-In>
        <SignInView/>
      </template>

    </ModalForm>

  </div>
</template>

<script>
import MainImg_ from '@/assets/Main_.png'
import ModalForm from '@/components/modal/ModalForm.vue'

import SignInView from '@/views/SignInView'
import SignUpView from '@/views/SignUpView'

export default {
  name : 'MainPage_B',
  components:{
    ModalForm,
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
</style>