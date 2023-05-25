<template>
  <div>
  <div class="give-movie-3D">
      
      <div class="scene">
        <div class="carousel" ref="carouselRef" :style="{ 'transition': transitionStyle }">
          
          <div class="item ModalGroup" 
          v-for="(item, index) in items" 
          :key="item.poster_path" 
          :style="{ '--i': index, '--target-angle': target_angle, '--translate-z': translateZ }">
          
            <div class="item-parent">

              <figure>
                <ModalButton :target="squeeze(item.title)" :movie="item"  @open-modal="handleOpenModal"/>
              </figure>

            </div>
          </div>
        </div>
      </div>


      <ModalDialog v-if="showModal" :target="squeeze(currentSelectedItem.title)" :item="currentSelectedItem" @close="handleCloseModal">
          <MovieItem :item="currentSelectedItem"/>
      </ModalDialog>
  </div>

    <!-- <div>
      <div class="scene">
        <div class="carousel">
          <div class="item" 
          v-for="(item, idx) in examples" 
          :key="idx" 
          :style="{ '--i': idx, '--target-angle': target_angle_test, '--translate-z': translateZ_test }">
            {{ item }}
          </div>
        </div>
      </div>
    </div> -->
  </div>
</template>


<script>
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import MovieItem from '@/components/movie/MovieItem'

export default {
  name: 'MovieContent',
  data(){
    return{
      examples : [1,2,3,4,5,6,7,8,9, 10],
      itemWidth : 135,
      sliderIndex: 0,
      showModal: false,
      selectedItem: null,
      carouselItems : null,
      carouselPosition: 0,
      isHovered: false,
    }
  },
  components:{
    ModalButton,
    ModalDialog,
    MovieItem,
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
    handleMouseOut() {
      this.isHovered = true;
      this.$refs.carouselRef.style.animationDuration = '40s';
    },
    handleMouseOver() {
      this.isHovered = false;
      this.$refs.carouselRef.style.animationDuration = '60s';
    },
  },
  computed:{
    target_angle() {
      return 360 / this.items.length;
    },
    translateZ() {
      console.log((this.itemWidth / 2) / Math.tan((this.target_angle / 2) * (Math.PI / 180)))
      return (this.itemWidth / 2) / Math.tan((this.target_angle / 2) * (Math.PI / 180));
    },
    transitionStyle() {
      return this.isHovered ? 'animation-timing-function: linear' : '';
    },

    target_angle_test() {
      return 360 / this.examples.length;
    },
    translateZ_test() {
      console.log((this.itemWidth / 2) / Math.tan((this.target_angle_test / 2) * (Math.PI / 180)))
      return (this.itemWidth / 2) / Math.tan((this.target_angle_test / 2) * (Math.PI / 180));
    },

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
}
</script>

<style scoped>


.give-movie {

max-height: 400px;
display: flex;

justify-content: space-between;

}





.ModalGroup{
flex: 0 0 25%;
margin: 1rem;
height: 100%;
width: 75%;
max-height: 300px;
object-fit: cover;
}


/* 3D회전 */

.give-movie-3D {
  width: 100%;
  max-height: 400px;
  display: flex;
  justify-content: center;

}


.scene {
  margin-top: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1200px;
  margin-bottom: 100px;
}

.carousel {
  width: 140px;
  height: 200px;
  position: relative;
  transform-style: preserve-3d;
  animation: spin 50s infinite linear;
  
}

.item > .item-parent > figure{
display: flex;
justify-content: center;
align-items: center;
height: 100%;
object-fit: contain;
transition: transform 0.3s ease-in-out;
}

.item > .item-parent:hover > figure{
transform: scale(1.1);
}


.item {
  position: absolute ;
  
  top: 0;
  left: 0;
  transform: rotateY(calc(1deg * var(--target-angle) * var(--i))) translateZ(calc(1px * var(--translate-z))); /* item의 width // tan(내심의 각의 반) */
  width: 130px;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  
  color: #fff;
  font-size: 32px;
  font-weight: 600;
}

.item-parent{
  position: relative;
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