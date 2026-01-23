<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Field,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
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
        <Input placeholder="请输入用户名" required />
      </Field>
      <Field>
        <div class="flex items-center">
          <FieldLabel for="password">
            密码
          </FieldLabel>
        </div>
        <Input id="password" type="password" required placeholder="请输入密码"/>
      </Field>
      <Field>
        <div class="flex items-center">
          <FieldLabel for="password">
            邀请码
          </FieldLabel>
        </div>
        <Input id="password" type="password" required placeholder="请输入邀请码"/>
      </Field>
      <Field>
        <Button type="submit">
          登录
        </Button>
      </Field>
    </FieldGroup>
  </form>
</template>
