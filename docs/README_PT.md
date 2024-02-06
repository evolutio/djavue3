# D-Jà Vue - README Português 🇧🇷 

## 💡 Introdução

### Por quê?

A ideia é sermos mais produtivos, desta forma um fluxo de trabalho e uma estrutura de projeto 
facilitam na elaboração dos passos iniciais. Sabemos que vamos errar. portanto vamos torná-los baratos.

### O que é D-Jà Vue?

D-Jà Vue é um **modelo de projeto** que criará uma estrutura de pastas e arquivos que contém dois projetos:

      - 🦄 **Django API backend** 
      - 🍰 **VueJS + Vuetify frontend**

Pode ser um ótimo pontapé inicial para o seu próximo projeto (na Prova de Conceito ou ideia de produto).
Está pronto para produção, onde você pode se concentrar nos recursos, no core business e gerar valor.

### Como fazer?

Simples, basta responder algumas perguntas. Assim você pode dar o nome ao projeto, e escolher coisas como a versão do banco de dados, o modelo principal para o seu projeto e algumas outras coisas. Ao finalisar uma estrutura completa do projeto será criada 📂! 
Então podemos pensar no principal que são as regras de negócio do projeto.


### Alguns possibilidades

- Iniciar criando o frontend sem ter o backend
- Testar as hipóteses, atraves de outputs (saídas)... 
- Deploy com antecedência e com mais frequência
- TDD facilita e diminui o tempo de entrega
- Para maiores informações [aqui](https://github.com/evolutio/djavue#contributing):

### Que saber mais?

- 💬 [**Alguma pergunta?**](https://github.com/evolutio/djavue3/discussions)
- 🐞 [**Encontrou um falha?**](https://github.com/evolutio/djavue3/issues)
- 🏆 [**Voce gostaria de contribuir?**](https://github.com/evolutio/djavue3/issues)
- 🌟 **Voce gostou?** [Considere a star in the github repo](https://github.com/evolutio/

## 🛠️ D-Jà Vue - requisitos necessários

Para criar seu projeto usando Djavue, voce precisa somente:
- 🐍 Python +3.10
- 🍪 Cookiecutter +1.7

Para executar (criação do projeto), voce pode escolher duas maneiras 🍨:
- usar Docker 🐋: **Docker** e **Docker compose**
- não usar Docker 📦: **Python** para o backend e **Node JS** para o frontend

## 📦 Criação do primeiro projeto usando D-Jà Vue

Primeiro, faça download do [cookiecutter](https://github.com/cookiecutter/cookiecutter/). E instale via pip.

```
pip install "cookiecutter>=1.7.0"
```

::: tip
🌈 DICAS/TRUQUES: Você pode usar [pipx ](https://pypa.github.io/pipx/) para instalar cookiecutter globalmente or criar via pyenv um ambiente virtual para isolar seu projeto. 
Com ambiente virtual voce proteger o python que esta rodando e seu sistema operacional.
:::

Com o cookiecutter instalado, você pode executá-lo informando o link do djavue. Será solicitado alguns valores, os quais voce deverá responder segundo os critérios do seu projeto. Fique tranquilo que longo explicaremos!...

::: info
👉 Atenção: se você não estiver usando Docker e quiser usar a mesma versão do Python que esta rodando na sua máquina, use `python -V` para verificar a versão corrente do python. A mesma coisa voce pode verificar com a versão do NodeJS como o comando `node --version`.
:::

```
cookiecutter https://github.com/evolutio/djavue3
```

Responda as perguntas segundo os critérios e necessidades do seu projeto. Acompanhe:

```shell
❯ cookiecutter https://github.com/evolutio/djavue3
  [1/27] project_name (My Todo List): <nome-projeto>
  [2/27] project_slug (<nome-projeto>): 
  [3/27] description (The Ultimate Django and Vue Template): <faça um descrição do seu projeto>
  [4/27] app_name (core): <app_name será criada com nome=core>
  [5/27] model (Tasks): <nome do modelo dentro da app core>
  [6/27] model_lower (tasks): 
  [7/27] model_singular (Task): 
  [8/27] model_singular_lower (task): 
  [9/27] Select python_version
    1 - 3.9
    2 - 3.10
    3 - 3.11
    Choose from [1/2/3] (1): <escolha a versão do python. Default=1>
  [10/27] Select package_manager
    1 - requirements.txt
    2 - pip-tools
    3 - poetry
    Choose from [1/2/3] (1): <escolha o gerenciador de versão. Default=1)
  [11/27] Select python_linter
    1 - flake8
    2 - pylint
    3 - ruff
    Choose from [1/2/3] (1): <escolha o linter para o projeto. Default=1)
  [12/27] Select django_api
    1 - 🦄 django_only
    2 - 🥷 django_ninja
    3 - 📄 openapi
    Choose from [1/2/3] (1): <escolha o Django para o projeto. Default=1>
  [13/27] Select database_version
    1 - postgres:15-alpine
    2 - postgres:14-alpine
    3 - postgres:13.3-alpine
    4 - postgis/postgis:14-3.2-alpine
    Choose from [1/2/3/4] (1): <escolha a versão do Postgres. Default=1>
  [14/27] use_sqlite_local_env (no): 
      <escolha se vai usar sqlite local. Default=No>
  [15/27] Select node_version
    1 - 18.18
    2 - 16.17
    3 - 14.14
    Choose from [1/2/3] (1): <escolha a versão do Node. Default=1>
  [16/27] Select pages_folder_name
    1 - views
    2 - pages
    Choose from [1/2] (1): <escolha o nome diretório - no Frontend. Default=1>
  [17/27] Select api_mock
    1 - mirageJS
    2 - express
    Choose from [1/2] (1): <escolha api_mock - no Frontend. Default=1>
  [18/27] use_github_actions_CI (yes): <use github_actions_integração continua. Default=yes>
  [19/27] keep_vscode_settings (yes): <aceite vscode_settings. Default=yes>
  [20/27] keep_vscode_devcontainer (no):<aceite vscode_devcontainer.Default=no>
  [21/27] Select docker_usage
    1 - 🐳 use docker by default
    2 - 📦 use venv npm by default
    Choose from [1/2] (1): <selecione se vai usar Docker. Default=1>
  [22/27] Select deploy_to
    1 - None
    2 - fly.io
    Choose from [1/2] (1): <selecione se vai Deploy. Default=1>
  [23/27] deploy_domain (nome-projeto.fly.dev): <Deploy no fly. Verifique se o domain esta livre>
  [24/27] author_name (Roger Camargo): <Inserir o nome do autor>
  [25/27] email (roger-camargo@example.com): <Inserir o email do autor>
  [26/27] version (0.1.0): 
  [27/27] Select license
    1 - MIT
    2 - agpl-3.0
    Choose from [1/2] (1): <selecione a licença. Default=1>
 
 [SUCCESS]: 🐍 Sua API Backend Django está criada! (root) ✨ 🍰 ✨
 [SUCCESS]: 🍰 Dua Vue 3 frontend está criada! (frontend folder) ✨ 🍰 ✨

O que fazer depois?
  Entrar no diretório do projeto. (cd <nome-projeto>)
  👉 Usuários DOCKER 🐳
       docker compose build
       docker compose up
       no brwoser -> http://localhost (porta não é necessário)
  👉 Usando virtualenv 📦
       Criar o ambiente virtual
       instalar as dependências
 
  📄 Para maiores informações
       https://djavue3.vercel.app

```

**Concluído!! 🎉🎉** A estrutura do seu projeto esta criado! Voce pode verificar o diretório 
`nome-projeto` e verificar as pastas.

**Qual o proximo passo?** O proximo passo e rodar seu projeto localmente e ter certeza que tudo esta funcionando! Depois voce pode começar a trabalhar na proxima facilidade do seu produto ou implementar uma nova ideia !✨

Basicamente, existe duas maneiras para rodar seu projeto. No passo 21 `Select docker_usage` podemos responder que será usado Docker ou não! Portanto durante o setup do projeto fazemos esta escolha. 🐋

Continue lendo para entender a diferença!

::: warning
⚠️ A estrututa do projeto **"nome-projeto"** em termos da interface de usuário, ainda esta longe do que deveria ser. Queremos deixar claro inicialmente que o projeto criado é uma simples API CRUD web (Backend e frontend).

:::

## 🐋 Diferença entre executar localmente com Docker, ou sem usar Docker (containers)
::: warning 🚧 TODO

Estamos traduzindo!
:::
## 📦 Executando o 🦄 backend sem usar Docker
::: warning 🚧 TODO

Estamos traduzindo!
:::
## 📦 Executando o ⚡️ frontend sem usar Docker
::: warning 🚧 TODO

Estamos traduzindo!
:::

## 🐞 Depurando a API do Django

::: danger 🚧 TODO

Voce pode ajudar!
:::

## 🐞 Depurando a web do VueJS

::: danger 🚧 TODO

Voce pode ajudar!
:::

## 🐋 Executar todo com Docker
::: warning 🚧 TODO

Estamos traduzindo!
:::

## 📦 Como fazer o gerenciamento do projeto com REQUIREMENTS

::: danger 🚧 TODO

Voce pode ajudar!
:::

## 📦 Como fazer o gerenciamento do projeto com Poetry
::: warning 🚧 TODO

Estamos traduzindo!
:::

## 📦 Como fazer o gerenciamento do projeto com Pip-tools

::: danger 🚧 TODO

Voce pode ajudar!
:::

## 📂 Estrutura & organização do Backend
::: danger 🚧 TODO

Voce pode ajudar!
:::

## 📂 Estrutura & organização do Frontend

::: danger 🚧 TODO

Voce pode ajudar!
:::

## 🤡 Usar API MOCK no Frontend

::: danger 🚧 TODO

Voce pode ajudar!
:::

## 🚀 Fluxo de trabalho para criação-(Build), Integração Continua-(CI) e implementação-(Deploy) 

::: danger 🚧 TODO

Voce pode ajudar!
:::

## ✨ Contibuições

::: danger 🚧 TODO

Voce pode ajudar!
:::

'
