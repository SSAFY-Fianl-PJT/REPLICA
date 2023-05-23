import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vClickOutside from 'v-click-outside'

Vue.use(vClickOutside)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
