import { createApp } from 'vue'
import App from './App.vue'
import './assets/style/reset.css';
import './assets/style/main.css';
import 'primeicons/primeicons.css'
import router from './router';

const app = createApp(App);
app.use(router);
app.mount('#app');