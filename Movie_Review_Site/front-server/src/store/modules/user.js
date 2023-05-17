import api from '@/api/base.js'
import { fetchLogin, fetchLogout, fetchSignup } from '@/api/user'

export default {
    state : {
        token: null,
    },
    getters: {
        isLogin(state) {
            if (state.token === null){
                api.clearToken()
            }else{
                api.setToken(state.token)
            }
            return state.token ? true : false
        },
    },
    mutations:{
        SAVE_TOKEN(state, token) {
            state.token = token
        },
    },
    actions:{
        async signUp(context, payload) {
            const username = payload.username
            const password1 = payload.password1
            const password2 = payload.password2
            await fetchSignup({username, password1, password2})
            .then((res) => {
                context.commit('SAVE_TOKEN', res.data.key )
            })
            .catch((err) => {
                console.log(err)
            })
        },

        async login(context, payload) {
            const username = payload.username
            const password = payload.password

            await fetchLogin({ username, password })
            .then((res) => {
                context.commit('SAVE_TOKEN', res.data.key)
                console.log(res.data.key)
            })
            .catch((err) => {
                console.log(err)})
        },

        async logout(context){
            await fetchLogout()
            .then(() => {
                context.commit('SAVE_TOKEN', null)
                localStorage.removeItem('user.token')
            })
            .catch((err) => console.log(err))
        }
    }
}