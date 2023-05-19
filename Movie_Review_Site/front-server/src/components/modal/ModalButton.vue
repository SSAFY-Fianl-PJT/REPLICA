<template>
    <div id="inform-movie-modal">          
        <div class="SignPageBtn" @click="handleclick()" data-bs-toggle="modal" :data-bs-target="item">
            <div id="movie-carrier" v-if="movie">
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
            item : null
        }
    },
    created(){
        this.item = this.set_target
        // console.log(this.item)
    },
    methods:{
        handleclick(){
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
#inform-movie-modal{
    display: flex;
    justify-content: center;
    align-items: center;
}

#movie-carrier{
    flex: 1;
    margin: 0 0 10px;
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

.movieimgthumbnail {
        width: 100%; /* Change this to make the image take the full width of its parent element */
        height: auto; /* This will maintain the aspect ratio of the image */
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
            max-height: 350px;
        }
    }

    /* For devices with width more than 900px */
    @media (min-width: 248px) {
        .movieimgthumbnail {
            max-height: 500px;
        }
    }


</style>