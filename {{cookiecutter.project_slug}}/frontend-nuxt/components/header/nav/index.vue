<template>
    <nav :class="compClass">
        <template v-for="item in items">
            <HeaderNavButton :key="item.href" :href="item.href" v-if="item.show && route.path != item.href" divider>
                {%raw%}{{ item.title }}{%endraw%}
            </HeaderNavButton>
        </template>
        <DevOnly>
            <HeaderNavButton href="https://www.djavue.org/01-o-que-eh.html" divider>Documentação
            </HeaderNavButton>
        </DevOnly>
    </nav>
</template>

<script setup lang="ts">
import type { NavItem } from '../index.vue';

const { direction } = defineProps<{
    direction: 'vertical' | 'horizontal',
    items: NavItem[]
}>()

const compClass = computed(() => {
    if (direction === 'horizontal') {
        return "d-none d-md-flex align-center ga-3"
    } else if (direction === 'vertical') {
        return "d-flex align-start flex-column"
    } return ''
})

const route = useRoute()
</script>