<template>
  <div v-if="user_test" class="usr-profile-container">
    <div :class="{ backgroundMoviePoster: getWishlist }" >
<!-- <div :class="{ backgroundMoviePoster: getWishlist }" :style="backgroundImageStyle"> -->
    <div class="user-name-block">
        <img :src="TestprofileUrl" class="profile-image" alt="프로필 이미지">
        <div class="user-inform-block">
            <div class="user-details">
                <span class="user-nickname"> {{ user_test.nickname }}  </span>

                <div class="follow-btn-container" v-if="!is_yourSelf">
                    <div class="btn" :class="{ 'active': is_over }" @click="isFollow"  @mouseover="is_over = true" @mouseleave="is_over = false">
                        <span v-if="is_follow">팔로우 취소</span>
                        <span v-else>팔로우</span>
                    <div class="dot"></div>
                    </div>
                </div>

                <!-- <button class="follow-button" v-if="!is_follow" @click="isFollow()">팔로우</button> -->
                <!-- <button class="unfollow-button" v-else @click="isFollow()">팔로우 취소</button> -->
            </div>
            <div class="user-stats">
                <span v-if="get_usr" class="user-nickname following">팔로잉 : {{user_test.followings_count}}</span>
                <span v-if="get_usr" class="user-nickname follower">팔로워 : {{user_test.followers_count}}</span>
            </div>
        </div>
        
        <div class="password-btn-container" v-if="isCurrentUser">
            
            <div class="delete-btn-container" @click="confirmPasswordChange" data-bs-backdrop="true" data-bs-toggle="modal"
            :data-bs-target="modalTarget">
                <button class="password-btn">비밀번호 변경</button>
            </div>

            <PasswordModal ref="passwordModal" />
    
            <div class="delete-btn-container" v-if="isCurrentUser">
                <button class="delete-btn" @click="confirmDeleteUser">회원탈퇴</button>
            </div>
        </div>
       
    </div>
    <hr class="hr-1">
    <div class="movie-lists-for-usr">

        <div class="users-wishlist">
            <h1><span v-if="get_usr" class="user-nickname" style="font-size:50px;">{{user_test.nickname}} 의 찜 리스트</span></h1>



  
        <div class="searchresult-container">
          
          <div class="search-result-found" v-if="Array.isArray(getWishlist)">
            <div class="SearchedMovieGroup" v-for="(item) in getWishlist" :key=item.poster_path>
              <div class="ResultMovieTag">
                <ModalButton 
                :target="squeeze(item.title)"
                :movie="item"
                @open-modal="handleOpenModal"/>
              </div>
        
              <ModalDialog :target="squeeze(item.title)">
                <MovieItem :item="item" />
              </ModalDialog>
            </div>
          </div>
          <div class="search-result-not-found" v-else>
            <h1 >찜한 영화가 없습니다.</h1>
          </div>
        </div>
        
        </div>
        <div class="users-reviews">
            <h1><span v-if="get_usr" class="user-nickname" style="font-size:50px;">{{user_test.nickname}}의 리뷰</span></h1>
            <ArticleList v-if="getUserReviews && getUserReviews.length > 0" :articles="getUserReviews" />
                <h1 class="no-review" v-else>작성한 리뷰가 없습니다.</h1>
        </div>
    </div>

    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList.vue'
import PasswordModal from '@/components/modal/PasswordModal.vue'

import ModalButton from '@/components/modal/ModalButton'
import ModalDialog from '@/components/modal/ModalDialog'
import MovieItem from '@/components/movie/MovieItem.vue'

import {fetchUsrInfo, fetchUsrfollow, fetchReviews, fetchUsrdelete } from '@/api/user'
import _ from 'lodash'
const MOVIE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
    name:'ProfileItem',
    data(){
        return{
            user_test : null,
            is_follow_test : null,
            userReviews: [],
            modalTarget: '#password-modal',
            TestprofileUrl: require('@/assets/TestUsr.png'),
        }
    },
    props:{
        user : String,
    },
    components:{
        ArticleList,
        PasswordModal,
        ModalButton,
        ModalDialog, 
        MovieItem,
    },
    async created(){

        
        console.log("왜 안됨",this.user)
        
        const username = this.user
        await fetchUsrInfo({username})
        .then((res) =>{
            this.user_test = res.data
        })  
        if(this.user_test.nickname !== username){
            try{
                await fetchUsrfollow({username}).then(res =>{
                    this.is_follow_test = res.data.is_followed
                })
                await fetchUsrfollow({username}).then(res =>{
                    this.is_follow_test = res.data.is_followed
                })
            }catch{
                console.log("본인이 접근했습니다.")
            }
        }
        await this.fetchUserReviews();
    },
    watch: {
        '$route.params.username': {
            immediate: true,
            handler: 'fetchData'
        }
    },
    methods: {
    squeeze(data){
      let squeezed_data = data.replace(/\s/g, "")
      return squeezed_data
    },
    async fetchUserReviews() {
      try {
        const response = await fetchReviews(); // 모든 리뷰 불러오기
        const reviews = response.data;
        // console.log('리뷰', reviews)
        // 현재 프로필의 사용자명과 리뷰의 사용자명을 비교하여 일치하는 리뷰만 추가
        this.userReviews = reviews.filter(review => review.username === this.user);
        // console.log("유저 리뷰",this.userReviews)
      } catch (error) {
        console.log(error);
      }
    },
    async fetchData() {
        
        console.log("fetching data for user:", this.$route.params.username);
        await this.$store.dispatch('get_profile4wishList', this.$route.params.username);
        },
    async isFollow(){
        if (this.user !== this.$store.state.user.info.username){
            const username = this.user
            const response = await fetchUsrfollow({username})
            console.log("is_followed:", response.data.is_followed)
            this.is_follow_test = !this.is_follow_test
            if(this.is_follow_test) {
                // if we just followed the user, increment the follower count
                this.user_test.followers_count++
            } else {
                // if we just unfollowed the user, decrement the follower count
                this.user_test.followers_count--
            }
        }else{
            console.log("자기자신을 팔로잉 할 수 없습니다.")
            alert('자기자신을 팔로잉 할 수 없습니다.')
        }
    }, 
    confirmDeleteUser() {
        console.log('확인')
        if (confirm("정말로 회원탈퇴하시겠습니까?")) {
            this.fetchUsrdelete();
        }
        },
        async fetchUsrdelete() {
            const user_id = this.user_test.id;
            try {
                await fetchUsrdelete({user_id}); // 회원 탈퇴 요청
                localStorage.removeItem('vuex'); // 토큰 삭제
                alert("회원 탈퇴되었습니다.");
                this.$router.push({ name: 'MainView' });

            } catch (error) {
                console.error(error);

            }
        },
        confirmPasswordChange() {
            
            this.$refs.passwordModal.showPasswordModal();

        },
     handleOpenModal() {
        this.$store.dispatch('openModal')
        this.showModal = true;
    },
    }, 

    computed : {
        is_yourSelf(){
          if(this.$store.state.user.info && this.user === this.$store.state.user.info.username){
            return true 
          }
          else{
            return false
          }
        },
        get_usr(){
            try {
                // console.log("찾는사람은",this.user_test.username)
                return this.$store.state.user.profile4wishList
            } catch(err) {
            console.log(err)
            return "없습니다."
            }
        },
        getWishlist(){
            
            console.log("위시리스트",this.get_usr.wishlist)
            return this.get_usr.wishlist
        },
        is_follow(){
            return this.is_follow_test
        },
        getUserReviews() {
            return this.userReviews;
        },
        isCurrentUser() {
            try{
                const loggedInUser = this.$store.state.user.info.username;
                console.log(loggedInUser)
                console.log(this.user)
                return loggedInUser === this.user;
            }catch{
                return false
            }
         },
         backgroundImageStyle(){
            return {
                background: `linear-gradient(
                to bottom,
                rgba(0,0,0,0.4) 10%,
                rgba(0,0,0,0.5) 25%,
                rgba(0,0,0,0.7) 40%,
                rgba(0,0,0,9) 50%
                ), url(${MOVIE_URL + _.sample(this.getWishlist).poster_path})`,
                backgroundSize: `contain`,
                backgroundRepeat: 'no-repeat',
                backgroundPosition: 'top',
                
            }
    },
    },
}
</script>

<style scoped>

.usr-profile-container{
    position: relative;
}
.user-nickname{
    font-size : 30px;
    margin: 0 0 15px;
}
.user-name-block{
   min-height: 145px;
    display: flex;
    flex-direction: row;
    position: relative;
    align-items: flex-start;
}
.user-name-block .user-inform-block{
    text-align: start;

    margin-top: 15px;
    margin-bottom: 10px;
    width: 80%;
}

.user-details{
    margin-top: 15px;
    top: 30px; 
    right: 10px;
}

.user-stats{
    top: 70px;
    right: 10px;
}


.profile-image{
    left: 0;
    width: 150px;
    margin: 30px 15px 15px 50px;
    border-radius: 5px;
}

.follower,
.following{
 margin-left: 5px;
 margin-right:5px;
}
.delete-btn-container {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 5px;
  margin-top: 5px;
  
}

.user-name-block .password-btn-container{
    text-align: start;
    margin-right: 15px;
    width: 80%;
}

.password-btn-container {
  display: flex;
  justify-content: flex-end;
  flex-direction: column;
  margin-top: 20px;
}

.delete-btn {
  font-size: 12px;
  padding: 6px 12px;
  background-color: rgb(233, 81, 81);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.password-btn {
  font-size: 12px;
  padding: 6px 12px;
  background-color: rgb(41, 100, 189);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}


.article-view-container {
  padding: 0.25rem;
  
  margin: 0 auto;
  
  color: #ccc;
  text-align: justify;
  font-family: ruluko;
}

@keyframes glow {
  0%{box-shadow: 0 0 2px #43a1ff;}
  50%{box-shadow: 0 0 8px #43a1ff;}
  100%{box-shadow: 0 0 2px #43a1ff;}
}

@-webkit-keyframes glow {
  0%{box-shadow: 0 0 2px #43a1ff;}
  50%{box-shadow: 0 0 8px #43a1ff;}
  100%{box-shadow: 0 0 2px #43a1ff;}
}

@keyframes glowMinor {
  0%{box-shadow: 0 0 2px black;}
  50%{box-shadow: 0 0 8px black;}
  100%{box-shadow: 0 0 2px black;}
}

@-webkit-keyframes glowMinor {
  0%{box-shadow: 0 0 2px black;}
  50%{box-shadow: 0 0 8px black;}
  100%{box-shadow: 0 0 2px black;}
}

h1 {
  margin-top: 50px;
  text-shadow:0 0 15px #43a1ff;
  animation: blin 0.5s linear, glowh1 1.5s ease-in-out infinite;
  -webkit-animation: blin 0.5s linear, glowh1 1.5s ease-in-out infinite;
  color:#43a1ff;
}



.liked-btn-container {
  position: relative;
  left: 0;
    width: 40%;
  box-sizing: border-box;
  }
.liked-btn-container:before, .liked-btn-container:after {box-sizing: border-box;}

.liked-btn-container {
  display: flex;
  justify-content: flex-start;
  
  flex-flow: wrap;
  font-size: 20px;
  font-family: 'Titillium Web', sans-serif;
}


.no-review {
    margin-bottom: 5rem;
}

.btn {
  position: relative;
  margin: 0 auto;
  width: 8em;
  margin-left: 0;
  color: #78bcff;
  border: .15em solid #78bcff;
  border-radius: 5em;
  text-transform: uppercase;
  text-align: center;
  font-size: 1em;
  line-height: 2em;
  cursor: pointer;  
}
.dot {
  content: '';
  position: absolute;
  top: 0;
  width: calc(6em*.2);
  height: 100%;
  border-radius: 100%;
  transition: all 300ms ease;
  display: none;
}
.dot:after {
  content: '';
  position: absolute;
  left: calc(50% - .2em);
  top: -.4em;
  height: .8em;
  width: .8em;
  background: #78bcff;
  border-radius: 1em;
  border: .25em solid #fff;
  box-shadow: 0 0 .7em #fff,
        0 0 2em #78bcff;
}
.btn:hover .dot,
.btn:focus .dot {
  animation: atom 2s infinite linear;
  display: block;
}
@keyframes atom {
  0% {transform: translateX(0) rotate(0);}
  30%{transform: translateX(calc(7em - calc(6.5em*.2))) rotate(0);}
  50% {transform: translateX(calc(7em - calc(6.5em*.2))) rotate(180deg);}
  80% {transform: translateX(0) rotate(180deg);}
  100% {transform: translateX(0) rotate(360deg);}
}


@keyframes glowh1 {
  0%{text-shadow: 0 0 8px #43a1ff;}
  50%{text-shadow: 0 0 20px #43a1ff;}
  100%{text-shadow: 0 0 8px #43a1ff;}
}

@-webkit-keyframes glowh1 {
  0%{text-shadow: 0 0 8px #43a1ff;}
  50%{text-shadow: 0 0 20px #43a1ff;}
  100%{text-shadow: 0 0 8px #43a1ff;}
}

@keyframes blin {
  0%{transform:translate(-2px, -10px);}
  2%{transform:translate(0px, 0px);}
  40%{transform:translateY(4px) skew(10deg);}
  52%{transform:translateY(0px) skew(0deg);}
}

@-webkit-keyframes blin {
  0%{transform:translate(-2px, -10px);}
  2%{transform:translate(0px, 0px);}
  40%{transform:translateY(4px) skew(10deg);}
  52%{transform:translateY(0px) skew(0deg);}
  100%{transform:translateY(0px) skey(0deg);}
}

.search-result-found{
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  flex-wrap: wrap;
}

.SearchedMovieGroup{
  /* width: 20%; */
  margin: 20px;
  object-fit: cover;
} 
.searchresult-container{
  width: 100%;
}

</style>