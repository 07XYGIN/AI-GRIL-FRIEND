<template>
    <div class="w-full h-full flex flex-col justify-between px-16">
        <div ref="messagesContainer">
            <div v-for="(item, index) in msgRes" :key="index" class="p-2"
                :class="item.role === 'user' ? 'text-right' : 'text-left'">
                <div
                    :class="item.role === 'user' ? 'inline-block  text-foreground rounded-lg p-2' : 'inline-block  text-foreground rounded-lg p-2'">
                    {{ item.content }}
                </div>
            </div>
            <div class="bg-background sticky bottom-0">
                <div class="grid gap-6">
                    <InputGroup>
                        <InputGroupTextarea placeholder="输入内容开始聊天......" v-model="msg" @keydown.enter.prevent="send"/>
                        <InputGroupAddon align="block-end">
                            <!-- <InputGroupButton variant="outline" class="rounded-full" size="icon-xs">
                                <PlusIcon class="size-4" />
                            </InputGroupButton> -->
                            <DropdownMenu>
                                <!-- <DropdownMenuTrigger as-child>
                                    <InputGroupButton variant="ghost">
                                        Auto
                                    </InputGroupButton>
                                </DropdownMenuTrigger> -->
                            </DropdownMenu>
                            <InputGroupText class="ml-auto">
                            </InputGroupText>
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
import { ArrowUpIcon,Loader } from 'lucide-vue-next'
import { DropdownMenu} from '@/components/ui/dropdown-menu'
import { InputGroup, InputGroupAddon, InputGroupButton, InputGroupText, InputGroupTextarea } from '@/components/ui/input-group'
import { Separator } from '@/components/ui/separator'
import { ref } from 'vue'
import {sendMsg} from '@/api/msg'

const msg = ref<string>("")
const msgRes = ref<Array<{role:string,content:string}>>([])
const isSend = ref(false)


const send = async() => {
    isSend.value = true
    setTimeout(
        ()=>isSend.value = false,3000
    )
}
</script>

<style lang="scss" scoped></style>