<template>
    <v-app-bar is="header" scroll-threshold="32" scroll-behavior="hide" class="px-md-12" elevation="0"
        color="#cccccc50">
        <div>
            <v-toolbar-title @click="navigateTo('/')" class="mx-4 cursor-pointer font-weight-black text-primary">
                D-jà Vue
            </v-toolbar-title>
        </div>
        <v-spacer></v-spacer>
        <HeaderNav :items="items" direction="horizontal" />
        <div class="mx-md-3">
            <DarkModeSwitch />
        </div>
        <v-app-bar-nav-icon class="d-flex d-md-none" variant="text" @click.stop="drawer = !drawer" />
    </v-app-bar>
    <ClientOnly>
        <v-navigation-drawer class="pa-4" v-model="drawer" location="right" temporary>
            <HeaderNav :items="items" direction="vertical" />
        </v-navigation-drawer>
    </ClientOnly>
</template>


<script setup lang="ts">
export type NavItem = {
    title: string,
    href: string,
    show: boolean
}
const drawer = ref(false)
const accountStore = useAccountStore()
const { loggedUser } = storeToRefs(accountStore)


const items = computed<NavItem[]>(() => [
    {
        title: 'Início',
        href: '/',
        show: !loggedUser.value,
    },
    {
        title: 'Cadastrar',
        href: '/sign-up',
        show: !loggedUser.value
    },
    {
        title: 'Entrar',
        href: '/login',
        show: !loggedUser.value
    },
    {
        title: 'Home',
        href: '/home',
        show: !!loggedUser.value
    },
    {
        title: 'Sair',
        href: '/logout',
        show: !!loggedUser.value
    },
])
</script>