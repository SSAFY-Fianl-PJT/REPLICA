<template>
  <div class="create-review-container">
    <div class="registration-form">
      <header>
        <span class="d-inline-block" tabindex="0" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-content="팝오버 내용">
        <h3>[리뷰 작성]</h3>
        <p>영화 리뷰를 작성해주세요</p>
        <p>더블클릭하면 제목 창이 돌아갑니다.</p>
        </span>
      </header>
        <form @submit.prevent="createArticle" class="form-container">
          
          <div class="button-container">
            <transition name="flip">
              <div v-if="!contentEntry" key="title" class="input-section">
                <a @dblclick.prevent="onClick('contentInput')" data-text="Enter Title">
                  <input ref="titleInput" type="text" v-model.trim="title" placeholder="Enter Title" required />
                </a>
              </div>
              <div v-else key="content" class="input-section">
                <a @dblclick.prevent="onClick('titleInput')" data-text="Enter Content">
                  <input ref="contentInput" type="text" v-model.trim="content" placeholder="Enter Content" required />
                </a>
              </div>
            </transition>
          </div>
            <button class="animated-button" type="submit"><span>&#9993;</span></button>
        </form>
    </div>
  </div>
</template>

<script>
import {fetchCreate} from '@/api/article'
export default {
  data() {
    return {
      title: '',
      content: '',
      contentEntry: false,
    };
  },
  props:{
    movie_title: String
  },
  methods: {
    onClick(inputRef) {
      this.contentEntry = !this.contentEntry;
      this.$nextTick(() => {
        this.$refs[inputRef].focus();
      });
    },
    createArticle() {
      const title = this.title
      const content = this.content
      const movie_title = this.mv_title

    // console.log(title, content, movie_title)
      fetchCreate({ title, content, movie_title })
      .then(() => {
        // console.log(res)
        // this.$router.push({name: 'ArticleView'})
        this.refreshPage()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    refreshPage() {
      this.$router.go(); // 현재 라우트를 다시 로드
    }
  },
  computed:{
    mv_title(){
      return this.movie_title.trim()
    }
  }
};
</script>


<style scoped>
body {
  font-family: "Roboto";
}

.create-review-container{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.registration-form {
    
    width: 400px;
    left: 50%;
    top: 15%;
    background: transparent;
    box-shadow: 0px 0px 100px rgba(255, 255, 255, 0.5);
    border-radius: 1rem;
    margin-right: 1.5rem;
    z-index: 3;
}

.registration-form header {
  z-index: 4;
  background: rgb(255, 255, 255);
  padding: 10px 40px;
  border-radius: 15px 15px 0 0;
  color: rgb(63, 143, 189);
}

.registration-form header p {
  word-spacing: 0px;
  color: rgba(63, 143, 189, 0.842);
  font-size: 17px;
  margin: 0;
  margin-top: 5px;
}


.registration-form h3 {
  font-weight: 900;
  letter-spacing: 1.5px;
  color: rgb(152, 174, 213);
  font-size: 23px;
  text-transform: uppercase;
  margin: 0;
}

.button-container {
  position: relative;
  width: 100%;  /* Adjust according to your needs */
}

.input-section {
  position: absolute;
  width: 100%;
  min-height: 100%;
  max-height: 100%;
  top: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.form-container {
  display: flex;
  flex-direction: row;

  justify-content: space-between; 
}

.button-container .input-section {
  width: 100%;
  font-size: 20px;
  display: flex;
  align-items: center;  /* 추가된 부분 */
  height: 75px;
  border-radius: 0 0 0 15px;
  overflow: hidden;
  z-index: 2;
  box-shadow: 0px 0px 100px rgba(0,0,0,0.2);
}

.registration-form form input {
  background: #f3f3fb; /* Use static color instead of lighten function */
  color: rgb(143, 143, 214);
  border: 0;
  padding: 40px 50px;
  margin: 0;
}

.registration-form form input::placeholder {
  color: rgb(143, 143, 214);
  font-weight: 100;
}

.registration-form form input:focus {
  outline: none;
}

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

.animated-button {
  font-size: 36px; /* 텍스트 크기 조정 */
  font-weight: bold;
  border-radius: 0 0 15px 0;
  
}

.animated-button span {
    color: rgb(143, 143, 214);
    margin-right: 0px; /* 화살표와 텍스트 사이 간격 조정 */
    transition: transform 0.3s ease-in-out;
}

.animated-button:hover span {
  transform: translateY(-15px); /* 오른쪽으로 이동할 거리 조정 */
}

.back {
  background: linear-gradient(120deg, rgb(100, 57, 134), rgb(152, 174, 213));
  width: 100%;
  height: 100%;
}

.flip-enter-active, .flip-leave-active {
  transition: transform 0.7s;
  transform: translateY(0);
  transform-origin: center;
}
.flip-enter, .flip-leave-to {
  transform-origin: left top;
  transform: rotateX(90deg);
}


</style>
