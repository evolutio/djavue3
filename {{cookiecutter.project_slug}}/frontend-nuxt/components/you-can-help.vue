<template>
    <div class="d-flex justify-center w-100 text-center">
        <v-card style="max-width: 600px;" class="ma-4 pa-4" elevation="2">
            <v-card-title class="font-weight-bold text-primary headline text-center">
                Esta tela ainda não está pronta...
            </v-card-title>
            <v-card-text>
                <p>
                    Mas você pode nos ajudar com seu Pull Request! 
                </p>
                <p class="mt-6 text-h4">😃</p>
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn color="primary" @click="handleHelpClick">
                    Saiba mais
                </v-btn>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script setup>
function handleHelpClick() {
    window.open('https://github.com/evolutio/djavue3/issues', '_blank')
}
</script>