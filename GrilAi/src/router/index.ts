import { createRouter, createWebHashHistory } from 'vue-router'

const Chat = () => import('@/pages/chat.vue')
const routes = [
    { path: '/', component: Chat,name:'chat' },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router