import api from '@/api/base'

const fetchArticles = async ()=>{
    return api.get('/community/')
}

const fetchReviews = async (mv_number)=>{
    return api.get(`/movies/${mv_number}/reviews/`)
}

const fetchCreate = async ({title, content, movie_title})=>{
    return api({
        method: 'post',
        url: '/community/',
        data: {title, content, movie_title},
      })
}

const getDetail = async(params_id)=>{
    return api.get(`/community/${ params_id }/`)
}

export { fetchArticles, fetchCreate, getDetail, fetchReviews }