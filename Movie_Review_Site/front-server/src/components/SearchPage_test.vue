<template>
  <div class="SearchPageInterface">

    <div class="searchresult-container">
      
      <div class="SearchedMovieGroup" v-for="(item) in getResult" :key=item.poster_path>

      </div>

    </div>
  </div>
</template>

<script>


export default {
  name:'SearchPage',
  data(){
    return{
      result : null
    }
  },
  components:{

  },
  created(){
    this.result = this.getResult
  },
  watch: {

  },
  methods:{
    squeeze(data){
      let squeezed_data = data.replace(/\s/g, "")
      return squeezed_data
    }
  },
  computed:{
    getResult(){
      return this.$store.state.movie.search_results.data
    }
  }
}
</script>

<style>


.searchresult-container{
  display: flex;
  flex-direction: row;
  
  flex-wrap: wrap;
}

.SearchedMovieGroup{
  width: 100px;
  height: 100px;
  background-color: white;
/* 
  flex: 0 0 ;
  margin: 1.5rem;
  height: 75%;
  object-fit: cover; */
}
</style>