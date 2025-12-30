<template>
    <div class="w-full h-full flex flex-col justify-between">
        <div>
            消息列表
        </div>
        <div class="flex justify-center">
            <div class="grid w-full max-w-lg gap-6">
                <InputGroup>
                    <InputGroupTextarea placeholder="Ask, Search or Chat..." />
                    <InputGroupAddon align="block-end">
                        <InputGroupButton variant="outline" class="rounded-full" size="icon-xs">
                            <PlusIcon class="size-4" />
                        </InputGroupButton>
                        <DropdownMenu>
                            <DropdownMenuTrigger as-child>
                                <InputGroupButton variant="ghost">
                                    Auto
                                </InputGroupButton>
                            </DropdownMenuTrigger>
                        </DropdownMenu>
                        <InputGroupText class="ml-auto">
                        </InputGroupText>
                        <Separator orientation="vertical" />
                        <InputGroupButton variant="default" class="rounded-full" size="icon-xs">
                            <ArrowUpIcon class="size-4" />
                            <span class="sr-only">Send</span>
                        </InputGroupButton>
                    </InputGroupAddon>
                </InputGroup>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ArrowUpIcon,PlusIcon,} from 'lucide-vue-next'
import { DropdownMenu, DropdownMenuTrigger } from '@/components/ui/dropdown-menu'
import { InputGroup, InputGroupAddon, InputGroupButton, InputGroupText, InputGroupTextarea } from '@/components/ui/input-group'
import { Separator } from '@/components/ui/separator'
</script>

<style lang="scss" scoped></style>