import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueNativeSock from 'vue-native-websocket'

Vue.config.productionTip = false

Vue.use(VueNativeSock, process.env.VUE_APP_KODI, 
        { reconnection: true, format: 'json'  })

new Vue({
 vuetify,
  render: h => h(App)
}).$mount('#app')
