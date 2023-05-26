<template>
  <div class="commentingbox-container">

    <div class="registration-form">
      <header>
        <h3>덧글 작성</h3>
        <p>덧글을 작성해주세요</p>
      </header>
      <form @submit.prevent="submitForm">
        <div class="input-section">
          <input type="text" v-model="content" placeholder="Comments" required>
          <button class="animated-button"><span>&#10225;</span></button>
        </div>
      </form>
  
    </div>
  </div>
</template>

<script>
import {createComments} from '@/api/article'
export default {
    name:'CommentingBox',
    props:{
        review_id: {
            type: Number,
            required: true
        }
    },
    data(){
        return{
            content: '',
            isSuccess: false,
            commentlist : [],
        }
    },
    methods: {
        submitForm() {
            // Here, perform form submission logic
            const content = this.content
            createComments(this.review_id, {content})
            .then(() => {
                this.isSuccess = true;
                this.content = '';
                this.$emit('comment-added',true);
            });
        }
    }
}
</script>
<style scoped>
/* Set global font family */
.commentingbox-container {
  display: flex;
  font-family: "Roboto";
  justify-content: center;
}

/* Define the form's size, position, and background */
.registration-form {
    width: 400px;
    left: 50%;
    top: 15%;
    background: transparent;
    margin: 0.5rem;
    box-shadow: 0px 0px 50px  rgba(152, 174, 213, 0.7);
    justify-content: center;
}

/* Style the header of the form */
.registration-form header {
  z-index: 4;
  background: white;
  padding: 10px 40px;
  border-radius: 15px 15px 0 0;
}

.registration-form h3 {
  font-weight: 900;
  letter-spacing: 1.5px;
  color: rgb(152, 174, 213);
  font-size: 23px;
  text-transform: uppercase;
  margin: 0;
}



.animated-button {
  font-size: 36px; /* 텍스트 크기 조정 */
  font-weight: bold;
}

.animated-button span {
    color: rgb(143, 143, 214);
    margin-right: 0px; /* 화살표와 텍스트 사이 간격 조정 */
    transition: transform 0.3s ease-in-out;
}
.animated-button:hover span {
  transform: translateY(15px); /* 오른쪽으로 이동할 거리 조정 */
}

/* Define the background gradient and set its dimensions to fill the entire page */
.back {
  background: linear-gradient(120deg, rgb(100, 57, 134), rgb(152, 174, 213));

  width: 100%;
  height: 100%;
}


/* Style the header of the form */
.registration-form header {
  z-index: 4;
  background: white;
  padding: 10px 40px;
  border-radius: 15px 15px 0 0;
}


/* Style the sub-title of the form */
.registration-form header p {
  word-spacing: 0px;
  color: rgb(159, 172, 182);
  font-size: 17px;
  margin: 0;
  margin-top: 5px;
}

/* Style the input sections of the form */
.registration-form .input-section {
    width: 100%;
    font-size: 20px; /* 텍스트 크기 조정 */
    /* 기타 스타일 */
    display: flex;
    left: 50%;
    height: 75px; /* Use static value for $input-height */
    border-radius: 0 0 15px 15px;
    overflow: hidden;
    z-index: 2;
    box-shadow: 0px 0px 100px rgba(0,0,0,0.2);
    transition: all 0.2s ease-in;
}

/* Define styles for input elements within the form */
.registration-form form input {
  background: #f3f3fb; /* Use static color instead of lighten function */
  color: rgb(143, 143, 214);
  width: 80%;
  border: 0;
  padding: 20px 40px;
  margin: 0;
}

.registration-form form input:focus {
  outline: none;
}

.registration-form form input::placeholder {
  color: rgb(143, 143, 214);
  font-weight: 100;
}

/* Define styles for the animated button */
.registration-form .animated-button {
  width: 20%;
  background-color: rgb(212, 212, 255);
  border: none;
}

.registration-form .animated-button span {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  line-height: 75px; /* Use static value for $input-height */
  text-align: center;
  height: 75px; /* Use static value for $input-height */
  transition: all 0.2s ease-in;
  outline: none;
}




</style>