<script setup lang="ts">
import { reactive, type HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import {
    Field,
    FieldGroup,
    FieldLabel,
    FieldDescription
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import type { loginForm } from "@/api/login"
import { login } from "@/api/login"
const props = defineProps<{
    class?: HTMLAttributes["class"]
}>()

const from = reactive<loginForm>({
    userName:undefined,
    password:undefined,
    code:undefined
})
const submit = async()=>{
    const res = await login(from)
    console.log(res);
}
</script>

<template>
    <div :class="cn('flex flex-col gap-6', props.class)">
        <Card class="login-card">
            <CardHeader class="text-center">
                <CardTitle class="text-xl">
                    Friend
                </CardTitle>
                <CardDescription>
                    register
                </CardDescription>
            </CardHeader>
            <CardContent>
                <form>
                    <FieldGroup>
                        <Field>
                            <FieldLabel for="checkout-7j9-card-name-43j">
                                <span class="text-foreground">用户名</span>
                            </FieldLabel>
                            <Input placeholder="请输入用户名" required v-model="from.userName"/>
                        </Field>
                        <Field>
                            <FieldLabel for="checkout-7j9-card-name-43j">
                                <span class="text-foreground">密码</span>
                            </FieldLabel>
                            <Input id="password" type="password" placeholder="请输入密码" required v-model="from.password"/>
                            <FieldDescription>
                                <span class="text-muted-foreground">
                                    请输入八位以上密码(不可以纯数字)
                                </span>
                            </FieldDescription>
                        </Field>
                        <Field>
                            <FieldLabel for="checkout-7j9-card-name-43j">
                                <span class="text-foreground">重复密码</span>
                            </FieldLabel>
                            <Input id="password" type="password" placeholder="请输入密码" required v-model="from.password"/>
                            <FieldDescription>
                                <span class="text-muted-foreground">
                                    请输入八位以上密码(不可以纯数字)
                                </span>
                            </FieldDescription>
                        </Field>
                        <Field>
                            <Button @click="submit">
                                注册
                            </Button>
                        </Field>
                    </FieldGroup>
                </form>
            </CardContent>
        </Card>
    </div>
</template>