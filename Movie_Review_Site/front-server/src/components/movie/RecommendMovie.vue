<template>
  <div>
    <div class="searchresult-container">
        
      <span v-if="getResult" >당신을 위한 추천 목록</span>
        <div class="search-result-found" v-if="Array.isArray(getResult)">
          <div class="SearchedMovieGroup" v-for="(item) in getResult" :key=item.poster_path>
            <div class="ResultMovieTag">
              <ModalButton 
              :target="squeeze(item.title)"
              :movie="item"/>
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
      search_target : null
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
  watch: {

  },
  methods:{
    squeeze(data){
      let squeezed_data = data;

      if (/\s/.test(data)) { // check if data contains any space
          squeezed_data = data.replace(/\s/g, "");
      }
      return squeezed_data
    }
  },
  computed:{
    getResult(){
    
      return this.items
    },
    tgt(){
      return this.$store.state.movie.search_target
    }
  }
}
</script>

<style scoped>
.search-result-found{
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
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
</style>