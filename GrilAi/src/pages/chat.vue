<template>
    <div class="w-full h-full flex flex-col px-16 ">
        <div class="flex-1">
            <div v-for="(item, index) in msgRes" :key="index" class="p-2"
                :class="item.type === 'human' ? 'text-right' : 'text-left'">
                <div>
                    {{ item.content }}
                </div>
            </div>
        </div>
        <div class="bottom-0 sticky z-10">
            <div class="bg-background mt-4 ">
                <div class="grid gap-6">
                    <InputGroup>
                        <InputGroupTextarea placeholder="输入内容开始聊天......" v-model="msg" @keydown.enter.prevent="send" />
                        <InputGroupAddon align="block-end">
                            <InputGroupAddon align="block-start" />
                            <InputGroupButton variant="default" class="rounded-full" size="icon-xs" @click="send">
                                <template v-if="!isSend">
                                    <ArrowUpIcon class="size-4" />
                                </template>
                                <template v-else>
                                    <Loader stroke="red" class="animate-spin size-4" />
                                </template>
                            </InputGroupButton>

                        </InputGroupAddon>
                    </InputGroup>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ArrowUpIcon, Loader } from 'lucide-vue-next'
import { InputGroup, InputGroupAddon, InputGroupButton, InputGroupTextarea } from '@/components/ui/input-group'
import { ref, onMounted, watch } from 'vue'
import { getMsgList } from '@/api/msg'
import useWebSocket from '@/utils/useWebSoct'
import useUserStore from '@/store/modules'
const getUserInfo = useUserStore()
const msg = ref<string>("")
const msgRes = ref<Array<{ type: string, content: string }>>([])
const isSend = ref(false)
const wsUrl = ref(`ws://localhost:8000/ws/${getUserInfo.userinfo.userId}`)

const { sendMsg, messages } = useWebSocket(wsUrl.value)
watch(messages, (v) => {
    msgRes.value.push(
        { type: "ai", content: v },
    )
    isSend.value = false
})
const send = async () => {
    if(msg.value === '') return
    sendMsg(msg.value)
    msgRes.value.push({ type: "human", content: msg.value })
    msg.value = ''
    isSend.value = true
}
const getList = async () => {
    if(getUserInfo.userinfo.userId){
        const { data } = await getMsgList(getUserInfo.userinfo.userId)
        msgRes.value = data
    }
}
onMounted(async() => {
    await getUserInfo.UserInfo()
    getList()
})
</script>

<style lang="scss" scoped></style>