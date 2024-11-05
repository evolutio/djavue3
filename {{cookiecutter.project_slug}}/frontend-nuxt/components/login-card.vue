<template>
    <v-form @keyup.enter="login(user.name, user.password)" class="login-card">
        <div class="d-flex my-4 justify-center align-center ga-2">
            <NuxtImg width="48px" max-width="48" src="/img/logo.svg"></NuxtImg>
            <span class="text-h6 text-primary font-weight-black">D-jà Vue</span>
        </div>

        <v-card class="mx-auto pa-8 pb-8 border-md" elevation="0" max-width="448" rounded="lg">
            <div class="text-subtitle-1 text-medium-emphasis">E-mail</div>

            <v-text-field v-model="user.name" density="compact" placeholder="Endereço de e-mail"
                prepend-inner-icon="mdi-email-outline" variant="outlined"></v-text-field>

            <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                Senha
                <NuxtLink class="text-caption text-decoration-none text-blue" to="/forgot-password"
                    rel="noopener noreferrer">
                    Esqueceu a senha?</NuxtLink>
            </div>

            <v-text-field v-model="user.password" :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                :type="visible ? 'text' : 'password'" density="compact" placeholder="Insira sua senha"
                prepend-inner-icon="mdi-lock-outline" variant="outlined"
                @click:append-inner="visible = !visible"></v-text-field>

            <v-btn is="submit" :loading="loading" @click="login(user.name, user.password)" class="mb-8" color="primary"
                size="large" variant="tonal" block>
                Entrar
            </v-btn>

            <v-card-text class="text-center w-100 justify-center d-flex ga-3">
                <NuxtLink class="text-blue text-decoration-none" to="/" rel="noopener noreferrer">
                    <v-icon icon="mdi-chevron-left"></v-icon> Voltar
                </NuxtLink>
                |
                <NuxtLink class="text-blue text-decoration-none" to="/sign-up" rel="noopener noreferrer">
                    Cadastrar <v-icon icon="mdi-chevron-right"></v-icon>
                </NuxtLink>
            </v-card-text>
        </v-card>
    </v-form>
</template>

<style scoped>
@media (width>=640px) {
    .login-card {
        width: 32rem;
    }
}

.login-card {
    min-width: 100%;
}
</style>

<script setup lang="ts">
const visible = ref(false)

const accountStore = useAccountStore()
const { login } = accountStore;
const { loading } = storeToRefs(accountStore)
const user = reactive({
    name: '',
    password: '',

})

</script>