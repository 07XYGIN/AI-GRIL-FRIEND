<template>
  <div class="p-5">
    <Momery :memory="momeryList" :loading="loading" @del-data="defData"/>
  </div>
</template>

<script setup lang="ts">
import Momery from '@/components/pages/Momery.vue';
import { delSinglList, getMomeryList } from '@/api/msg';
import {ref,onMounted} from 'vue'
import useUserStore from '@/store/modules';
const getUserInfo = useUserStore();
const loading = ref<boolean>(false)
export interface MemoryMetadata {
    title: string
    content: string
    create_time: string
    timestamp:string
}

export interface MemoryDocument {
    id: string
    metadata: MemoryMetadata
    page_content: string
    type: 'Document'
}
const momeryList = ref<Array<MemoryDocument>>([])
const setMomery = async()=>{
  if(getUserInfo.userinfo.userId){
    try{
      loading.value = true
      const {data} = await getMomeryList({user_id:getUserInfo.userinfo.userId})
      momeryList.value = data
  }finally{
    loading.value = false
  }
}
}
const defData = async(id:string)=>{
  if(getUserInfo.userinfo.userId){
    try{
      await delSinglList(getUserInfo.userinfo.userId,id)
      await setMomery()
    }
    finally{
      loading.value = false
    }
  }
}

onMounted(
  async()=>{
    await getUserInfo.UserInfo();
    setMomery()
  }
)
</script>

<style lang="scss" scoped></style>
