<template>
  <div class="w-full h-full flex flex-col px-16">
    <div class="flex-1 overflow-auto" ref="msgContainer">
      <div v-for="(item, index) in msgRes" :key="index" class="p-2"
        :class="item.type === 'human' ? 'text-right' : 'text-left'">
        <div>
          {{ item.content }}
        </div>
      </div>
    </div>
    <div class="bottom-0 sticky z-10">
      <div class="bg-background mt-4">
        <div class="grid gap-6">
          <InputGroup>
            <InputGroupTextarea placeholder="给Aura发送消息" v-model="msg" @keydown.enter.prevent="send" />
            <InputGroupAddon align="block-end">
              <InputGroupButton variant="ghost">
                <PlusIcon class="size-4" />
                <Input id="picture" type="file" multiple @change="handleSubmit"/>
              </InputGroupButton>
              <InputGroupText class="ml-auto"></InputGroupText>
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
import { ArrowUpIcon, Loader, PlusIcon } from 'lucide-vue-next';
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupTextarea,
} from '@/components/ui/input-group';
import { ref, onMounted } from 'vue';
import { flieUpLoad, getMsgList } from '@/api/msg';
import useUserStore from '@/store/modules';
import useSse from '@/utils/useSse';
const msg = ref<string>('');
const msgContainer = ref<HTMLDivElement | null>(null);
const { connect, disconnect } = useSse('http://127.0.0.1:8000/send/sse/', {
  onMessage: (data) => {
    const lastMsg = msgRes.value[msgRes.value.length - 1];
    // done时停止追加
    if (data === '[DONE]') return

    if (lastMsg?.type === 'ai') {
      // 在新增的消息中追加data
      lastMsg.content += data;
    } else {
      // 如果最后一条不是aimessage就新增
      msgRes.value.push({ type: 'ai', content: data })
    }
    isSend.value = false
    scrollToBottom()
  }
})
const getUserInfo = useUserStore();
const msgRes = ref<Array<{ type: string; content: string }>>([]);
const isSend = ref(false);
const formData = ref(new FormData())
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
    msgRes.value = data;
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
const handleSubmit = async(e:any)=>{
  console.log(e.target.files[0]);
  const formData = new FormData();
  formData.append('file', e.target.files[0]);
  await flieUpLoad(formData).then((res)=>{
    console.log(res);
  })
}
onMounted(async () => {
  await getUserInfo.UserInfo();
  await getList();
  scrollToBottom()
});
</script>

<style lang="scss" scoped></style>
