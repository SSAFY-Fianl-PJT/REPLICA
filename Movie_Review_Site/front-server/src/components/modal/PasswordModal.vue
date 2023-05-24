<template>
  <div class="modal-container">
    <div class="modal-overlay"></div>
    <div class="modal-content">
      <h3>비밀번호 변경</h3>
      <form @submit.prevent="changePassword">
        <div class="form-group">
          <label for="current-password">현재 비밀번호</label>
          <input type="password" id="current-password" v-model="currentPassword" required>
        </div>
        <div class="form-group">
          <label for="new-password">새로운 비밀번호</label>
          <input type="password" id="new-password" v-model="newPassword" required>
        </div>
        <div class="form-group">
          <label for="confirm-password">새로운 비밀번호 확인</label>
          <input type="password" id="confirm-password" v-model="confirmPassword" required>
        </div>
        <div class="form-actions">
          <button type="submit">비밀번호 변경</button>
          <button type="button" @click="cancel">취소</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
    };
  },
  methods: {
    async changePassword() {
        if (this.newPassword !== this.confirmPassword) {
            alert('새로운 비밀번호가 일치하지 않습니다.');
            return;
        }

      try {
        const response = await api.post('/accounts/password/change/', {
          new_password1: this.newPassword,
          new_password2: this.confirmPassword,
        });

        console.log('비밀번호 변경 성공', response);
        // 비밀번호 변경 성공 처리
        this.updateUserPassword(); // 유저 비밀번호 업데이트 호출

        this.cancel();
      } catch (error) {
        console.error('비밀번호 변경 실패', error);
      }
    },
    cancel() {
      // 모달 닫기
      this.$emit('close');
    },
    async updateUserPassword() {
      try {
        // 유저의 비밀번호 업데이트 API 호출
        await api.put(`/accounts/user/`, {
          password: this.newPassword,
        });

        console.log('유저 비밀번호 업데이트 성공');
        // 유저 비밀번호 업데이트 성공 처리
      } catch (error) {
        console.error('유저 비밀번호 업데이트 실패', error);
        // 유저 비밀번호 업데이트 실패 처리
      }
    },

  },
};
</script>

<style scoped>
.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 4px;
  max-width: 400px;
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-actions {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
}

.form-actions button {
  margin-left: 10px;
}
</style>
