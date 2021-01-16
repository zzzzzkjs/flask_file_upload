import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "@/plugins/axios";

Vue.config.productionTip = false

Vue.prototype.$store = store
Vue.prototype.$getters = store.getters;
Vue.prototype.$commit = store.commit;
Vue.prototype.$dispatch = store.dispatch;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
