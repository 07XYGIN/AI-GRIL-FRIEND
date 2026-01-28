<template>
  <div class="w-full h-full flex flex-col px-16">
    <div class="flex-1 overflow-auto" ref="msgContainer">
      <div v-for="(item, index) in msgRes" :key="index" class="p-2"
        :class="item.type === 'human' ? 'text-right' : 'text-left'">
        <div v-html="item.content" />
      </div>
    </div>
    <div class="bottom-0 sticky z-10">
      <div class="bg-background mt-4">
        <div class="grid gap-6">
          <InputGroup>
            <InputGroupTextarea placeholder="给Aura发送消息" v-model="msg" @keydown.enter.prevent="send" />
            <InputGroupAddon align="block-end">
              <InputGroupAddon align="block-start" />
              <InputGroupButton variant="default" class="rounded-full" size="icon-xs"
                @click="isSend ? cancel() : send()">
                <ArrowUpIcon v-if="!isSend" class="size-4" />
                <Loader v-else class="animate-spin size-4" stroke="red" />
              </InputGroupButton>

            </InputGroupAddon>
          </InputGroup>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ArrowUpIcon, Loader } from 'lucide-vue-next';
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupTextarea,
} from '@/components/ui/input-group';
import { ref, onMounted, nextTick, onUnmounted } from 'vue';
import hljs from 'highlight.js'
import MarkdownIt from 'markdown-it'
import mermaid from 'mermaid'
import { getMsgList } from '@/api/msg';
import useUserStore from '@/store/modules';
import 'highlight.js/styles/github-dark-dimmed.css';
import useSse from '@/utils/useSse';
const msg = ref<string>('');
const msgContainer = ref<HTMLDivElement | null>(null);
const { connect, disconnect } = useSse('http://127.0.0.1:8000/send/sse/', {
  onMessage: (data) => {
    if (data === '[DONE]') {
      // 所有数据接收完毕，开始渲染
      const lastMsg = msgRes.value[msgRes.value.length - 1];
      if (lastMsg?.type === 'ai') {
        // 只渲染一次
        lastMsg.content = md.value.render(lastMsg.content);
        console.log(lastMsg.content);
        
        // 初始化 mermaid
        nextTick(() => {
          mermaid.init(undefined, document.querySelectorAll('.mermaid:not([data-processed])'))
        });
      }
      isSend.value = false;
      scrollToBottom();
      return;
    }

    const lastMsg = msgRes.value[msgRes.value.length - 1];
    
    if (lastMsg?.type === 'ai') {
      // 直接追加原始文本，不渲染
      lastMsg.content += data;
    } else {
      // 新增 AI 消息，存储原始文本
      msgRes.value.push({ 
        type: 'ai', 
        content: data,
      })
    }
    
    // 实时滚动
    scrollToBottom()
  }
})
const getUserInfo = useUserStore();
const msgRes = ref<Array<{ type: string; content: string }>>([]);
const isSend = ref(false);
const send = async () => {
  if (isSend.value) return
  isSend.value = true
  msgRes.value.push({ type: "human", content: msg.value })
  await connect({
    body: JSON.stringify({
      message: msg.value,
      userId: getUserInfo.userinfo.userId
    })
  });
  msg.value = ''
  scrollToBottom()
};
const getList = async () => {
  if (getUserInfo.userinfo.userId) {
    const { data } = await getMsgList(getUserInfo.userinfo.userId);
    const endList = data.map(i=>{
      return ({
        ...i,
        content:md.value.render(i.content)
      })
    })
    
    msgRes.value = endList;
  }
};
const cancel = () => {
  console.log('cancel');
  isSend.value = false
  disconnect()
}
const scrollToBottom = async () => {
  if (msgContainer.value) {
    window.scrollTo({
      top: msgContainer.value.scrollHeight,
      behavior: 'smooth'
    });
  }
};
const md = ref(new MarkdownIt({
  highlight:(str,lang):string=>{
    if (lang === 'mermaid') {
      return `<div class="mermaid">${str}</div>`
    }
    const html = hljs.highlight(str,{language:lang}).value
    return html
  }
}))
onMounted(async () => {
  await hljs.highlightAll();
  await getUserInfo.UserInfo();
  await getList();
  await nextTick()
  mermaid.init(undefined, document.querySelectorAll('.mermaid'))
  scrollToBottom()
});
onUnmounted(() => {
  disconnect()
})
</script>

<style lang="scss" scoped></style>
