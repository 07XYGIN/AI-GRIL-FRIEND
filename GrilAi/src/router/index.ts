import { createRouter, createWebHashHistory } from 'vue-router'

const Chat = () => import('@/pages/chat.vue')
const Memory = () => import('@/pages/Memory.vue')
const routes = [
    { 
        path: '/', component: Chat,name:'chat',
    },
    {
        path: '/Memory', component: Memory ,name:'Memory' 
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router