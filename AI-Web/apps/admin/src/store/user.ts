import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
  const token = ref<string>('')

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
    setToken,
    loadToken,
    clearToken
  }
})
