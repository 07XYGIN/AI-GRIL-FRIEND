<template>
  <div class="login-container flex justify-center items-center h-screen bg-gradient-to-br from-blue-400 to-purple-600">
    <div class="login-card bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
      <h2 class="text-2xl font-bold text-center mb-6 text-gray-800">登录</h2>
      <el-form :model="form" label-width="auto" @submit.prevent="onSubmit" ref="formRef">
        <el-form-item label="用户名" prop="username" :rules="[{ required: true, message: '请输入用户名' }]">
          <el-input v-model="form.username" placeholder="请输入用户名" />
        </el-form-item>
        <el-form-item label="密码" prop="password" :rules="[{ required: true, message: '请输入密码' }]">
          <el-input v-model="form.password" type="password" placeholder="请输入密码" />
        </el-form-item>
        <el-form-item label="年龄">
          <el-input-number v-model="form.age" :min="1" :max="120" placeholder="请输入年龄" />
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="form.gender">
            <el-radio value="male">男</el-radio>
            <el-radio value="female">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="form.email" type="email" placeholder="请输入邮箱" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit" class="w-full" @click="Login">登录</el-button>
        </el-form-item>
      </el-form>
      <p class="text-center mt-4 text-gray-600">
        没有账号? <span @click="goToRegister" class="text-blue-500 cursor-pointer hover:underline">去注册</span>
      </p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import type { FormInstance } from 'element-plus'
import {login} from "@/api/user";

interface LoginForm {
  username: string
  password: string
  age: number
  gender: string
  email: string
}

const form = reactive<LoginForm>({
  username: '',
  password: '',
  age: 0,
  gender: '',
  email: ''
})

const formRef = ref<FormInstance>()
const router = useRouter()

const onSubmit = async () => {
  if (!formRef.value) return
  const valid = await formRef.value.validate().catch(() => false)
  if (valid) {
    console.log('登录成功:', form)
    login(form).then(() => {

    })
  }
}

const goToRegister = () => {
  router.push('/register')
}
</script>

<style scoped>
.login-container {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-card {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}
</style>
