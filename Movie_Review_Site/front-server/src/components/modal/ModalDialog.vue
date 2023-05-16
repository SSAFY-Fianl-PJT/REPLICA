<template>
    <div class="modal fade" :id="set_target" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
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
        name: "ModalDialog",
        props:{
            target : String
        },
        computed:{
            set_target(){
                return `${this.target}`
            }
        }
    }
</script>
<style>

</style>