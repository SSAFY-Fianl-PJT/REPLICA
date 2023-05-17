import axios from "axios";

// const IMG_URL = process.env.VUE_APP_IMG_URL
const IMG_URL_ROOT ='https://image.tmdb.org/t/p/w500'
console.log(IMG_URL_ROOT)
const api = axios.create({
  baseURL: IMG_URL_ROOT,
})

const getImg = async (img_url)=>{
  console.log("이곳에서", img_url)
  return api.get(img_url)
}


export { getImg };