<script setup lang="ts">
import type { HTMLAttributes } from "vue"
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
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"

const props = defineProps<{
    class?: HTMLAttributes["class"]
}>()
</script>

<template>
    <div :class="cn('flex flex-col gap-6', props.class) ">
        <Card class="login-card">
            <CardHeader class="text-center">
                <CardTitle class="text-xl">
                    Friend
                </CardTitle>
                <CardDescription>
                    login
                </CardDescription>
            </CardHeader>
            <CardContent>
                <form>
                    <FieldGroup>
                        <Field>
                            <Input placeholder="用户名" required />
                        </Field>
                        <Field>
                            <Input id="password" type="password" placeholder="密码" required />
                        </Field>
                        <Field>
                            <Input placeholder="测试码" required />
                        </Field>
                        <Field>
                            <Button class="">
                                Login
                            </Button>
                        </Field>
                    </FieldGroup>
                </form>
            </CardContent>
        </Card>
    </div>
</template>