# 🗂️ Organização de pastas e projeto

## Organização das camadas (🦄 Backend)

```
                                           ___ Models 
                                          /
 Cliente -->   API      --> Services --> ORM
             urls+views                   \___ Manager
             Schemas        Regras

```

- **Cliente**: Qualquer coisa que faz chamadas HTTP para a API
- **API**: Tem as definições de rotas e validação dos dados de entrada, sem ou pouca regras de negócio, redireciona os dados para a camada de serviço
- **Services**: Módulos python puro com a implementação das regras de negócio, é a camada que mais deve ser testada
- **ORM**: Mapeamento dos dados na base de dados


## Estrutura de pastas (🦄 Backend)

Visao geral

```shell
twitterclone                       👉 Pasta raiz do projeto
 ├── README.md
 ├── manage.py                     👉 Django CLI (Ponto de entrada)
 ├── requirements.txt              👉 Dependencias principais
 ├── requirements-dev.txt          👉 Dependencias locais (pode mudar no modo Poetry)
 ├── docker-compose.yml            👉 Descritor docker para rodar local
 ├── Dockerfile                    👉 Receita para rodar projeto
 ├── tox.ini
 ├── uwsgi.ini
 └── twitterclone                  👉 base do projeto
    ├── base                       👉 app para regras fora do "core"
    │   └── ...
    ├── accounts                   👉 app relacionado a usuarios e autenticacao
    │   └── ...
    ├── core                       👉 app principal com o "core business" 
    │   └── ...
    └── twitterclone               👉 centraliza configuracoes do projeto
        ├── api.py
        ├── settings.py            👉 Configuracoes principal do Django
        ├── urls.py                👉 Configuracao principal/inicial das rotas no Django
        └── wsgi.py
```

O Django tem o conceito de "apps" com a ideia de separar os contextos do seu projeto, ao invés de ter tudo na app principal, podemos ir criando novas apps como por exemplo, vendas, compras, estoque, relatórios, blog de forma a agrupar funcionalidades da mesma natureza. Cada app segue a estrutura abaixo: 

```
   urls --> views --> service --> models
   1) Rotas           2) Regras   3) Banco
```

```shell
├── core                       👉 Raiz da django app para centralizar uma solução de um dado contexto
│   ├── apps.py                👉 Como um __init__ da app
│   ├── urls.py                👉 1) Definição das rotas (com django-ninja a urls fica vazia)
│   ├── views.py               👉 1) Implementação das rotas
│   ├── schemas.py             👉 1) Definição dos atributos nome/tipo 
│   ├── service                👉 2) Implementação das regras de negócio
│   ├── models.py              👉 3) Definição das tabelas para salvar os dados
│   ├── migrations             👉 3) Histórico de como criar/alterar as tabelas no banco de dados
│   ├── admin.py               👉 Configuração dos dados que podemos acessar via back-office
│   ├── tests                  👉 Centraliza os testes da app
│   └── templates              👉 Não utilizado nas apps de API, mas pode gerar páginas HTML

```
