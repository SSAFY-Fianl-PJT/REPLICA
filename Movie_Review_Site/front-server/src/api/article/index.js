import api from '@/api/base'

const fetchArticles = async ()=>{
    return api.get('/api/v1/articles/')
}

const fetchCreate = async ({title, content})=>{
    return api({
        method: 'post',
        url: '/api/v1/articles/',
        data: {title, content},
      })
}

const getDetail = async(params_id)=>{
    return api.get(`/api/v1/articles/${ params_id }/`)
}

export { fetchArticles, fetchCreate, getDetail }