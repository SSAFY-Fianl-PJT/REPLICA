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

const updateComment = async ({review_id, comment_id, editContent}) => {
    const response = await api.put(`/community/${review_id}/comments/${comment_id}/`, editContent);
    return response.data;
  }

const deleteComment = async ({review_id, comment_id}) => {
    return api.delete(`/community/${review_id}/comments/${comment_id}/`);
}

const getComments = async (review_id) =>{
    return api.get(`/community/${review_id}/comments/`)
}

const createComments = async (review_id, {content}) =>{
    return api.post(`/community/${review_id}/comments/`,{content})
}

export { fetchArticles, fetchCreate, getDetail, fetchReviews, updateArticle, deleteArticle, 
    getComments, createComments, updateComment, deleteComment }