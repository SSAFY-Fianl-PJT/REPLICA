<template>
  <div class="usr-profile-container">
    <div>렌덤 무비포스터 있으면 좋을듯</div>
    <div class="user-name-block">
        <span class="user-nickname">{{get_usr.nickname}}</span>
        <button>팔로우</button>
        <button>팔로잉</button>
        <hr>
        <span v-if="get_usr" class="user-nickname">팔로잉 : {{get_usr.followings_count}}</span>
        <span v-if="get_usr" class="user-nickname">팔로워 : {{get_usr.followers_count}}</span>
    </div>
    <div class="movie-lists-for-usr">

        <div class="users-wishlist">
            <span v-if="get_usr" class="user-nickname">{{get_usr.nickname}} 의 찜 리스트</span>
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

export default {
    name:'ProfileItem',
    props:{
        user:String
    },
    components:{
        MovieContent
    },
    async created(){
        await this.$store.dispatch('getMovies')
        this.$store.dispatch('get_profile', this.user)
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
            console.log(this.get_usr.wishlist, "이거 되나?")
            // console.log("이건 무비리스트", this.items)
            return this.get_usr.wishlist
        },
        upcomingmovies(){
            return this.$store.state.movie.upcoming_movies.slice(0,5)
        },
    }
}
</script>

<style scoped>



.user-nickname{
    font-size : 30px;
    margin: 0 0 15;
}
</style>