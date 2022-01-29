import Vue from 'vue';
import Router from 'vue-router';
import PromoPage from '../views/PromoPage';
import NotExist from '../views/NotExist';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/:url',
      name: 'PromoPage',
      component: PromoPage,
    },
    {
      path: '/404',
      name: '404',
      component: NotExist,
    },
  ],
});
