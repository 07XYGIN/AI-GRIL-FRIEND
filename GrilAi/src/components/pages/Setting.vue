<script setup lang="ts">

import {
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
} from '@/components/ui/card'

import { Button } from '@/components/ui/button'
import { Separator } from '@/components/ui/separator'
import Theme from './theme.vue'
import {
    Select,
    SelectTrigger,
    SelectValue,
    SelectContent,
    SelectItem,
} from '@/components/ui/select'

import {
    Alert,
    AlertTitle,
    AlertDescription,
} from '@/components/ui/alert'

const languages = [
    { value: 'zh', label: '中文 (简体)' },
    //   { value: 'en', label: 'English (US)' },
    //   { value: 'jp', label: '日本語' },
]
</script>

<template>
    <!-- Header -->
    <header class="mb-10">
        <h1 class="text-3xl font-semibold tracking-tight">设置</h1>
        <p class="text-sm text-muted-foreground mt-1">
            管理您的账户偏好和安全选项
        </p>
    </header>

    <Card>
        <CardHeader>
            <CardTitle>偏好设置</CardTitle>
            <CardDescription>
                个性化您的界面和语言选项
            </CardDescription>
        </CardHeader>

        <CardContent class="space-y-6">
            <div class="flex items-center justify-between">
                <div>
                    <p class="text-sm font-medium">显示主题</p>
                    <p class="text-xs text-muted-foreground mt-1">
                        切换亮色或暗色模式
                    </p>
                </div>
                <Theme />

            </div>

            <Separator />

            <div class="flex items-center justify-between">
                <div>
                    <p class="text-sm font-medium">系统语言</p>
                    <p class="text-xs text-muted-foreground mt-1">
                        选择应用显示语言
                    </p>
                </div>

                <Select default-value="zh">
                    <SelectTrigger class="w-45">
                        <SelectValue placeholder="选择语言" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem v-for="lang in languages" :key="lang.value" :value="lang.value">
                            {{ lang.label }}
                        </SelectItem>
                    </SelectContent>
                </Select>
            </div>
        </CardContent>
    </Card>

    <div class="mt-12">
        <Alert variant="destructive">
            <AlertTitle>危险区域</AlertTitle>
            <AlertDescription class="mt-2">
                注销账号将永久删除您的所有对话记录、记忆偏好以及个人资料，
                此操作不可撤销，请谨慎操作。
            </AlertDescription>
            <div class="mt-6">
                <Button variant="destructive">
                    注销账号
                </Button>
            </div>
        </Alert>
    </div>
</template>
