<template>
    <div v-if="props.loading" class="grid grid-cols-4 gap-4">
        <template v-for="item in 10" :key="item">
            <Skeleton class="h-60 w-60" />
        </template>
    </div>
    <div v-else-if="props.memory&&props.memory.length === 0">
        <Empty>
            <EmptyHeader>
                <EmptyMedia variant="icon">
                    <FolderOpen />
                </EmptyMedia>
            </EmptyHeader>
            <EmptyTitle>目前还没有记忆呢</EmptyTitle>
        </Empty>
    </div>
    <div v-else class="grid grid-cols-4 gap-4">
        <div v-for="item in props.memory" :key="item.id" class="group">
            <Card class="transition-all duration-300 hover:shadow-lg hover:border-gray-400">
                <CardHeader class="flex justify-between items-center pb-2">
                    <Badge variant="secondary" class="text-xs">
                        {{ item.metadata.title }}
                    </Badge>
                    <span class="text-[10px] text-muted-foreground font-mono">
                        {{ item.metadata.create_time }}
                    </span>
                </CardHeader>

                <CardContent class="p-2 text-sm text-zinc-300 leading-relaxed line-clamp-4">
                    <span>{{ item.metadata.content }}</span>
                </CardContent>

                <CardFooter class="flex justify-end opacity-0 group-hover:opacity-100 transition-opacity duration-200">
                    <Button variant="ghost" size="sm" class="cursor-pointer" @click="delData(item.id)">
                        <Trash color="#ef4444" />
                    </Button>
                </CardFooter>
            </Card>
        </div>
    </div>
</template>

<script setup lang="ts">
import { Card, CardContent, CardHeader, CardFooter } from '@/components/ui/card'
import { Skeleton } from '../ui/skeleton';
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Trash } from 'lucide-vue-next';
import { FolderOpen } from 'lucide-vue-next'
import {
    Empty,
    EmptyHeader,
    EmptyMedia,
    EmptyTitle,
} from '@/components/ui/empty'
export interface MemoryMetadata {
    title: string
    content: string
    create_time: string
    timestamp: string
}

export interface MemoryDocument {
    id: string
    metadata: MemoryMetadata
    page_content: string
    type: 'Document'
}

const props = defineProps<{
    memory: MemoryDocument[]
    loading:boolean
}>()
const emit = defineEmits<{
    delData: [id: string]
}>()

const delData = (id: string) => {
    emit("delData", id)
}


</script>
