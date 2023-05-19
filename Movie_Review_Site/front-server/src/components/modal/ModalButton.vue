<template>
    <div>
        <div class="modal-buttontag">            
            <div class="SignPageBtn" @click="handleclick()" data-bs-toggle="modal" :data-bs-target="item">
                <div v-if="movie">
                    <img class="movieimgthumbnail img-thumbnail" :src="movie_url" alt="" style = "border: 3px solid white">>
                    <div class="text-center">
                        <span>{{ item }}</span>
                    </div>
                </div>
                <div v-else>
                    <span>{{ item }}</span>
                </div>

            </div>
        </div>
    </div>
</template>


<script>
const MOVIE_URL = 'https://image.tmdb.org/t/p/w500'
export default {
    name : 'ModalBtn',
    props:{
        target : String,
        movie : Object
    },
    data(){
        return{
            item : null
        }
    },
    created(){
        this.item = this.set_target
        console.log(this.item)
    },
    methods:{
        handleclick(){
            console.log(true)
            return true
        }
    },
    computed:{
        set_target(){
            return `#${this.target}`
        },
        movie_url(){
            return MOVIE_URL + this.movie.poster_path
        }
    }
}
</script>

<style scoped>
.modal-buttontag{
    margin: 0 0 25%;
    height: auto;
    object-fit: contain;
}
.SignPageBtn {
    
    display: flex;
    justify-content: center;
    
    flex-direction: column;
    position: relative; 
    object-fit: contain;
}

.movieimgthumbnail{
    max-height: 100%
}

.text-center {
  width: 100%;
  min-height: 70px;
  
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  bottom: 5px;
  background-color: white;
  color: black;
  border-radius: 3px;
  font-weight: bold;
  font-size: 1.2rem;
}

</style>