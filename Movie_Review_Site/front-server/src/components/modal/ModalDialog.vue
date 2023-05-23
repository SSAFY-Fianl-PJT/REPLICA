<template>
    <div class="modal fade" :id="set_target" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" :aria-labelledby="set_target" aria-hidden="true" >
        <div class="modal-dialog modal-xl modal-dialog-scrollable modal-dialog-centered">
            <div class="modal-content modal-xl">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" :id="set_target">{{ item }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" @click="handleCloseModal" aria-label="Close"></button>
                </div>
                    <div class="modal-body">
                    <slot>
                        <!-- 이곳에 component를 넣습니다 -->
                    </slot>
                </div>
            </div>
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
        console.log("에혀",this.item)
    },
    methods:{ 
        handleCloseModal(){
            this.$emit('close')
        }
    },
    computed:{
        set_target(){
            return `${this.target}`
        },
    }
}
</script>
<style scoped>
.modal-dialog-centered {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: calc(100% - (1.75rem * 2));
}
</style>