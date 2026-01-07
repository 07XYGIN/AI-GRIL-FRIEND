import { createRouter, createWebHashHistory } from 'vue-router'

const SidebarLayout = () => import('@/components/pages/sidebar.vue')
const Chat   = () => import('@/pages/chat.vue')
const Memory = () => import('@/pages/Memory.vue')
const register  = () => import("@/pages/register.vue")
const login  = () => import("@/pages/Login.vue")
const routes = [
    {
        path: '/',
        component: SidebarLayout,
        children: [
            {
                path: '',
                component: Chat,
                name: 'chat',
            },
            {
                path: 'memory',
                component: Memory,
                name: 'Memory',
            }
        ]
    },
    {
        path: '/register',
        component: register,
        name: 'register',
    },
    {
        path: '/login',
        component: login,
        name: 'login',
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router