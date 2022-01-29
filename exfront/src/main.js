// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import axios from 'axios';
import VueAxios from 'vue-axios';

import Vue from 'vue';
import App from './App';
import router from './router';

Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

axios.interceptors.response.use(response => response, (error) => {
  if (error.response.status === 404) {
    router.push({ name: '404' });
  }
  return Promise.reject(error.response);
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  axios,
});
