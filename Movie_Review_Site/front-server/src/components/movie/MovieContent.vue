<template>
    <div>

        <modal-form v-if="items" :Comps="getItems" targetSlot="Movie-Item">

            <template v-slot:Movie-Item>
                <MovieItem/>
            </template>

        </modal-form>
        
    </div>
    
</template>

<script>
import ModalForm from '@/components/modal/ModalForm'
import MovieItem from '@/components/movie/MovieItem'
export default {
    name: 'MovieContents',
    components:{
        ModalForm,
        MovieItem
    },
    props:{
        items: Array
    },
    methods:{
        handler(){
            console.log("하위",this.items)
        }
    },
    computed: {
        getItems(){
            console.log("이건 무비리스트", this.items)
            return this.items
        }
    }
}
</script>

<style>

</style>