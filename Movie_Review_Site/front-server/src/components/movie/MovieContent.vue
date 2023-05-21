<template>
    <div class="give-movie">

        <div class="handle left-handle" @click="handleClick('left')">
        <p>&#8249;</p></div>
        <div class="slider" :style="{ transform: sliderTransform }">

            <modal-form :Comps="getItems" targetSlot="Movie-Item">
                <template v-slot:default="slotProps">
                    <MovieItem :item="slotProps.item"/>
                </template>
            </modal-form>
        </div>
        <div class="handle right-handle" @click="handleClick('right')"><p>&#8250;</p></div>

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
        const maxIndex = Math.ceil(this.items.length / 4) +1; // 아이템 개수 업데이트
        if (direction === 'left') {
          this.sliderIndex = this.sliderIndex <= 0 ? maxIndex : this.sliderIndex - 1;
        } else {
          this.sliderIndex = this.sliderIndex >= maxIndex ? 0 : this.sliderIndex + 1;
        }
      },
    },
    computed: {
        getItems(){
            // console.log("이건 무비리스트", this.items)
            return this.items
        },
      sliderTransform() {
        return `translateX(-${this.sliderIndex * 50}%)`;
      },
    }
  };
  </script>
  
  <style scoped>
  .give-movie {

    max-height: 400px;
    display: flex;
    overflow: hidden;
    justify-content: space-between;
    overflow: hidden;
  }
  
    
  .slider {
    
    display: flex;
    flex: 1;
    box-sizing: border-box;
    align-items: center;
    transform: translateX(0);
    transition: transform 0.5s ease-in-out;
  }
  
  .handle {
    width: 60px;
    font-size: 5rem;
    background-color: #5c81f12b ; /* Temporary background color to visualize the handle */
    border-radius: 0.5rem;
    z-index: 1;
    display : flex;
    justify-content: center;
    align-items: center;
    line-height: 2;
  }
  .handle:hover {
    background-color: #5c81f166 ;
  }
  
  .left-handle {
    border-top-left-radius : 0;
    border-bottom-left-radius : 0;
    margin-right: 1rem;
    margin-top: 2.5rem;
    margin-bottom: 2.5rem;
  }

  
  .right-handle {
    border-top-right-radius : 0;
    border-bottom-right-radius : 0;
    margin-left: 1rem;
    margin-top: 2.5rem;
    margin-bottom: 2.5rem;
  }
 
  </style>