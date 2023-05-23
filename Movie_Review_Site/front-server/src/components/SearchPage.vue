<template>
  <div class="SearchPageInterface">

    <div class="searchresult-result">
      <div class="searchresult-information">
        <span class="searchresult-center">{{ query_info }} 에 대한 검색결과입니다.</span>
      </div>
  
      <div class="searchresult-container">
        
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

  </div>
</template>

<script>
import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import MovieItem from '@/components/movie/MovieItem.vue'
import {fetchSearchMovies} from '@/api/movie'


export default {
  name:'SearchPage',
  data(){
    return{
      search_target : null,
      searched_lst : []
    }
  },
  components:{
    ModalButton,
    ModalDialog,
    MovieItem
  },
  async created(){
    this.search_target = this.$route.query.q
    // 탐색하는 함수 실행 

    await this.getSearchedList()

  },
  watch: {
    '$route.query.q'(newQuery) {
      this.search_target = newQuery;
      console.log( this.search_target)
      // 변경되면 재탐색하는 함수 실행
      this.getSearchedList()
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
    async getSearchedList(){
      let search_lst = []
      
      const search_rlt_title = await fetchSearchMovies({title : this.search_target})
      const title_lst = search_rlt_title.data
      console.log(title_lst)
      if(Array.isArray(title_lst) && title_lst.length !== 50){
        search_lst = [...search_lst, ...title_lst]
        console.log(search_lst)
      }

      const search_rlt_genere = await fetchSearchMovies({genere : this.search_target})
      const genere_lst = search_rlt_genere.data

      if(Array.isArray(genere_lst) && genere_lst.length !== 50){
        search_lst = [...search_lst, ...genere_lst]
        console.log(search_lst)
      }

      console.log(!isNaN(this.search_target))
      console.log(this.search_target)
      if (!isNaN(this.search_target))
      {
        const search_rlt_year = await fetchSearchMovies({year : this.search_target})
        const year_lst = search_rlt_year.data
        console.log(year_lst)
        if(Array.isArray(year_lst) ){
          search_lst = [...search_lst, ...year_lst]
        }
      }
      this.searched_lst = search_lst
      
    }
  },
  computed:{
    getResult(){
      return this.searched_lst
    },
    tgt(){
      return this.$store.state.movie.search_target
    },
    query_info(){
      return this.search_target
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