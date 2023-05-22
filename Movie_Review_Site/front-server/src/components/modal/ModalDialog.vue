<template>
    <div class="modal fade" :id="set_target" tabindex="-1" :aria-labelledby="set_target" aria-hidden="true">
        <div class="modal-dialog modal-xl modal-dialog-scrollable modal-dialog-centered">
            <div class="modal-content modal-xl">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" :id="set_target">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                    <div class="modal-body">
                    <slot>
                        <!-- 이곳에 component를 넣습니다 -->
                    </slot>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Understood</button>
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
        // console.log(this.item)
    },
    methods:{
        handleclick(){
            return true
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