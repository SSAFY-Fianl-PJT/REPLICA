<template>
  <div v-if="user_test" class="usr-profile-container">
    <div>렌덤 무비포스터 있으면 좋을듯</div>
    <div class="user-name-block">
        <span class="user-nickname">{{ user_test.nickname }}  </span>
            <button v-if="!is_follow" @click="isFollow()">   팔로우</button>
            <button v-else @click="isFollow()">팔로우 취소</button>
        <hr>
        <span v-if="get_usr" class="user-nickname">팔로잉 : {{user_test.followings_count}}</span>
        <span v-if="get_usr" class="user-nickname">팔로워 : {{user_test.followers_count}}</span>
        <br><br>
    </div>
    <div class="movie-lists-for-usr">

        <div class="users-wishlist">
            <span v-if="get_usr" class="user-nickname">{{user_test.nickname}} 의 찜 리스트</span>
            <MovieContent  v-if="getWishlist  && getWishlist.length > 0" :items="getWishlist"/>
                <p v-else>찜한 영화가 없습니다.</p>
        </div>
        <div class="users-reviews">
            <span v-if="get_usr" class="user-nickname">{{user_test.nickname}}의 리뷰</span>
            <ArticleList v-if="getUserReviews && getUserReviews.length > 0" :articles="getUserReviews" />
                <p v-else>작성한 리뷰가 없습니다.</p>
        </div>
    </div>
    <div class="password-btn-container" v-if="isCurrentUser">
      <button class="password-btn" @click="confirmPasswordChange">비밀번호 변경</button>
      <PasswordModal ref="passwordModal" />
    </div>

    <div class="delete-btn-container" v-if="isCurrentUser">
      <button class="delete-btn" @click="confirmDeleteUser">회원탈퇴</button>
    </div>
  </div>
</template>

<script>
import MovieContent from '@/components/movie/MovieContent.vue';
import ArticleList from '@/components/community/ArticleList.vue'
import PasswordModal from '@/components/modal/PasswordModal.vue'
import {fetchUsrInfo, fetchUsrfollow, fetchReviews, fetchUsrdelete } from '@/api/user'

export default {
    name:'ProfileItem',
    data(){
        return{
            user_test : null,
            is_follow_test : null,
            userReviews: [],
        }
    },
    props:{
        user : String,
    },
    components:{
        MovieContent,
        ArticleList,
        PasswordModal,
    },
    async created(){
        console.log("??뭐지",this.user)
        const username = this.user
        await fetchUsrInfo({username})
        .then((res) =>{
            this.user_test = res.data
        })  

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
        await this.fetchUserReviews();
    },
    watch: {
        '$route.params.username': {
            immediate: true,
            handler: 'fetchData'
        }
    },
    methods: {
    async fetchUserReviews() {
      try {
        const response = await fetchReviews(); // 모든 리뷰 불러오기
        const reviews = response.data;
        console.log('리뷰', reviews)
        // 현재 프로필의 사용자명과 리뷰의 사용자명을 비교하여 일치하는 리뷰만 추가
        this.userReviews = reviews.filter(review => review.username === this.user);
        console.log(this.userReviews)
      } catch (error) {
        console.log(error);
      }
    },
    async fetchData() {
        
        console.log("fetching data for user:", this.$route.params.username);
        this.$store.dispatch('get_profile', this.$route.params.username);
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
        confirmPasswordchange() {
            if (confirm("비밀번호를 변경하시겠습니까?")) {
                this.$refs.passwordModal.showModal();
            }
        }
 
    },  
    computed : {
        get_usr(){
            try {
                return this.$store.state.user.profile
            } catch(err) {
            console.log(err)
            return "없습니다."
            }
        },
        getWishlist(){
            return this.get_usr.wishlist
        },
        is_follow(){
            return this.is_follow_test
        },
        getUserReviews() {
            return this.userReviews;
        },
        isCurrentUser() {
            const loggedInUser = this.$store.state.user.info.username;
            console.log(loggedInUser)
            console.log(this.user)
            return loggedInUser === this.user;
  },
    },
}
</script>

<style scoped>
.user-nickname{
    font-size : 30px;
    margin: 0 0 15;
}

.delete-btn-container {
  display: flex;
  justify-content: flex-end;
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
</style>