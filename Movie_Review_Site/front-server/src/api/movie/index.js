import api from '@/api/base'

const fetchMovies = async ()=>{
    return api.get('/movies/')
}

const fetchSearchMovies = async ({title, genres, year})=>{
    return api({
        method:'get',
        url:'/movies/search',
        params:{title, genres, year}
    })
}

const getMovie_Detail = async(params_id)=>{
    return api.get(`/movies/${params_id}/`)
}

export { fetchMovies, getMovie_Detail, fetchSearchMovies}