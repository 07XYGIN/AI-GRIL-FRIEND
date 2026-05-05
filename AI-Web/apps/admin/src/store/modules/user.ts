import { defineStore } from 'pinia'
import { ref } from 'vue'
import {getUserInfo} from "@/api/user.ts";

export const useUserStore = defineStore('user', () => {
  const token = ref<string>('')

  const userInfo = ref()

  const getUser = async()=>{
    const res = await getUserInfo()
    userInfo.value = res.data
  }

  const setToken = (newToken: string) => {
    token.value = newToken
    localStorage.setItem('token', newToken)
  }

  const loadToken = () => {
    const storedToken = localStorage.getItem('token')
    if (storedToken) {
      token.value = storedToken
    }
  }

  const clearToken = () => {
    token.value = ''
    localStorage.removeItem('token')
  }

  return {
    token,
    userInfo,
    getUser,
    setToken,
    loadToken,
    clearToken
  }
})
