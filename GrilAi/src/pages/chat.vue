<template>
    <div class="w-full h-full flex flex-col px-16 ">
        <div class="flex-1">
            <div v-for="(item, index) in msgRes" :key="index" class="p-2"
                :class="item.type === 'human' ? 'text-right' : 'text-left'">
                <div
                    :class="item.type === 'user' ? 'inline-block  text-foreground rounded-lg p-2' : 'inline-block  text-foreground rounded-lg p-2'">
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
                            <InputGroupText class="ml-auto" />
                            <InputGroupAddon align="block-start">
                            </InputGroupAddon>
                            <Separator orientation="vertical" />
                            <template v-if="!isSend">
                                <InputGroupButton variant="default" class="rounded-full" size="icon-xs" @click="send">
                                    <ArrowUpIcon class="size-4" />
                                </InputGroupButton>
                            </template>
                            <template v-else>
                                <InputGroupButton variant="default" class="rounded-full" size="icon-xs">
                                    <Loader stroke="red" class="animate-spin size-4" />
                                </InputGroupButton>
                            </template>
                        </InputGroupAddon>
                    </InputGroup>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ArrowUpIcon, Loader } from 'lucide-vue-next'
import { InputGroup, InputGroupAddon, InputGroupButton, InputGroupText, InputGroupTextarea } from '@/components/ui/input-group'
import { Separator } from '@/components/ui/separator'
import { ref, onMounted } from 'vue'
import { getMsgList } from '@/api/msg'
const msg = ref<string>("")
const msgRes = ref<Array<{ type: string, content: string }>>([])
const isSend = ref(false)
const wsUrl = ref('ws://localhost:8000/ws')
const ws = ref(new WebSocket(wsUrl.value))
const send = async () => {
    isSend.value = true
    ws.value.send(msg.value)
    ws.value.onmessage = (e: MessageEvent) => {
        console.log(e.data);
        msgRes.value.push(
            { type: "human", content: msg.value },
            { type: "ai", content: e.data },
        )
        isSend.value = false
        msg.value = ''
    }
}
const getList = async () => {
    const { data } = await getMsgList()
    msgRes.value = data

}
onMounted(() => {
    getList()
})
</script>

<style lang="scss" scoped></style>