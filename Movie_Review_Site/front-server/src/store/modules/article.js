// import api from '@/api/base.js'
import { fetchArticles } from '@/api/article'
export default {
    state : {
        articles: [],
    },
    mutations:{
        GET_ARTICLES(state, articles) {
            state.articles = articles
        },
    },
    actions:{
        getArticles(context) {

            fetchArticles()
            .then((res) => {
              console.log(res)
              context.commit('GET_ARTICLES', res.data)
            })
            .catch((err) => {
            console.log(err)
            })
        },
    }
}