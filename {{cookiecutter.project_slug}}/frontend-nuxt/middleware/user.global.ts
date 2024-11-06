export default defineNuxtRouteMiddleware(async (to, from) => {
    const account = useAccountStore()
    const { whoAmI } = account
    const { loggedUser } = storeToRefs(account)
    onNuxtReady(async () => {
        if (loggedUser.value === undefined) {
            await whoAmI()
        }
    })
});
