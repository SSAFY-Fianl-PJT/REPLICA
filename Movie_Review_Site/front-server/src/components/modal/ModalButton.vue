<template>
    <div>
        <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="set_target">
            테스팅 중 {{ target }}
        </button>
     -->
        <div @click="handleclick()" data-bs-toggle="modal" :data-bs-target="item">
            {{ item }}
        </div>
    </div>
</template>

<script>
export default {
    name : 'ModalBtn',
    props:{
        target : String
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
    }
}
</script>

<style>

</style>