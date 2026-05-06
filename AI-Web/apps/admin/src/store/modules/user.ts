import { defineStore } from 'pinia'
import { ref } from 'vue'
import {getUserInfo} from "@/api/user.ts";
import type { UserInfo } from '@/type/user'

const EMPTY_USER_INFO: UserInfo = {
  username: '',
  password: '',
  age: 1,
  sex: 0,
  email: '',
}

const USER_INFO_STORAGE_KEY = 'userInfo'

export const useUserStore = defineStore('user', () => {
  const token = ref<string>('')

  const userInfo = ref<UserInfo>({ ...EMPTY_USER_INFO })

  const loadLocalUserInfo = () => {
    const storedUserInfo = localStorage.getItem(USER_INFO_STORAGE_KEY)
    if (!storedUserInfo) return null

    try {
      return JSON.parse(storedUserInfo) as Partial<UserInfo>
    } catch {
      localStorage.removeItem(USER_INFO_STORAGE_KEY)
      return null
    }
  }

  const getUser = async()=>{
    const res = await getUserInfo()
    const localUserInfo = loadLocalUserInfo()
    userInfo.value = {
      ...EMPTY_USER_INFO,
      ...res.data,
      ...localUserInfo,
    }
  }

  const updateUserInfo = (newUserInfo: UserInfo) => {
    userInfo.value = { ...newUserInfo }
    localStorage.setItem(USER_INFO_STORAGE_KEY, JSON.stringify(userInfo.value))
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
    userInfo.value = { ...EMPTY_USER_INFO }
    localStorage.removeItem('token')
    localStorage.removeItem(USER_INFO_STORAGE_KEY)
  }

  return {
    token,
    userInfo,
    getUser,
    updateUserInfo,
    setToken,
    loadToken,
    clearToken
  }
})
