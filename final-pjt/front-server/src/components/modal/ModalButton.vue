<template>
    <div id="inform-movie-modal">          
        <div class="SignPageBtn" @click="handleclick" data-bs-backdrop="true" data-bs-toggle="modal" :data-bs-target="item">
            <div class="movie-carrier" v-if="movie">
                <img class="movieimgthumbnail img-thumbnail" :src="movie_url" alt="" style = "border: 3px solid white">
            </div>
            <div v-else>
                <span>{{ item }}</span>
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
            item : null,
        }
    },
    mounted(){
        this.item = this.set_target
        // console.log(this.item)
    },
    methods:{
        handleclick(){
            
            this.$emit('open-modal', this.movie);
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


/* #movie-carrier {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    display: flex;
    justify-content: center;
    align-items: center;
} */

#inform-movie-modal{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

.movie-carrier{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    flex: 1;
    padding: 20px 0 20px;
    /* margin: 0 0 10px; */
    object-fit: contain;
}

.SignPageBtn {
    
    display: flex;
    justify-content: center;
    height: 100%;
    flex-direction: column;
    position: relative; 
    object-fit: contain;
}

.movieimgthumbnail {
    width: auto;
    height: 75%;
    object-fit: contain;
}

    /* For devices with width less than or equal to 600px */
    @media (max-width: 100px) {
        .movieimgthumbnail {
            max-height: 200px;
        }
    }

    /* For devices with width between 601px and 900px */
    @media (min-width: 101px) and (max-width: 247px) {
        .movieimgthumbnail {
            max-height: 250px;
        }
    }

    /* For devices with width more than 900px */
    @media (min-width: 248px) {
        .movieimgthumbnail {
            max-height: 300px;
        }
    }


</style>
