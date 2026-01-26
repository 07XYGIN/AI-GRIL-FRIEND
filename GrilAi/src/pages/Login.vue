<script lang="ts">
export const description = 'A two column login page with a cover image.'
</script>

<script setup lang="ts">
import LoginForm from '@/components/pages/LoginForm.vue'
import { Motion } from 'motion-v'
</script>

<template>
  <div class="grid min-h-svh lg:grid-cols-2">
    <div class="bg-muted relative hidden lg:block overflow-hidden">
      <div class="flex h-full justify-center items-center">
        <Motion
          tag="div"
          class="relative z-10 flex flex-col items-center gap-8"
          :initial="{ opacity: 0, scale: 0.96 }"
          :animate="{ opacity: 1, scale: 1 }"
          :transition="{ duration: 1.2 }"
        >
          <div class="relative group cursor-default">
            <Motion
              tag="div"
              class="absolute inset-0 rounded-full border border-white/20 scale-150 opacity-30"
              :animate="{ rotate: 360, x: [0, 2, 0], y: [0, -2, 0] }"
              :transition="{ duration: 12, repeat: Infinity }"
            />

            <Motion
              tag="div"
              class="absolute inset-0 rounded-full border border-white/10 scale-[1.8] opacity-20"
              :animate="{ rotate: -360, x: [0, -2, 0], y: [0, 2, 0] }"
              :transition="{ duration: 18, repeat: Infinity }"
            />

            <Motion
              tag="div"
              class="w-32 h-32 rounded-full border border-white/30
                     flex items-center justify-center
                     bg-black backdrop-blur-sm Aura-glow relative"
              :animate="{
                boxShadow: [
                  '0 0 25px rgba(255,255,255,0.25)',
                  '0 0 45px rgba(255,255,255,0.45)',
                  '0 0 25px rgba(255,255,255,0.25)'
                ]
              }"
              :transition="{ duration: 4, repeat: Infinity}"
              while-hover="{ scale: 1.05 }"
            >
              <div class="relative">
                <Motion
                  tag="div"
                  class="w-3 h-3 bg-white rounded-full shadow-[0_0_25px_white]"
                  :animate="{ scale: [1, 1.6, 0.9, 1], opacity: [0.9, 1, 0.8, 0.9] }"
                  :transition="{ duration: 2.2, repeat: Infinity }"
                />
                <Motion
                  tag="div"
                  class="absolute inset-0 rounded-full border border-white/40"
                  :animate="{ scale: [1, 3], opacity: [0.6, 0] }"
                  :transition="{ duration: 2.5, repeat: Infinity}"
                />
              </div>
            </Motion>
          </div>

          <Motion
            tag="div"
            class="text-center space-y-3"
            :initial="{ opacity: 0, y: 12 }"
            :animate="{ opacity: 1, y: 0 }"
          >
            <h1 class="text-5xl font-bold tracking-[0.2em] ml-3">Aura</h1>
            <p class="text-gray-500 tracking-widest text-sm font-light">
              Virtual AI Assistant
              <span class="mx-2 opacity-30">|</span>
              虚拟 AI 助手
            </p>
          </Motion>
        </Motion>
      </div>
    </div>

    <div class="flex flex-col gap-4 p-6 md:p-10">
      <div class="flex flex-1 items-center justify-center">
        <Motion
  tag="div"
  class="relative w-full max-w-xs p-6 rounded-2xl bg-black/60 backdrop-blur-md overflow-hidden"
  :initial="{ opacity: 0, y: 16 }"
  :animate="{ opacity: 1, y: 0 }"
  :transition="{ delay: 0.3, duration: 0.9 }"
  style="border: 1px solid rgba(255,255,255,0.06);"
>
  <div class="relative z-10">
    <LoginForm />
  </div>
</Motion>
      </div>
    </div>
  </div>
</template>
