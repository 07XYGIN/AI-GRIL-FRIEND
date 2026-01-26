<script setup lang="ts">
import { reactive, type HTMLAttributes } from 'vue';
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Field,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field"
import { useRouter } from 'vue-router';

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
import { Input } from '@/components/ui/input';
import type { loginForm } from '@/api/login';
import { login } from '@/api/login';
import useUserStore from '@/store/modules';
const user = useUserStore();
const router = useRouter();
const from = reactive<loginForm>({
  userName: undefined,
  password: undefined,
  code: undefined,
});

const loginSubmit = async () => {
  const { data } = await login(from);
  user.setCode(data);
  router.push('/');
};
</script>

<template>
  <form :class="cn('flex flex-col gap-6', props.class)">
    <FieldGroup>
      <div class="flex flex-col items-center gap-1 text-center">
        <h1 class="text-2xl">
          欢迎访问
        </h1>
        <p class="text-muted-foreground text-sm text-balance">
          请输入凭证验证身份
        </p>
      </div>
      <Field>
        <FieldLabel for="email">
          用户名
        </FieldLabel>
        <Input placeholder="用户名" required v-model="from.userName" />
      </Field>
      <Field>
        <div class="flex items-center">
          <FieldLabel for="password">
            密码
          </FieldLabel>
        </div>
        <Input
                id="password"
                type="password"
                required
                placeholder="请输入密码"
                v-model="from.password"
              />
      </Field>
      <Field>
        <div class="flex items-center">
          <FieldLabel for="password">
            邀请码
          </FieldLabel>
        </div>
        <Input
                id="password"
                type="password"
                required
                placeholder="请输入邀请码"
                v-model="from.code"
              />
      </Field>
      <Field>
        <Button @click="loginSubmit"> 登录 </Button>
      </Field>
    </FieldGroup>
  </form>
</template>
