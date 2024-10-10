# 💿 Iniciando

## 🛠️ D-Jà Vue - Requisitos necessários

Para criar seu projeto usando Djavue, você precisa somente de:
- 🐍 Python +3.10
- 🍪 Cookiecutter +1.7

Para executar (criação do projeto), você pode escolher duas maneiras 🍨:
- usar Docker 🐋: **Docker** e **Docker compose**
- não usar Docker 📦: **Python** para o backend e **Node JS** para o frontend

## 📦 Criação do primeiro projeto usando D-Jà Vue

Primeiro, faça download do [cookiecutter](https://github.com/cookiecutter/cookiecutter/). E instale via pip.

```
pip install "cookiecutter>=1.7.0"
```

::: tip
🌈 DICAS/TRUQUES: Você pode usar [pipx ](https://pypa.github.io/pipx/) para instalar cookiecutter globalmente or criar via pyenv um ambiente virtual para isolar seu projeto. 
Com ambiente virtual você protegerá o python que está rodando e seu sistema operacional.
:::

Com o cookiecutter instalado, você pode executá-lo informando o link do djavue. Será solicitado alguns valores, os quais você deverá responder segundo os critérios do seu projeto. Fique tranquilo que logo explicaremos!...

::: info
👉 Atenção: se você não estiver usando Docker e quiser usar a mesma versão do Python que está rodando na sua máquina, use `python -V` para verificar a versão corrente do python. A mesma coisa você pode verificar com a versão do NodeJS como o comando `node --version`.
:::

```
cookiecutter https://github.com/evolutio/djavue3
```

Responda as perguntas segundo os critérios e necessidades do seu projeto. Acompanhe:

```shell
❯ cookiecutter https://github.com/evolutio/djavue3
  [1/27] project_name (My Todo List): Twitter Clone
  [2/27] project_slug (twitterclone): 
  [3/27] description (The Ultimate Django and Vue Template): My first Djavue template
  [4/27] app_name (core): posts
  [5/27] model (Tasks): Tweets
  [6/27] model_lower (tweets): 
  [7/27] model_singular (Tweet): 
  [8/27] model_singular_lower (tweet): 
  [9/27] Select python_version
    1 - 3.9
    2 - 3.10
    3 - 3.11
    Choose from [1/2/3] (1): 2
  [10/27] Select package_manager
    1 - requirements.txt
    2 - poetry
    Choose from [1/2] (1): 1
  [11/27] Select python_linter
    1 - flake8
    2 - pylint
    3 - ruff
    Choose from [1/2/3] (1): 
  [12/27] Select django_api
    1 - 🦄 django_only
    2 - 🥷 django_ninja
    Choose from [1/2/3] (1): 2
  [13/27] Select database_version
    1 - postgres:15-alpine
    2 - postgres:14-alpine
    3 - postgres:13.3-alpine
    4 - postgis/postgis:14-3.2-alpine
    Choose from [1/2/3/4] (1): 
  [14/27] use_sqlite_local_env (no): yes
  [15/27] Select node_version
    1 - 18.18
    2 - 16.17
    3 - 14.14
    Choose from [1/2/3] (1): 2
  [16/27] Select pages_folder_name
    1 - views
    2 - pages
    Choose from [1/2] (1): 2
  [17/27] Select api_mock
    1 - mirageJS
    2 - express
    Choose from [1/2] (1): 
  [18/27] use_github_actions_CI (yes): 
  [19/27] keep_vscode_settings (yes): 
  [20/27] keep_vscode_devcontainer (no): 
  [21/27] Select docker_usage
    1 - 🐳 use docker by default
    2 - 📦 use venv npm by default
    Choose from [1/2] (1): 2
  [22/27] Select deploy_to
    1 - None
    2 - fly.io
    Choose from [1/2] (1): 
  [23/27] deploy_domain (twitterclone.fly.dev): 
  [24/27] author_name (Roger Camargo): 
  [25/27] email (roger-camargo@example.com): 
  [26/27] version (0.1.0): 
 
 [SUCCESS]: 🐍 Your Django API backend is created! (root) ✨ 🍰 ✨
 [SUCCESS]: 🍰 Your Vue 3 frontend is created! (frontend folder) ✨ 🍰 ✨

What's next?
  cd twitterclone
  👉 For DOCKER users 🐳
       docker compose build
       docker compose up
       go to http://localhost  (PORT is NOT necessary)
  👉 Using virtualenv 📦
       create a virtualenv
       install dependencies
 
  📄 for more information
       https://djavue3.vercel.app

```

**Concluído!! 🎉🎉** A estrutura do seu projeto está criada! você pode verificar o diretório 
`twitterclone` e verificar as pastas.

**Qual o próximo passo?** O próximo passo e rodar seu projeto localmente e ter certeza que tudo está funcionando! Depois você pode começar a trabalhar na próxima facilidade do seu produto ou implementar uma nova ideia !✨

Basicamente, existe duas maneiras para rodar seu projeto. No passo `21 - Select docker_usage` podemos responder que será usado Docker ou não! Portanto, durante o setup do projeto fazemos esta escolha. 🐋

Continue lendo para entender a diferença!

::: warning
⚠️ A estrutura do projeto **"twitterclone"** em termos da interface de usuário, ainda esta longe do que deveria ser. Queremos deixar claro inicialmente que o projeto criado é uma simples API CRUD web (Backend e frontend).

:::

## 🐋 Diferença entre executar localmente com Docker, ou sem Docker (containers)

Quando usamos containers (docker) temos um modo seguro de criar um ambiente similar ao ambiente de produção com a vantagem de instalar somente uma dependência local em nossa máquina que é o docker.
Sem dúvida a melhor forma para rodar o nosso projeto localmente (container) trazendo uma ótima experiência ao desenvolvedor.


::: info
Usando 🐋 Docker podemos criar projetos com muitas dependências internas(libs, frameworks e também dependências do SO) e por outro lado, externamente: temos conexões com banco de dados, servidor de email, gerenciador de fila, etc e rodamos tudo isto com somente um CLICK. É muito comum desenvolvedores trabalharem com múltiplos projetos, e cada um usando diferentes versões de Python ou banco de dados.
Pense no pesadelo que seria manipular esta matriz de possibilidades!!! O conceito de contanier está aqui para ajudar, ou melhor, nos salvar. 
:::

![local-env-with-docker](./images/local-env-using-docker.jpg)

Usando o modelo DJavue, seu projeto terá o conceito de container a partir da instalação. É bom lembrar que você pode iniciar seu projeto sem usar Docker, mas o Djavue esáa pronto para executar com docker (que é uma ótima possibilidade), principalmente para melhorar a operação de desenvolvimento. (ou na implentação para produção )

📦 **Executar sem usar docker** poder ser muito útil também, é mais fácil para fazer debug, entretanto, é necessário criar um ambiente virtual, instalar todas as dependências tanto para o backend como para o frontend e também algumas configurações extras para possibilitar o acesso entre frontend e backend (CORS settings). A ciação do ambiente virtual vai depender do desenvolvedor usar as ferramentas (NVM ou PYENV) para fazer que a máquina local trabalhe com a mesma versão do python que o servidor de produção usará. 

![local-env-without-docker](./images/local-env-without-docker.jpg)

O melhor é que o modelo `D-Jà Vue` está usando uma boa base para tornar a experiência do desenvolvedor a melhor possível, mesmo o desenvolvedor escolhendo um ambiente sem atrito (sem docker), ou por exemplo, executando um banco de dados SQLITE localmente ou ainda qualquer versão disponível de python or misturando com serviço de banco Postgres dentro de um container, é claro, estará mais próximo possível do que será executado em produção. Por exemplo, ter um servidor web ou qualquer outro serviço externo que o projeto possa ser integrado.