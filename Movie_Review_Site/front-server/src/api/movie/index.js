import api from '@/api/base'

const fetchMovies = async ()=>{
    return api.get('/movies/')
}

const getMovie_Detail = async(params_id)=>{
    return api.get(`/movies/${params_id}/`)
}

export { fetchMovies, getMovie_Detail }