// import api from '@/api/base.js'
import { fetchArticles, fetchReviews } from '@/api/article'
export default {
    state : {
        articles: [],
        reviews: [],
    },
    mutations:{
        GET_ARTICLES(state, articles) {
            state.articles = articles
        },
        GET_REVIEWS(state, reviews){
            
            state.reviews = reviews
        }
    },
    actions:{
        getArticles(context) {

            fetchArticles()
            .then((res) => {
            //   console.log(res)
              context.commit('GET_ARTICLES', res.data)
            })
            .catch((err) => {
            console.log(err)
            })
        },

        async getReviews(context, mv_number) {
            let review = null
            await fetchReviews(mv_number)
            .then((res) => {
                //   console.log(res)
                context.commit('GET_REVIEWS', res.data)
                // console.log("이게 결과입니다.",res.data)
                review = res.data
            })
            .catch((err) => {
                console.log(err)
            })
            return review
        },
    }
}