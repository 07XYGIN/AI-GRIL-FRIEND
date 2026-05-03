import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './main.css';

const app = createApp(App);
const pinia = createPinia();

app.use(router)
   .use(pinia)
   .use(ElementPlus)
   .mount('#app');

// const { useUserStore } = await import('./store/user');
// const userStore = useUserStore();
// userStore.loadFromStorage();
