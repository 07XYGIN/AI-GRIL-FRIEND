<template>
  <div class="w-full h-full flex flex-col px-16">
    <div class="flex-1">
      <div
        v-for="(item, index) in msgRes"
        :key="index"
        class="p-2"
        :class="item.type === 'human' ? 'text-right' : 'text-left'"
      >
        <div>
          {{ item.content }}
        </div>
      </div>
    </div>
    <div class="bottom-0 sticky z-10">
      <div class="bg-background mt-4">
        <div class="grid gap-6">
          <InputGroup>
            <InputGroupTextarea
              placeholder="给ARUA发送消息"
              v-model="msg"
              @keydown.enter.prevent="send"
            />
            <InputGroupAddon align="block-end">
              <InputGroupAddon align="block-start" />
                <InputGroupButton
                variant="default"
                class="rounded-full"
                size="icon-xs"
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
import { ref, onMounted } from 'vue';
import { getMsgList } from '@/api/msg';
import useUserStore from '@/store/modules';
import useSse from '@/utils/useSse';
const msg = ref<string>('');
const {connect,disconnect} = useSse('http://127.0.0.1:8000/send/sse/',{
onMessage: (data) => {
  const lastMsg = msgRes.value[msgRes.value.length - 1];
  // done时停止追加
  if(data === '[DONE]') return 

  if (lastMsg?.type === 'ai') {
    // 在新增的消息中追加data
    lastMsg.content += data;
  }else{
    // 如果最后一条不是aimessage就新增
    msgRes.value.push({ type: 'ai', content: data })
  }
  isSend.value = false
}
})
const getUserInfo = useUserStore();
const msgRes = ref<Array<{ type: string; content: string }>>([]);
const isSend = ref(false);
const send = async () => {  
  if (isSend.value) return
  isSend.value = true
  msgRes.value.push({type:"human",content:msg.value})
  await connect({
    body: JSON.stringify({
      message: msg.value,
      userId: getUserInfo.userinfo.userId
    })
  });
};
const getList = async () => {
  if (getUserInfo.userinfo.userId) {
    const { data } = await getMsgList(getUserInfo.userinfo.userId);
    msgRes.value = data;
  }
};
const cancel = ()=>{  
  console.log('cancel');
  isSend.value = false
  disconnect()
}
onMounted(async () => {
  await getUserInfo.UserInfo();
  getList();
});
</script>

<style lang="scss" scoped></style>
