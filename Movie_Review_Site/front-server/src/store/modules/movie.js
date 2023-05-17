import { getImg } from '@/api/movie'
export default {
    state : {

    },
    mutations:{

    },
    actions:{
        async getImage() {

          return await getImg('/75aHn1NOYXh4M7L5shoeQ6NGykP.jpg')
        },
    }
}