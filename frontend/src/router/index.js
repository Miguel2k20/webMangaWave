import { createRouter, createWebHistory } from 'vue-router';
import Home from '../sessions/Home.vue';
import About from '../sessions/AboutUs.vue';
import SearchMangas from '../sessions/SearchMangas.vue'
import MangaInfo from '@/sessions/MangaInfo.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about-us',
    name: 'SobreNos',
    component: About
  },
  {
    path: '/search-mangas',
    name: 'SearchMangas',
    component: SearchMangas,
    props: route => ({ mangaName: route.query.manga })
  },
  {
    path: '/info-mangas',
    name: 'MangaInfo',
    component: MangaInfo,
    props: route => ({ mangaId: route.query.id })
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;