<script lang="ts">
export const description = "A login page with a muted background color."
</script>

<script setup lang="ts">
import LoginForm from "@/components/pages/register.vue"
</script>

<template>
    <div class="bg-muted flex min-h-svh flex-col items-center justify-center gap-6 p-6 md:p-10">
        <div class="flex w-full max-w-sm flex-col gap-6 ">
            <LoginForm />
        </div>
    </div>
</template>
