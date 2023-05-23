import api from '@/api/base'

const fetchLogin = async ({username, password})=>{            
    return api({
        method: 'post',
        url: `/accounts/login/`,
        data: {
            username, password
        }
    })
}

const fetchLogout = async ()=>{            
    return api({
        method: 'post',
        url: `/accounts/logout/`,
    })
}

const fetchSignup = async ({username, nickname, password1, password2})=>{
    return api({
        method: 'post',
        url: `/accounts/signup/`,
        data: {
            username, nickname, password1, password2
        }
    })
}

const tk2Ur = () =>{
    return api.get('/accounts/user-info/')
}

const fetchUsrInfo = ({username}) =>{
    return api.get(`/accounts/profile/${username}`)
}


const fetchUsrfollow = ({username}) =>{
    return api.post(`/accounts/${username}/follow/`)
}

const fetchReviews = () =>{
    return api.get(`/community/`)
}

const fetchUsrdelete = ({user_id}) =>{
    console.log('z')
    return api.post(`/accounts/user-delete/${user_id}/`)
}

export { fetchLogin, fetchLogout, fetchSignup, fetchUsrInfo, tk2Ur,fetchUsrfollow, fetchReviews, fetchUsrdelete }