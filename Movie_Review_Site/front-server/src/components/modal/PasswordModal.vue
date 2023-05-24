<template>
  <div>
    <button class="password-btn" @click="showModal">비밀번호 변경</button>
    <div class="modal fade" ref="modal" tabindex="-1" role="dialog" aria-labelledby="passwordModalLabel"
      aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="passwordModalLabel">비밀번호 변경</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <!-- 비밀번호 변경 폼 -->
            <form @submit.prevent="changePassword">
              <div class="form-group">
                <label for="currentPassword">현재 비밀번호</label>
                <input type="password" class="form-control" id="currentPassword" v-model="passwords.current_password"
                  required>
              </div>
              <div class="form-group">
                <label for="newPassword1">새로운 비밀번호</label>
                <input type="password" class="form-control" id="newPassword1" v-model="passwords.new_password1"
                  required>
              </div>
              <div class="form-group">
                <label for="newPassword2">새로운 비밀번호 확인</label>
                <input type="password" class="form-control" id="newPassword2" v-model="passwords.new_password2"
                  required>
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
export default {
  data() {
    return {
      passwords: {
        current_password: '',
        new_password1: '',
        new_password2: '',
      },
    };
  },
  methods: {
    showModal() {
      this.$refs.modal.show();
    },
    hideModal() {
      this.$refs.modal.hide();
    },
    async changePassword() {
      // 비밀번호 변경 요청 처리
      try {
        await this.$axios.post('/accounts/password/change/', this.passwords);
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
.password-btn {
  font-size: 12px;
  padding: 6px 12px;
  background-color: rgb(61, 153, 112);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
