# 📦 STORES

## Por que?

Utilizamos [Pinia](https://pinia.vuejs.org/getting-started.html) para
manter o estado entre componentes (É um VUEX mais fácil e organizado)

Exemplo: Na página de Login obtemos o usuário do backend, mas este
usuário é utilizado no cabeçalho, rodapé e várias outras páginas
e poderia também em outros componentes visuais.

A solução é ter o estado salvo e Pinia é fundamental e padrão para esta
finalidade.

```

PAGES  <-------------\
                      \
                       ------>   PINIA
                      /
COMPONENTES <--------/

```

## Como utilizar

Em qualquer componente podemos consultar um estado com:

```JavaScript
// script
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),  // 👈
  },

// Template
<app-footer :user="loggedUser" />
```

Em qualquer componente podemos alterar um estado com:

```JavaScript
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  setup() {
    const accountsStore = useAccountsStore()
    return { accountsStore }
  },
  methods: {
    async login() {
      await this.accountsStore.login('user', 'abc') // 👈
    },
```

## Como está organizado

No pinia a ideia é organizar os estados por módulos, por exemplo, compra, vendas, contas etc ao invés de colocar tudo no stores/index.js

E basicamente, precisamos:
- #1 dos estados para serem consultados via computed
- #2 das actions para modificar os estados

```JavaScript

import { defineStore } from "pinia"

export const useAccountsStore = defineStore("accountsStore", {
  state: () => ({              // 👈 #1
    loggedUser: null,
  }),
  actions: {                   // 👈 #2
    async login(username, password) {
      // Faz alguma coisa
      this.loggedUser = 'NOVO VALOR'
    },
```