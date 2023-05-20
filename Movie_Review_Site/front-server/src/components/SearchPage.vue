<template>
  <div class="SearchPageInterface">

    <div class="searchresult-result">
      <div class="searchresult-information">
        <span class="searchresult-center">{{ tgt }} 에 대한 검색결과입니다.</span>
      </div>
  
      <div class="searchresult-container">
        
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

  </div>
</template>

<script>
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import MovieItem from './movie/MovieItem.vue'

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
      console.log(this.$store.state.movie.search_results)
      return this.$store.state.movie.search_results.data
    },
    tgt(){
      return this.$store.state.movie.search_target
    }
  }
}
</script>

<style>
/* .SearchPageInterface{
  display: flex;
  flex-direction: column;
} */



.searchresult-information{
  margin-top: 25px;
  margin-left: 15px;
  font-weight: bold;
  font-size: 1.2rem;
}

.searchresult-center{
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 100%;
}

.searchresult-container{
  
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
}

.SearchedMovieGroup{

  margin: 1.5rem;

  object-fit: cover;
}
</style>