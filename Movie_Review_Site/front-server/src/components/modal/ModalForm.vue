<template>

  <div id="main-page" >
    <div class="accountactions">
      <div class="ModalGroup" v-for="(item, idx) in get_Components" :key=idx>
        <figure>
          <ModalButton :target="item.title"/>
        </figure>
  
        <ModalDialog :target="item.title">
          <slot v-if="useSlots" :name="item.name"></slot>
          <slot v-else :name="targetSlot"></slot>
        </ModalDialog>
  
      </div>
    </div>
  </div>

</template>

<script>
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'


export default {
  name : 'ModalForm',
  props:{
    Comps : Array,
    useSlots: {
      type: Boolean,
      default: false
    },
    targetSlot:String,
  },
  components:{
    ModalButton,
    ModalDialog,
  },
  computed:{
    get_Components(){
      console.log("겟 콤프",this.Comps)
      return this.Comps
    }
  }
}
</script>

<style scoped>
#main-page{
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