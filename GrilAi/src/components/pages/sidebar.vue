<script setup lang="ts">
import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupContent,
    SidebarHeader,
    SidebarInset,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarProvider,
    SidebarRail,
    SidebarTrigger,
} from '@/components/ui/sidebar'
import Theme from './theme.vue';
</script>

<template>
    <SidebarProvider>
        <Sidebar>
            <SidebarHeader>
                <SidebarMenu>
                    <SidebarMenuItem>
                        <SidebarMenuButton size="lg">
                            <div
                                class="flex aspect-square size-8 items-center justify-center rounded-lg text-sidebar-primary-foreground">
                            </div>
                            <div class="flex flex-1 text-left text-sm leading-tight justify-between items-center">
                                <span class="truncate font-semibold">Gin friend</span>
                            </div>
                        </SidebarMenuButton>
                    </SidebarMenuItem>
                </SidebarMenu>
            </SidebarHeader>
            <SidebarContent>
                <SidebarGroup>
                    <SidebarGroupContent>
                        <SidebarMenu>
                            <SidebarMenuItem>
                                <SidebarMenuButton as-child>
                                    <router-link to="/">
                                        <span>Home</span>
                                    </router-link>
                                </SidebarMenuButton>
                                <SidebarMenuButton as-child>
                                    <router-link to="/memory">
                                        <span>memory</span>
                                    </router-link>
                                </SidebarMenuButton>
                            </SidebarMenuItem>
                        </SidebarMenu>
                    </SidebarGroupContent>
                </SidebarGroup>
            </SidebarContent>
            <SidebarFooter />
            <SidebarRail />
        </Sidebar>
        <SidebarInset>
            <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear sticky top-0 bg-background z-10 ">
                <div class="flex items-center gap-2 px-4">
                    <SidebarTrigger class="-ml-1" />
                    <Theme />
                </div>
            </header>
            <main class="h-full">
                <router-view></router-view>
            </main>
        </SidebarInset>
    </SidebarProvider>
</template>
