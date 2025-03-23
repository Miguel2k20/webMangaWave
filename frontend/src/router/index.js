import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import About from '../components/AboutUs.vue';

// Define as rotas
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about-us',
    name: 'Sobre Nós',
    component: About
  }
];

// Cria a instância do roteador
const router = createRouter({
  history: createWebHistory(), // Usa o modo HTML5 History
  routes
});

export default router;