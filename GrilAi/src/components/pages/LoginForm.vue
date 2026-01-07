<script setup lang="ts">
import { reactive, type HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import {
    Field,
    FieldDescription,
    FieldGroup,
    FieldLabel,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import type { loginForm } from "@/api/login"
import { login } from "@/api/login"
const from = reactive<loginForm>({
    userName: undefined,
    password: undefined,
    code: undefined
})
const loginSubmit = async()=>{
    await login(from)
}
const props = defineProps<{
    class?: HTMLAttributes["class"]
}>()
</script>

<template>
    <div :class="cn('flex flex-col gap-6', props.class)">
        <Card>
            <CardHeader class="text-center">
                <CardTitle class="text-xl">
                    Welcome
                </CardTitle>
            </CardHeader>
            <CardContent>
                <form>
                    <FieldGroup>
                        <Field>
                            <FieldLabel for="email">
                                用户名
                            </FieldLabel>
                            <Input placeholder="用户名" required v-model="from.userName"/>
                        </Field>
                        <Field>
                            <div class="flex items-center">
                                <FieldLabel for="password">
                                    密码
                                </FieldLabel>
                            </div>
                            <Input id="password" type="password" required placeholder="请输入密码"  v-model="from.password"/>
                        </Field>
                        <Field>
                            <div class="flex items-center">
                                <FieldLabel for="password">
                                    邀请码
                                </FieldLabel>
                            </div>
                            <Input id="password" type="password" required placeholder="请输入邀请码" v-model="from.code"/>
                        </Field>
                        <Field>
                            <Button @click="loginSubmit">
                                登录
                            </Button>
                            <FieldDescription class="text-center">
                                没有账号?去
                                <router-link to="/register">注册</router-link>
                            </FieldDescription>
                        </Field>
                    </FieldGroup>
                </form>
            </CardContent>
        </Card>
    </div>
</template>
