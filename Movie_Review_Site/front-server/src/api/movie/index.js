import api from '@/api/base'

const fetchMovies = async ()=>{
    return api.get('/movies/')
}

const fetchSearchMovies = async (searchParams) => {
    return api({
        method: 'get',
        url: '/movies/search/',
        params: searchParams
    })
}

const getMovie_Detail = async(params_id)=>{
    return api.get(`/movies/${params_id}/`)
}

const WishList = async({movie_id})=>{
    return api.post(`/movies/${movie_id}/wishlist/`)
}

const MyWishList = async({user_name}) => {
    return api.get(`/accounts/my_wishlist/${user_name}/`)
}
const fetchRecommend = async({username}) => {
    console.log("ㅎㅇ",username)
    return api.get(`/movies/recommend/${username}/`)
}

const fetchRecommendByKeyword = async(keyword) =>{
    return api.get(`/movies/recommend/?keyword=${keyword}`)
}

export { fetchMovies, getMovie_Detail, 
    fetchSearchMovies, fetchRecommend, fetchRecommendByKeyword,
    WishList, MyWishList}