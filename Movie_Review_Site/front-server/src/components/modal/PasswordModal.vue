<template>
  <div>
     <div class="modal fade" :class="{ show: showModal }" ref="modal" :id="modalId" tabindex="-1" role="dialog" aria-labelledby="passwordModalLabel"
      aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="passwordModalLabel">비밀번호 변경</h5>
            <!-- <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="hideModal">
              <span aria-hidden="true">&times;</span>
            </button> -->
          </div>
          <div class="modal-body">
            <!-- 비밀번호 변경 폼 -->
            <form @submit.prevent="fetchPasswordChange">
              <div class="form-group">
                <label for="currentPassword">현재 비밀번호</label>
                <input type="password" class="form-control" id="currentPassword" v-model="passwords.current_password" required>
              </div>
              <div class="form-group">
                <label for="newPassword1">새로운 비밀번호</label>
                <input type="password" class="form-control" id="newPassword1" v-model="passwords.new_password1" required>
              </div>
              <div class="form-group">
                <label for="newPassword2">새로운 비밀번호 확인</label>
                <input type="password" class="form-control" id="newPassword2" v-model="passwords.new_password2" required>
              </div>
              <button type="submit" class="btn btn-primary">변경</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {fetchPasswordChange} from '@/api/user'

export default {
  data() {
    return {
      modalId: 'password-modal',
      passwords: {
        current_password: '',
        new_password1: '',
        new_password2: '',
      },
      showModal: false,
    };
  },
  methods: {
    showPasswordModal() {
      this.showModal = true;
    },
    hideModal() {
      this.$store.dispatch('closeModal')
      this.showModal = false;
      
    },
    async fetchPasswordChange() {
      if (!this.passwords.new_password1 || !this.passwords.new_password2) {
        alert('새로운 비밀번호를 입력해주세요.');
        return;
      }
      
      if (this.passwords.new_password1 !== this.passwords.new_password2) {
        alert('새로운 비밀번호가 일치하지 않습니다.');
        return;
      }
      // 비밀번호 변경 요청 처리
      const { new_password1, new_password2 } = this.passwords
      try {
      await fetchPasswordChange({
        // current_password: this.passwords.current_password,
        new_password1: new_password1,
        new_password2: new_password2,
      });
      this.hideModal();
      alert('비밀번호가 변경되었습니다.');
    } catch (error) {
      console.error(error);
      alert('비밀번호 변경에 실패했습니다. 다시 시도해주세요.');
    }
    },
  },
};
</script>

<style scoped>
.modal {
  display: none;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999;
  overflow: auto;
  color: black;
}
</style>
