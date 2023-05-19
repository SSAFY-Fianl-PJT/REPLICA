<template>


    <div class="accountactions">
      <div class="ModalGroup" v-for="(item) in get_Components" :key=item.poster_path>
        <figure>
          <ModalButton 
          :target="squeeze(item.title)"
          :movie="item"/>
        </figure>
  
        <ModalDialog :target="squeeze(item.title)">
          <slot :item="item"></slot>
        </ModalDialog>
  
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
  methods:{
    squeeze(data){
      let squeezed_data = data.replace(/\s/g, "")
      return squeezed_data
    }
  },
  computed:{
    get_Components(){
      // console.log("겟 콤프",this.Comps)
      return this.Comps
    }
  }
}
</script>

<style scoped>


.accountactions{
  display: flex;
  justify-content: space-around;
  align-items:center;
  

}

.ModalGroup{
  flex: 0 0 25%;
  margin: 1.5rem;

  object-fit: cover;
}

.accountactions > .ModalGroup > figure{
  
  transition: transform 0.3s ease-in-out;

}

.accountactions > .ModalGroup:hover > figure{
  transform: scale(1.1);
}
</style>