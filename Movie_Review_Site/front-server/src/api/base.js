import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL

const api = axios.create({
    baseURL: API_URL,
})

// api token 설정 메소드 정의
api.setToken = function(token){
    this.defaults.headers.common['Authorization'] = `Token ${token}`
}
// api token 제거 메소드 정의
api.clearToken = function(){
    delete this.defaults.headers.common['Authorization']
}

export default api;