<template>
  <div>
    <MovieItem :item="getitem">

    </MovieItem>
  </div>
</template>

<script>
import MovieItem from '@/components/movie/MovieItem.vue';
export default {
  name:'MovieViewTest',
  components:{
    MovieItem
  },
  data(){
    return{
      item : {
    "id": 24,
    "genres": [
        {
            "id": 28,
            "genre_id": 28,
            "genre_name": "Action"
        },
        {
            "id": 80,
            "genre_id": 80,
            "genre_name": "Crime"
        }
    ],
    "movie_id": 24,
    "title": "킬 빌: 1부",
    "overview": "어느 한적한 오후, 행복한 결혼식을 앞둔 더 브라이드와 그녀의 신랑, 그리고 모든 하객들이 의문의 조직에 의해 처참하게 살해당한다. 그로부터 5년 후, 코마상태의 더 브라이드는 죽음 직전까지 갔다가 어렵게 깨어난다. 그리고 피로 얼룩진 과거가 그녀의 뇌리에 스치면서 서서히 복수의 리스트를 작성하기 시작한다. 그녀는 전세계적으로 악명높은 살인조직 데들리 바이퍼의 일원이었고, 조직의 보스인 빌을 포함한 5명의 일원이 새로운 삶을 앞둔 그녀를 처참하게 무너뜨렸음이 밝혀지자, 그녀는 텍사스, 멕시코, 일본을 방문하며 가장 잔인한 복수를 실행하게 되는데...",
    "poster_path": "/lH82lk837fACeVZUmqHH0UiEeWL.jpg",
    "video_path": null,
    "popularity": 39.489,
    "actors": [
        "Uma Thurman",
        "Lucy Liu",
        "Vivica A. Fox",
        "Daryl Hannah",
        "David Carradine"
    ],
    "director": "Robert Rodriguez",
    "score_average": 8,
    "release_date": "2003-10-10",
    "like_users": []
}
    }
  },
  computed:{
    getitem(){
      return this.item
    }
  }
}
</script>

<style>

</style>