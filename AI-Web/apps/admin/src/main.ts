import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store/store';
import { useUserStore } from './store/modules/user';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './main.css';

const app = createApp(App);
const userStore = useUserStore(store);

userStore.loadToken();

app.use(router)
   .use(store)
   .use(ElementPlus)
   .mount('#app');
