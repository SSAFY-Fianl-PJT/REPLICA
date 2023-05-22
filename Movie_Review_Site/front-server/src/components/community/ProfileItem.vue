<template>
  <div v-if="user_test" class="usr-profile-container">
    <div>렌덤 무비포스터 있으면 좋을듯</div>
    <div class="user-name-block">
        <span class="user-nickname">{{ user_test.nickname }}</span>
            <button v-if="!is_follow" @click="isFollow()">팔로우</button>
            <button v-else @click="isFollow()">팔로우 취소</button>
        <hr>
        <span v-if="get_usr" class="user-nickname">팔로잉 : {{user_test.followings_count}}</span>
        <span v-if="get_usr" class="user-nickname">팔로워 : {{user_test.followers_count}}</span>
    </div>
    <div class="movie-lists-for-usr">

        <div class="users-wishlist">
            <span v-if="get_usr" class="user-nickname">{{user_test.nickname}} 의 찜 리스트</span>
            <MovieContent  v-if="getWishlist  && getWishlist.length > 0" :items="getWishlist"/>
                
        </div>
        <div class="users-wishlist">
            <span v-if="get_usr" class="user-nickname">개봉 예정작</span>
            <MovieContent  v-if="upcomingmovies  && upcomingmovies.length > 0" :items="upcomingmovies"/>
        </div>
    </div>

    {{ get_usr }}
  </div>
</template>

<script>
import MovieContent from '@/components/movie/MovieContent.vue';
import {fetchUsrInfo, fetchUsrfollow} from '@/api/user'

export default {
    name:'ProfileItem',
    data(){
        return{
            user_test : null,
            is_follow_test : null,
        }
    },
    props:{
        user : String,
    },
    components:{
        MovieContent,
    },
    async created(){
        const username = this.user
        // console.log("살려줘",username)
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
    },
    watch: {
        '$route.params.username': {
            immediate: true,
            handler: 'fetchData'
        }
    },
    methods: {
    async fetchData() {
        // 여기에 새로운 사용자 데이터를 불러오는 로직을 구현하세요.
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
            }
        }, 
        
    },  
    computed : {
        get_usr(){
            try {
                // console.log("이게 말이되나",this.$store.state.user.profile)
                return this.$store.state.user.profile
            } catch(err) {
            console.log(err)
            return "없습니다."
            }
        },
        getWishlist(){
            // console.log(this.get_usr.wishlist, "이거 되나?")
            // console.log("이건 무비리스트", this.items)
            return this.get_usr.wishlist
        },
        upcomingmovies(){
            return this.$store.state.movie.upcoming_movies.slice(0,5)
        },
        is_follow(){

            return this.is_follow_test
        }
    },
}
</script>

<style scoped>
.user-nickname{
    font-size : 30px;
    margin: 0 0 15;
}
</style>