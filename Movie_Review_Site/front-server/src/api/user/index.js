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

export { fetchLogin, fetchLogout, fetchSignup }