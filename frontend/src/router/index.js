import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import About from '../components/AboutUs.vue';
import SearchMangas from '../components/SearchMangas.vue'

// Define as rotas
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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;