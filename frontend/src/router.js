import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage'
import DashboardPage from '@/components/DashboardPage'

const app = createApp(App);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardPage,
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

app.use(router);
app.mount('#app');
