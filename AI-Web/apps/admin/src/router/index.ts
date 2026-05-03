import {createRouter, createWebHashHistory} from 'vue-router';


const routes = [
    {
        path: '/',
        component: import('@/pages/login/Login.vue'),
        name: 'login',
        meta: { requiresAuth: false },
    },
    {
        path: '/register',
        component: import('@/pages/register/Register.vue'),
        name: 'register',
        meta: { requiresAuth: false },
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});



export default router;
