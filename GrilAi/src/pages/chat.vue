<template>
    <div class="w-full h-full flex flex-col justify-between px-16 relative">
        <div class="">
            <div v-for="(item, index) in response.data" :key="index" class="p-2"
                :class="item.role === 'user' ? 'text-right' : 'text-left'">
                <div
                    :class="item.role === 'user' ? 'inline-block  text-foreground rounded-lg p-2' : 'inline-block  text-foreground rounded-lg p-2'">
                    {{ item.content }}
                </div>
            </div>
            <div class="bg-black w-7xl fixed bottom-0">
                <div class="grid gap-6">
                    <InputGroup>
                        <InputGroupTextarea placeholder="输入内容开始聊天......" v-model="msg" />
                        <InputGroupAddon align="block-end">
                            <InputGroupButton variant="outline" class="rounded-full" size="icon-xs">
                                <PlusIcon class="size-4" />
                            </InputGroupButton>
                            <DropdownMenu>
                                <DropdownMenuTrigger as-child>
                                    <InputGroupButton variant="ghost">
                                        Auto
                                    </InputGroupButton>
                                </DropdownMenuTrigger>
                            </DropdownMenu>
                            <InputGroupText class="ml-auto">
                            </InputGroupText>
                            <Separator orientation="vertical" />
                            <InputGroupButton variant="default" class="rounded-full" size="icon-xs" @click="send"
                                @click.enter="send">
                                <ArrowUpIcon class="size-4" />
                                <span class="sr-only">Send</span>
                            </InputGroupButton>
                        </InputGroupAddon>
                    </InputGroup>
                </div>
            </div>
        </div>
        </div>
</template>

<script setup lang="ts">
import { ArrowUpIcon, PlusIcon, } from 'lucide-vue-next'
import { DropdownMenu, DropdownMenuTrigger } from '@/components/ui/dropdown-menu'
import { InputGroup, InputGroupAddon, InputGroupButton, InputGroupText, InputGroupTextarea } from '@/components/ui/input-group'
import { Separator } from '@/components/ui/separator'
import { ref } from 'vue'
const msg = ref<string>("")
const response = ref({
    code: 200,
    msg: "OK",
    data: [
        {
            role: "user",
            content: "Hello, how are you?"
        },
        {
            role: "assistant",
            content: "I'm fine, thank you! How can I assist you today?"
        },
        {
            role: "user",
            content: "I'm fine, thank you! How can I assist you today?"
        },
        
    ]
})

const send = () => {
    if (!msg.value) return
    response.value.data.push({
        role: "user",
        content: msg.value
    })
    msg.value = ""
}
</script>

<style lang="scss" scoped></style>