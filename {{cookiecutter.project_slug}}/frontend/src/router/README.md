# ➡️ ROUTES

## Por que?

É o início da jornada do requisição do visitante do site, por exemplo,
o caminho (path) '/' (raiz) irá redirecionar para a Página `HomeView`
e está defina no arquivo base.routes.js

```
/                  👉 pages/base/HomeView
/getstarted        👉 pages/base/GetStartedView
/accounts/login    👉 pages/accounts/LoginView
...
```

## Como utilizar

Basta criar novas Páginas dentro da pasta pages/views e criar uma rota
apontando para a nova página

## Como está organizado

De forma modular como todo o resto, desta forma as rotas estão organizadas em contextos como compra, venda, contas etc...