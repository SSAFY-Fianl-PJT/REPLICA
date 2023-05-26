<template>
  <div>

  
  <div class="give-movie">

      <div class="scene ">
        <div class="carousel">
          <div class="item ModalGroup" v-for="(item, index) in items" :key="item.poster_path" :style="{ '--i': index }">
            <figure>
              <ModalButton :target="squeeze(item.title)" :movie="item"  @open-modal="handleOpenModal"/>
            </figure>
          </div>
        </div>
      </div>


      <ModalDialog v-if="showModal" :target="squeeze(currentSelectedItem.title)" :item="currentSelectedItem" @close="handleCloseModal">
          <MovieItem :item="currentSelectedItem"/>
      </ModalDialog>


  </div>
  <div>

    <!-- <div class="scene">
      <div class="carousel">
        <div class="item" v-for="(item, index) in example" :key="index" :style="{ '--i': index }">
          {{ item }}
        </div>
      </div>
    </div> -->

  </div>
  </div>
</template>

<script>
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import MovieItem from '@/components/movie/MovieItem'

export default {
  name: 'MovieContents',
  data() {
    return {
      example: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      sliderIndex: 0,
      showModal: false,
      selectedItem: null,
      carouselItems : null,
      carouselPosition: 0,
    };
  },
  components: {
    MovieItem,
    ModalButton,
    ModalDialog,
  },
  props: {
      items: Array,
  },
  mounted(){
      this.carouselItems = this.items; // items를 받아와서 carouselItems로 설정
      this.cycleCarousel();
    },
  methods: {
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
      let scrollSpeed = (Math.random()*0.3 + 0.5) * 2000; // 스크롤 속도 (ms)

      setInterval(() => {
        if (this.carouselPosition <= -itemWidth * (this.carouselItems.length)) {
          // 만약 모든 항목을 넘어서면 처음 항목으로 바로 이동하지 않고, 순환 리스트의 다음 항목으로 이동합니다.
          
          this.carouselPosition = 0; // 위치를 이동하지 않고 항목들만 순환시킵니다.
        } else {
          
          this.carouselPosition -= itemWidth;
        }
      }, scrollSpeed);
    },
  },
  computed: {
    getItems(){
      return this.items
    },
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
}



.carousel{
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

.carousel > .ModalGroup > figure{
display: flex;
justify-content: center;
align-items: center;
height: 100%;
object-fit: contain;
transition: transform 0.3s ease-in-out;
}

.carousel > .ModalGroup:hover > figure{
transform: scale(1.1);
}



*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}


.scene{
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    perspective: 1200px;
}

.carousel{
    width: 100%;
    height: 150px;
    position: relative;
    transform-style: preserve-3d;
    animation: spin 10s infinite linear;
}
.item {
  background-color: #5fb2e2;
  border: 1px solid #fff;
  transform: rotateY(calc(360deg / 9 * var(--i))) translateZ(288px);
  position: absolute;
  top: 0;
  left: 0;
  width: 200px;
  height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 32px;
  font-weight: 600;
}

@keyframes spin{
    from{
        transform: rotateY(0deg);
    }
    to{
        transform: rotateY(360deg);
    }
}
</style>
