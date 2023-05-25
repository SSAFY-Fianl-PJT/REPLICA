<template>
  <div class="create-review-container">
    <div class="registration-form">
      <header>
        <span class="d-inline-block" tabindex="0" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-content="팝오버 내용">
        <h3>[리뷰 작성]</h3>
        <p>영화 리뷰를 작성해주세요</p>
        </span>
        <div class="starpoint_wrap">
          <div class="starpoint_box">
            <label for="starpoint_1" class="label_star" @mouseover="showScore"   @click="clickScore" title="1"><span class="blind">1점</span></label>
            <label for="starpoint_2" class="label_star" @mouseover="showScore"   @click="clickScore" title="2"><span class="blind">2점</span></label>
            <label for="starpoint_3" class="label_star" @mouseover="showScore"   @click="clickScore" title="3"><span class="blind">3점</span></label>
            <label for="starpoint_4" class="label_star" @mouseover="showScore"   @click="clickScore" title="4"><span class="blind">4점</span></label>
            <label for="starpoint_5" class="label_star" @mouseover="showScore"   @click="clickScore" title="5"><span class="blind">5점</span></label>
            <label for="starpoint_6" class="label_star" @mouseover="showScore"   @click="clickScore" title="6"><span class="blind">6점</span></label>
            <label for="starpoint_7" class="label_star" @mouseover="showScore"   @click="clickScore" title="7"><span class="blind">7점</span></label>
            <label for="starpoint_8" class="label_star" @mouseover="showScore"   @click="clickScore" title="8"><span class="blind">8점</span></label>
            <label for="starpoint_9" class="label_star" @mouseover="showScore"   @click="clickScore" title="9"><span class="blind">9점</span></label>
            <label for="starpoint_10" class="label_star" @mouseover="showScore" @click="clickScore"  title="10"><span class="blind">10점</span></label>
            <input type="radio" name="starpoint" id="starpoint_1" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_2" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_3" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_4" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_5" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_6" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_7" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_8" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_9" class="star_radio">
            <input type="radio" name="starpoint" id="starpoint_10" class="star_radio">
            <span class="starpoint_bg"></span>
          </div>
          <div class="score_display" v-if="score">{{ score }}점</div>
          <div class="score_display" v-else>0점</div>
        </div>
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
      scoreSelected: false,
      score:null
    };
  },
  props:{
    movie_title: String,
    movie_id: {
      type: Number, 
      required: true 
    }
  },

  methods: {
    showScore(event) {
      if (!this.scoreSelected) {
        this.score = event.target.title;
      }
    },

    clickScore() {
      this.scoreSelected = !this.scoreSelected;
    },
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
      const rating = this.score
      console.log(rating)
    // console.log(title, content, movie_title)
      fetchCreate({ title, content, movie_title, rating })
      .then(() => {
        console.log("res, ", this.movie_id)
        this.$router.push({name: 'MovieViewTest',params : {id:this.movie_id}})
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
  margin-top: 25px;
}

.registration-form {
    
    width: 400px;
    left: 50%;
    top: 15%;
    background: transparent;
    box-shadow: 0px 0px 50px  rgba(152, 174, 213, 0.7);
  
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

.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}
 
.score_display {
  margin-left: 10px; /* starpoint_box와 score_display 사이의 간격 조절 */
}
.starpoint_wrap {
  display: flex;
  align-items: center; /* 세로 중앙 정렬 */
}
.starpoint_box, .score_display {
  display: inline-block;
}
.starpoint_box{position:relative;background:url(https://ido-archive.github.io/svc/etc/element/img/sp_star.png) 0 0 no-repeat;font-size:0;}
.starpoint_box .starpoint_bg{display:block;position:absolute;top:0;left:0;height:18px;background:url(https://ido-archive.github.io/svc/etc/element/img/sp_star.png) 0 -20px no-repeat;pointer-events:none;}
.starpoint_box .label_star{display:inline-block;width:10px;height:18px;box-sizing:border-box;}
.starpoint_box .star_radio{opacity:0;width:0;height:0;position:absolute;}
.starpoint_box .star_radio:nth-of-type(1):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(1):checked ~ .starpoint_bg{width:10%;}
.starpoint_box .star_radio:nth-of-type(2):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(2):checked ~ .starpoint_bg{width:20%;}
.starpoint_box .star_radio:nth-of-type(3):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(3):checked ~ .starpoint_bg{width:30%;}
.starpoint_box .star_radio:nth-of-type(4):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(4):checked ~ .starpoint_bg{width:40%;}
.starpoint_box .star_radio:nth-of-type(5):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(5):checked ~ .starpoint_bg{width:50%;}
.starpoint_box .star_radio:nth-of-type(6):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(6):checked ~ .starpoint_bg{width:60%;}
.starpoint_box .star_radio:nth-of-type(7):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(7):checked ~ .starpoint_bg{width:70%;}
.starpoint_box .star_radio:nth-of-type(8):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(8):checked ~ .starpoint_bg{width:80%;}
.starpoint_box .star_radio:nth-of-type(9):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(9):checked ~ .starpoint_bg{width:90%;}
.starpoint_box .star_radio:nth-of-type(10):hover ~ .starpoint_bg,
.starpoint_box .star_radio:nth-of-type(10):checked ~ .starpoint_bg{width:100%;}

.blind{position:absolute;clip:rect(0 0 0 0);margin:-1px;width:1px;height: 1px;overflow:hidden;}

</style>
