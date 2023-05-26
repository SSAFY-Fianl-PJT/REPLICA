import axios from 'axios'
// const API_URL = process.env.VUE_APP_API_URL
const API_URL ='https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_API_KEY = 'AIzaSyBlNSqg-9WQraWKrdqLdMqh-L0umq_73eA'

const api = axios.create({
    baseURL: API_URL,
    params: {
      key: YOUTUBE_API_KEY
    }
})


export default api;