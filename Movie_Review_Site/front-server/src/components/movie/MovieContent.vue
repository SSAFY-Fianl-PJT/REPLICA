<template>
  <div class="give-movie">
      <div class="handle left-handle" @click="handleClick('left')">
          <p>&#8249;</p>
      </div>
      <div class="slider" :style="{ transform: sliderTransform }">
          <div class="accountactions">
              <div class="ModalGroup" v-for="(item) in items" :key="item.poster_path">
                  <figure>
                      <ModalButton :target="squeeze(item.title)" :movie="item"  @open-modal="handleOpenModal"/>
                  </figure>
              </div>

          </div>
      </div>
      <div class="handle right-handle" @click="handleClick('right')">
        <p>&#8250;</p>
      </div>

      <ModalDialog v-if="showModal" :target="squeeze(currentSelectedItem.title)" :item="currentSelectedItem" @close="handleCloseModal">
          <MovieItem :item="currentSelectedItem"/>
      </ModalDialog>

  </div>
</template>
  
<script>
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import MovieItem from '@/components/movie/MovieItem'

  export default {
    name: 'MovieContents',
    components: {
      MovieItem,
      ModalButton,
      ModalDialog,
    },
    props: {
      items: Array,
    },
    data() {
      return {
        sliderIndex: 0,
        showModal: false,
        selectedItem: null,
        carouselItems : null,
        carouselPosition: 0,
      };
    },
    created(){

    },  
    mounted(){
      this.carouselItems = this.items; // items를 받아와서 carouselItems로 설정
      this.cycleCarousel();
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
      handleOpenModal(movie) {
        this.selectedItem = movie;
        this.$store.dispatch('openModal')
        this.showModal = true;
      },
      handleCloseModal(){
        this.$store.dispatch('closeModal')
        this.showModal = false;
      },
      squeeze(data){
        let squeezed_data = data.replace(/\s/g, "")
        return squeezed_data
      },
      cycleCarousel() {
        let itemWidth = 300; // 한 항목의 너비. 실제 항목의 너비에 맞게 조정해야 합니다.
        let scrollSpeed = (Math.random()*0.3 + 0.5) * 1000; // 스크롤 속도 (ms)

        setInterval(() => {
          if (this.carouselPosition <= -itemWidth * (this.carouselItems.length)) {
            // 만약 모든 항목을 넘어서면 처음 항목으로 바로 이동하지 않고, 순환 리스트의 다음 항목으로 이동합니다.
            
            this.carouselPosition = 0; // 위치를 이동하지 않고 항목들만 순환시킵니다.
          } else {
            // 그렇지 않으면 carouselPosition을 갱신하여 다음 항목으로 이동합니다.
            
            this.carouselPosition -= itemWidth;
          }
        }, scrollSpeed);
      },
    },
    computed: {
      getItems(){
        return this.items
      },
      // sliderTransform() {
      //   return `translateX(-${this.sliderIndex * 50}%)`;
      // },
      currentSelectedItem() {
        return this.selectedItem;
      },
      sliderTransform() {
        return `translateX(${this.carouselPosition}px)`;
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
 

  .accountactions{
  display: flex;
  justify-content: space-between;
  /* aspect-ratio: 16/9; */
  align-items:center;
  max-height: 400px;
}

.ModalGroup{
  flex: 0 0 25%;
  margin: 1rem;
  height: 100%;
  width: 75%;
  max-height: 400px;
  object-fit: cover;
}

.accountactions > .ModalGroup > figure{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  object-fit: contain;
  transition: transform 0.3s ease-in-out;
}

.accountactions > .ModalGroup:hover > figure{
  transform: scale(1.1);
}

  </style>