<template>
    <div class="give-movie" v-if="items" >
        <div class="handle left-handle" @click="handleClick('left')">ㅅㅂ;</div>

            <div class="slider">

                <modal-form :Comps="getItems" targetSlot="Movie-Item">
                    <template v-slot:default="slotProps">
                        <MovieItem :item="slotProps.item"/>
                    </template>
                </modal-form>
            </div>


        <div class="handle right-handle" @click="handleClick('right')">ㅂㅅ;</div>
    </div>
  </template>
  
  <script>
import ModalForm from '@/components/modal/ModalForm'
import MovieItem from '@/components/movie/MovieItem'

  export default {
    name: 'MovieContents',
    components: {
      MovieItem,
      ModalForm,
    },
    props: {
      items: Array,
    },
    data() {
      return {
        sliderIndex: 0,
      };
    },
    methods: {
      handleClick(direction) {
        const maxIndex = Math.ceil(this.items.length / 4) - 1; // Adjust this depending on your items per screen
        if (direction === 'left') {
          this.sliderIndex = Math.max(0, this.sliderIndex - 1);
        } else {
          this.sliderIndex = Math.min(maxIndex, this.sliderIndex + 1);
        }
      },
    },
    computed: {
        getItems(){
            console.log("이건 무비리스트", this.items)
            return this.items
        }
    }
  };
  </script>
  
  <style scoped>
  .give-movie {
    width: 100%;
    display: flex;
    justify-content: space-between;
    
    min-height: 25%;
  }
  
    
  .slider {
    display: flex;
    
    flex: 1;
  }
  
  .handle {
    width: 50px;
    height: auto;
    background-color: #ddd; /* Temporary background color to visualize the handle */
    cursor: pointer;
    z-index: 10;
  }
  
  .left-handle {
    margin-right: 1rem;
  }
  
  .right-handle {
    margin-left: 1rem;
  }
  </style>