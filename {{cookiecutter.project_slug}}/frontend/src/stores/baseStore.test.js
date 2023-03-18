// stores/counter.spec.ts
import { setActivePinia, createPinia } from "pinia"
import { describe, beforeEach, it, expect } from "vitest"
import { useBaseStore } from "@/stores/baseStore"

describe("Counter Store", () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it("Deve iniciar com sem mensagens", () => {
    const store = useBaseStore()
    expect(store.snackbarMessage).toBe(undefined)
    expect(store.showSnackbarMessage).toBe(false)
  })

  it("Deve mostrar mensagem ao chamar showSnackbar", () => {
    const store = useBaseStore()
    store.showSnackbar("Oi", "danger")
    expect(store.type).toBe("danger")
    expect(store.snackbarMessage).toBe("Oi")
    expect(store.showSnackbarMessage).toBe(true)
  })
})
