export default defineNuxtRouteMiddleware(async (to, from) => {
  const account = useAccountStore()
  const { loggedUser } = storeToRefs(account)

  setTimeout(() => {
    onNuxtReady(() => {
      if (loggedUser.value) {
        return navigateTo('/home')
      }
    })
  }, 400)
});
