# 🕸️ API MOCK

## Por que?

Mudar o comportamento do backend (DA API DO BACKEND) é muito mais fácil
em um imitador de backend (api mock) do que no real backend.

Desta forma, a camada de API MOCK serve para agilizar o desenvolvimento
do frontend sem se preocupar com o backend.


## Como utilizar

Basta ATIVAR a api mock ao invés bater no backend verdadeiro utilizando
a variável de mabiente `VITE_API_MOCK=true`.

Desta forma, o mirageJS vai fazer a mágina e interceptar as chamadas ao
backend e responder o que quisermos utilizando código JS.
O mais legal é que a camada API (api client) vai ser chamada normalmente
e permitindo um teste muito perto do real.

## Como está organizado

routes    -> tem as rotas imitando o backend
fixtures  -> podemos ter JSON fixos para simular uma tabela (model) do banco de dados
factories -> serve para gerar dados (models) de forma aleatória (faker)
