<template>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="set_target">
        테스팅 중 {{ target }}
    </button>
</template>

<script>
export default {
    name : 'ModalBtn',
    props:{
        target : String
    },
    computed:{
        set_target(){
            return `#${this.target}`
        }
    }
}
</script>

<style>

</style>