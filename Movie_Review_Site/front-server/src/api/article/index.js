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

const updateArticle = async (params_id, updatedData) => {
    const response = await api.put(`/community/${params_id}/`, updatedData);
    return response.data;
  }

const deleteArticle = async (params_id) => {
    return api.delete(`/community/${params_id}/`);
}
export { fetchArticles, fetchCreate, getDetail, fetchReviews, updateArticle, deleteArticle }