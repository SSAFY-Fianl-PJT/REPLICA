<template>
  <div>
    <div class="radio-checked">
        <input class="radio-checked_input" type="radio" id="on" name="radio" value="on" v-model="checked" />
        <label class="radio-checked_label radio-checked_label--on" for="on">ON</label>

        <input class="radio-checked_input" type="radio" id="off" name="radio" value="off" v-model="checked" />
        <label class="radio-checked_label radio-checked_label--off" for="off">OFF</label>

        <div class="radio-checked_highlight"></div>
    </div>

    <div class="searchresult-container">
        
      <span v-if="getResult" >당신을 위한 추천 목록</span>
        <div class="search-result-found" v-if="Array.isArray(getResult)">
          <div class="SearchedMovieGroup" v-for="(item) in getResult" :key=item.poster_path>
            <div class="ResultMovieTag">
              <ModalButton 
              :target="squeeze(item.title)"
              :movie="item"
              @open-modal="handleOpenModal"/>
            </div>
      
            <ModalDialog :target="squeeze(item.title)">
              <MovieItem :item="item" />
            </ModalDialog>
          </div>
        </div>
        <div class="search-result-not-found" v-else>
          <p> 검색결과가 없습니다.</p>
        </div>
      </div>
  </div>

</template>

<script>
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import MovieItem from '@/components/movie/MovieItem.vue'

export default {
  name:'SearchPage',
  data(){
    return{
      search_target : null,
      checked: 'on'
    }
  },
  components:{
    ModalButton,
    ModalDialog,
    MovieItem
  },
  props:{
    items : Array
  },
  created(){
    this.search_target = this.$store.state.movie.search_target
  },
  mounted() {
        this.checked = 'on';
  },
  watch: {
        checked(val) {
            const highlightLeft = val === 'on' ? 0 : '100%';
            document.documentElement.style.setProperty('--highlight-left', highlightLeft);
        }
  },
  methods:{
    squeeze(data){
      let squeezed_data = data;

      if (/\s/.test(data)) { // check if data contains any space
          squeezed_data = data.replace(/\s/g, "");
      }
      return squeezed_data
    },
    handleOpenModal() {
        this.$store.dispatch('openModal')
        this.showModal = true;
      },
  },
  computed:{
    getResult(){
      return this.items
    },
    tgt(){
      return this.$store.state.movie.search_target
    },
    highlightStyle() {
      return {
        '--pagination-width': this.checked === 'on' ? '0' : '100%',
        '--highlight-left': this.checked === 'on' ? '100%' : '0%',
      };
    },
  }
}
</script>

<style scoped>
.search-result-found{
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;

}

.SearchedMovieGroup{
  /* width: 20%; */
  margin: 20px;
  object-fit: cover;
} 
.searchresult-container{
  width: 100%;
  
}


.ModalGroup{
  flex: 0 0 25%;
  margin: 1rem;
  height: 100%;
  width: 75%;
  max-height: 400px;
  object-fit: cover;
}

.search-result-found > .SearchedMovieGroup > .ResultMovieTag{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  object-fit: contain;
  transition: transform 0.3s ease-in-out;
}

.search-result-found > .SearchedMovieGroup:hover > .ResultMovieTag{
  transform: scale(1.1);
}


/* .SearchPageInterface{
  flex-direction: row;
  justify-content: flex-start; 
  flex-wrap: wrap;
}

.search-result-found
.searchresult-result{
  width: 100%;
}


.searchresult-information{
  margin-top: 25px;
  margin-left: 15px;
  font-weight: bold;
  font-size: 1.2rem;
}




.SearchedMovieGroup{

  margin: 1.5rem;

  object-fit: cover;
} */


@import url("https://fonts.googleapis.com/css2?family=Comfortaa:wght@600&display=swap");

:root {
  --highlight-left: 0;
  --pagination-width: 0;
}

body {
  font-family: sans-serif;
  height: 100%;
  margin: 0;
  font-family: "Comfortaa", cursive;
  background-color: #eef3f7;
  user-select: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.radio-checked {
  width: 250px;
  position: relative;
  font-size: 34px;
  letter-spacing: 1px;
  box-shadow: -5px -5px 10px 4px rgba(152, 174, 213, 0.5);
  border-radius: 70px;
}

.radio-checked_input {
  display: none;
}

.radio-checked_input:checked + .radio-checked_label {
  color: #47cf73;
  text-shadow: 0 0 7px rgba(71, 207, 115, 0.6);
}

.radio-checked_input:checked + .radio-checked_label--off {
  color: #ff3c41;
  text-shadow: 0 0 7px rgba(255, 60, 65, 0.6);
}

.radio-checked_input:checked + .radio-checked_label:before {
  display: none;
}

.radio-checked_label {
  cursor: pointer;
  display: inline-block;
  padding: 20px 25px 15px;
  line-height: 1;
  border-radius: 3rem;
  color: #acb2c0;
  transition: all 250ms ease-in-out;
}

.radio-checked_label:before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  display: block;
}

.radio-checked_container {
  position: relative;
}

.radio-checked_highlight {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 130px;
  height: 100%;
  border-radius: 70px;
  box-shadow: -5px -5px 10px 4px rgba(152, 174, 213, 0.5);
  background: #eef3f7;
  transition: all 0.6s ease;
  transform: translateX(var(--highlight-left));
}

.svg {
  position: absolute;
  top: -50%;
  bottom: -50%;
  pointer-events: none;
}

.svg_icon {
  width: auto;
  height: 100%;
}

.svg--right {
  left: 100%;
}

.svg--left {
  right: 100%;
}


</style>