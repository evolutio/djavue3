# D-Jà Vue - README Português 🇧🇷 

## 💡 Introdução

### Por quê?

A ideia é sermos mais produtivos, desta forma um fluxo de trabalho e uma estrutura de projeto 
facilitam na elaboração dos passos iniciais. Sabemos que vamos errar, portanto vamos torná-los baratos.

### O que é D-Jà Vue?

D-Jà Vue é um **modelo de projeto** que criará uma estrutura de pastas e arquivos que contém dois projetos: um  **Django API backend** e outro **VueJS + Vuetify frontend**.
Pode ser um ótimo pontapé inicial para o seu próximo projeto (na Prova de Conceito ou ideia de produto).
Está pronto para produção, onde você pode se concentrar nos recursos, no core business e gerar valor.

### Como fazer?

Simples, basta responder algumas perguntas. Assim você pode dar o nome ao projeto, e escolher coisas como a versão do banco de dados, o modelo principal para o seu projeto e algumas outras coisas. Ao finalizar uma estrutura completa do projeto será criada 📂! 
Então podemos pensar no principal que são as regras de negócio do projeto.


### Alguns possibilidades

- Iniciar criando o frontend sem ter o backend
- Testar as hipóteses, através de outputs (saídas)... 
- Deploy com antecedência e com mais frequência
- TDD facilita e diminui o tempo de entrega
- Para maiores informações [aqui](https://github.com/evolutio/djavue#contributing):

### Que saber mais?

- 💬 [**Alguma pergunta?**](https://github.com/evolutio/djavue3/discussions)
- 🐞 [**Encontrou uma falha?**](https://github.com/evolutio/djavue3/issues)
- 🏆 [**Você gostaria de contribuir?**](https://github.com/evolutio/djavue3/issues)
- 🌟 **Você gostou?** [Considere a star in the github repo](https://github.com/evolutio/)

## 🛠️ D-Jà Vue - requisitos necessários

Para criar seu projeto usando Djavue, você precisa somente:
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
    Choose from [1/2/3] (1): <Escolha a versão do python. Default=1>
  [10/27] Select package_manager
    1 - requirements.txt
    2 - pip-tools
    3 - poetry
    Choose from [1/2/3] (1): <Escolha o gerenciador de versão. Default=1)
  [11/27] Select python_linter
    1 - flake8
    2 - pylint
    3 - ruff
    Choose from [1/2/3] (1): <Escolha o linter para o projeto. Default=1)
  [12/27] Select django_api
    1 - 🦄 django_only
    2 - 🥷 django_ninja
    3 - 📄 openapi
    Choose from [1/2/3] (1): <Escolha o Django para o projeto. Default=1>
  [13/27] Select database_version
    1 - postgres:15-alpine
    2 - postgres:14-alpine
    3 - postgres:13.3-alpine
    4 - postgis/postgis:14-3.2-alpine
    Choose from [1/2/3/4] (1): <Escolha a versão do Postgres. Default=1>
  [14/27] use_sqlite_local_env (no): 
      <escolha se vai usar sqlite local. Default=No>
  [15/27] Select node_version
    1 - 18.18
    2 - 16.17
    3 - 14.14
    Choose from [1/2/3] (1): <Escolha a versão do Node. Default=1>
  [16/27] Select pages_folder_name
    1 - views
    2 - pages
    Choose from [1/2] (1): <Escolha o nome diretório - no Frontend. Default=1>
  [17/27] Select api_mock
    1 - mirageJS
    2 - express
    Choose from [1/2] (1): <Escolha api_mock - no Frontend. Default=1>
  [18/27] use_github_actions_CI (yes): <use github_actions_integração continua. Default=yes>
  [19/27] keep_vscode_settings (yes): <mantenha vscode_settings. Default=yes>
  [20/27] keep_vscode_devcontainer (no):<mantenha vscode_devcontainer.Default=no>
  [21/27] Select docker_usage
    1 - 🐳 use docker by default
    2 - 📦 use venv npm by default
    Choose from [1/2] (1): <Selecione se vai usar Docker. Default=1>
  [22/27] Select deploy_to
    1 - None
    2 - fly.io
    Choose from [1/2] (1): <Selecione se vai Deploy. Default=1>
  [23/27] deploy_domain (nome-projeto.fly.dev): <Deploy no fly. Verifique se o domain esta livre>
  [24/27] author_name (Roger Camargo): <Inserir o nome do autor>
  [25/27] email (roger-camargo@example.com): <Inserir o email do autor>
  [26/27] version (0.1.0): 
  [27/27] Select license
    1 - MIT
    2 - agpl-3.0
    Choose from [1/2] (1): <Selecione a licença. Default=1>
 
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

**Concluído!! 🎉🎉** A estrutura do seu projeto está criada! você pode verificar o diretório 
`nome-projeto` e verificar as pastas.

**Qual o próximo passo?** O próximo passo e rodar seu projeto localmente e ter certeza que tudo está funcionando! Depois você pode começar a trabalhar na próxima facilidade do seu produto ou implementar uma nova ideia !✨

Basicamente, existe duas maneiras para rodar seu projeto. No passo 21 `Select docker_usage` podemos responder que será usado Docker ou não! Portanto, durante o setup do projeto fazemos esta escolha. 🐋

Continue lendo para entender a diferença!

::: warning
⚠️ A estrutura do projeto **"nome-projeto"** em termos da interface de usuário, ainda esta longe do que deveria ser. Queremos deixar claro inicialmente que o projeto criado é uma simples API CRUD web (Backend e frontend).

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


## 📦 Executando o 🦄 backend sem usar Docker

**Requesitos:**
- Git
- Python +3.9  (para o backend)
- Node JS +14 (para o frontend - em uma etapa seguinte)
- um terminal shell (por ser um terminal linux, um terminal WSL no Windows ou um PowerShell), ⚠️ PowerShell pode ocorrer algumas diferenças nos comandos

::: tip
Você pode usar qualquer versão do Python, contudo, o ideal seria usar localmente a mesma versão do Python que será usada no ambiente de produção. Por este motivo, você pode escolher a versão de Python na instalação. 💡 No arquivo `Dockerfile` é possível verificar a versão de Python que será utilizado no ambiente de produção (inclusive é possível alterar se necessário).


::: code-group

```dockerfile [Dockerfile]
FROM python:3.10-slim
...

```
🌈 DICAS/TRUQUES: Você pode instalar um versão específica de Python para a sua máquina ou usar uma ferramenta como [Pyenv](https://github.com/pyenv/pyenv) ou [asdf](https://github.com/asdf-vm/asdf) para instalar/manusear múltiplas versões de Python uma para cada projeto que você possa trabalhar.

:::

O projeto **nome-projeto** foi criado anteriormente, e para dar continuidade é necessário entrar dentro do diretório do projeto. Veja ...

```shell
cd nome-projeto/
```

Na sequência vamos criar um ambiente virtual Python para o backend e instalar as dependências: 

::: warning
⚠️ **Não esqueça de ativar** o ambiente (`source .venv/bin/activate`), caso você esqueça de ativar as dependências serão instaladas na sua máquina fora do ambiente virtual do seu projeto.

:::

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Com o ambiente virtual Python pronto, você pode usar o comando `pip freeze` e verificar se todas as dependências python foram instaladas. Outro ponto importante a ser feito neste momento é executar um formatador de código (`lint`) para garantir que todo o código está correto. 

```shell
black nome-projeto/
```
::: info
👉 Lembre-se que o nome `nome-projeto/` pode ser diferente baseado no que na resposta que você deu ao nome do projeto (`nome-projeto`)

:::
Agora está na hora de rodar as migrações, ou melhor, criar as tabelas iniciais dentro do banco de dados (baseado no aquivo models). Basicamente os modelos que o Django têm, tais como, **Users**, **Sessions** e também o modelo inicial do nosso projeto, no nosso caso a tabela **Tweets**. O comando `migrate` do Django irá ler todas as migrações e criar as tabelas correspondentes. 

::: info
Para este projeto, o banco de dados padrão é o SQLITE caso tenhamos respondido `yes` e também `2` para as seguintes opções:

```shell{2,6}
  ...
  [14/27] use_sqlite_local_env (no): yes
  ...
  [21/27] Select docker_usage
    1 - 🐳 use docker by default
    2 - 📦 use venv npm by default
    Choose from [1/2] (1): 2
  ...
```
👉 Caso precise alterar para o banco Postgres, não esqueça que não será necessário recriar todo o projeto novamente, será necessário apenas mudar o arquivo `.env`
:::

Rodar as migrações para todas as apps Django:

```shell
./manage.py migrate
```
E rapidamente teremos nossa base de dados criada, então podemos criar um novo usuário:

```shell
./manage.py createsuperuser
Usuário: admin
Endereço de email: admin@example.br
Password: ********** 
Password (again): **********
Superuser created successfully.
```
Finalmente podemos rodar o projeto localmente:

```shell
./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 17, 2023 - 08:39:10
Django version 4.1.7, using settings 'dashboardtarget.dashboardtarget.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
👉 abra seu browser e acesse a url `http://localhost:8000`, a aplicação deve estar em execução

![local-env-without-docker-localhost-8000](./images/local-run-without-docker-localhost-8000.jpg)

**Outra coisa que você pode fazer neste momento:**
- acessar a url `http://localhost:8000/admin` e depois de logar (usando o usuário que criamos antes) abrir o Administrador do Django
- executar o comando `pytest` para passar todos os testes criados no backend
- executar o comando `./manage.py shell_plus --ipython --print-sql` e executar codigos, tais como:
  - `Tweet.objects.all()` ou 
  - `Tweet.objects.create(description="My first post using djavue")`

::: info
👉 Lembre o nome `Tasks` no código `Tasks.objects.all()` é o nome do modelo que você escolheu ou pode ser diferente no seu caso. Caso tenha escolhido outro nome.

:::

- Acesse a url `http://localhost:8000/api/docs` e verifique a documentação da API
- Acesse a url `http://localhost:8000/api/posts/tweets/list` e obtenha a lista de tweets criadas na API de backend
::: info
👉 Novamente os nomes `posts` e `tweets` podem ser diferentes baseado nas suas respostas para app_name and model_name

:::
::: info
👉  Se você obter a receber a mensagem:
`{"detail": "Unauthorized"}` quando acessar a url `http://localhost:8000/api/posts/tweets/list`, você pode acessar a url `http://localhost:8000/admin/login/`  e logar usando o usuário que você criou com o comando `createsuperuser` e fazer uma nova tentativa.
:::


## 📦 Executando o ⚡️ frontend sem usar Docker

**Requisitos:**
- Git
- Node JS +14 (para o frontend)
- um terminal shell (por ser um terminal linux, um terminal WSL no Windows ou um PowerShell), ⚠️ PowerShell pode ocorrer algumas diferenças nos comandos
- O backend em execução

Abra um segundo terminal (no primeiro deverá estar rodando o backend). Navegue dentro do diretório do projeto e na pasta do frontend. 

```shell
cd nome-projeto/frontend
```

Use o `npm` para instalar todas as dependências do frontend. Observe que as dependências estão listadas dentro do arquivo `package.json`. Observe também que o ambiente deste projeto, comparado com o diretório .venv que foi criado para armazenar todas as dependências do backend, para projetos de frontend, este diretório é `node_modules` e não precisamos criar ou informar qualquer coisa. Por default este diretório será criado depois de executarmos o seguinte comando.

```shell
npm install 
```
Agora vamos executar o frontend usando vite

```shell
npm run dev
  VITE v4.4.11  ready in 669 ms
  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help

```

**FEITO!! 🎉🎉** O frontend está rodando

👉 Abra seu browser e acesse a url `http://localhost:3000` (ou o ip de sua máquina + a porta se estiver com --host) para solicitar o aplicativo frontend!
Deveria estar rodando agora.

![local-env-without-docker-localhost-3000](./images/local-run-without-docker-localhost-3000.jpg)

::: info
📱 O template D-Jà Vue tem como objetivo ser 'MOBILE FIRST', ou seja, funcionar bem em dispositivos movéis.
:::

::: tip

🌈 DICAS/TRUQUES: Como uma alternativa podemos usar o comando `npm run dev -- --host`
que disponibilizará o aplicativo para sua rede, desta maneira você pode usar o endereço ip da sua máquina para acessar o aplicativo de qualquer máquina ou telefone celular dentro da mesma rede de WIFI.
:::

::: tip
você pode usar qualquer versão do Node JS, contudo, o ideal seria usar localmente a mesma versão do Node JS que será usada no ambiente de produção. Por este motivo, você pode escolher a versão na instalação. 💡 No arquivo `frontend/Dockerfile` é possível verificar a versão de produção (inclusive é possível alterar se necessário).


::: code-group

```dockerfile [frontend/Dockerfile]
FROM node:16.17-slim
...

```

🌈 DICAS/TRUQUES: você pode instalar um versão específica do node em sua máquina ou usar uma ferramenta como [NVM](https://github.com/nvm-sh/nvm), [nodist](https://github.com/nullivex/nodist) e [asdf](https://github.com/asdf-vm/asdf) para instalar/manusear multiplas versões, para cada projeto use uma versão específica.
:::

**Outra coisa que você pode fazer neste momento:**
- Usar `npm run format` para executar um formatador de código (Prettier) e corrigir alguns possíveis erros na formatação de estilo      
- Usar `npm run lint` para executar o linter e verificar se algum código não está seguindo as regras.
- Usar `npm run test:unit` para executar os testes do frontend
- Usar `npm run build` que irá gerar o diretório `dist` que contém html+css+js final a ser publicado.



## 🐞 Depurando a API do Django

::: danger 🚧 TODO

você pode ajudar!
:::

## 🐞 Depurando a web do VueJS

::: danger 🚧 TODO

você pode ajudar!
:::

## 🐋 Executar todo com Docker

**Requisitos:**

- Docker version >= 24.0.2 (para qualquer S.O.)
- Docker Compose version >= v2.18.1
- Um terminal shell (por ser um terminal linux, um terminal WSL no Windows ou um PowerShell), ⚠️ PowerShell pode ocorrer algumas diferenças nos comandos


O comportamento da aplicação em tempo de execução é baseada na configuração do ambiente seguindo os [12 fatores](https://12factor.net/), desta maneira, aplicação pode se conectar a um banco de dados sqlite ou a postgres, pode estar no modo de depuração ou não. Tudo pode ser modificado apenas com alteração de uma ou mais variáveis de ambiente sem mudar nenhum código.
O arquivo `.env` que guarda todas as variáveis que podem ser alteradas.

Para mudar o modo de execução: de execução local usando ambiente virtual (conforme observamos antes quando respondemos as perguntas na instalação) para uma execução em containers(docker), devemos alterar alguns valores dentro do arquivo .env.

::: code-group

```shell{13-17} [.env (📦 usando ambiente virtual)]
DEBUG=True
SECRET_KEY='cria-um-segredo-qualquer'
LANGUAGE_CODE=pt-br
TIME_ZONE=America/Sao_Paulo

POSTGRES_DB=db_posts
POSTGRES_USER=posts
POSTGRES_PASSWORD=posts

# ⚠️ AVISO
# É possível alterar entre COM DOCKER ou SEM DOCKER conforme as configurações abaixo

## 🖥️  Para uso local via virtualenv
POSTGRES_HOST=localhost
POSTGRES_PORT=15432
# DATABASE_URL=postgres://posts:posts@localhost:15432/db_posts
DATABASE_URL=sqlite:///db_local.sqlite3

## 🐳 Para uso via container/Docker
# POSTGRES_HOST=postgres
# POSTGRES_PORT=5432
# DATABASE_URL=postgres://posts:posts@postgres:5432/db_posts

```

```shell{19-22} [.env (🐋 usando docker)]
DEBUG=True
SECRET_KEY='cria-um-segredo-qualquer'
LANGUAGE_CODE=pt-br
TIME_ZONE=America/Sao_Paulo

POSTGRES_DB=db_posts
POSTGRES_USER=posts
POSTGRES_PASSWORD=posts

# ⚠️ AVISO
# É possível alterar entre COM DOCKER ou SEM DOCKER conforme as configurações abaixo

## 🖥️  Para uso local via virtualenv
# POSTGRES_HOST=localhost
# POSTGRES_PORT=15432
# DATABASE_URL=postgres://posts:posts@localhost:15432/db_posts
# DATABASE_URL=sqlite:///db_local.sqlite3

## 🐳 Para uso via container/Docker
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
DATABASE_URL=postgres://posts:posts@postgres:5432/db_posts
```
:::

::: info
👉 Para projeto existentes, podemos alterar o `.env` ou para um novo template, podemos responder conforme abaixo:

```shell{2,5} 
  ...
  [14/27] use_sqlite_local_env (no): no
  ...
  [21/27] Select docker_usage
    1 - 🐳 use docker by default
    2 - 📦 use venv npm by default
    Choose from [1/2] (1): 1
  ...
```
:::

Primeiro, independentemente de qual diretório você esteja, digite o seguinte comando e tenha certeza de que não existe nenhum container em execução.

```shell
docker ps

CONTAINER ID   IMAGE  COMMAND      CREATED       STATUS                PORTS 
``` 

::: info
👉 Caso tiver algum container em execução, será necessário interromper a execução usando o comando `docker stop [CONTAINER ID]`

:::

Então certifique-se que você esta na raiz do projeto

```shell
cd nome-projeto/
```

Se você já executou localmente o projeto frontend, provavelmente existe o diretório `node_modules` que foi criado quando as dependências foram criadas. Então será necessário excluir.


```shell
rm -rf nome-projeto/node_modules
```
Digite o seguinte comando para construir e executar tudo:

```shell
docker compose up -d
```

Após baixar as images e construir tudo, podemos executar o comando `docker ps`, deverá listar quatro containers em execução:


```shell
docker ps

CONTAINER ID  IMAGE COMMAND                 STATUS         PORTS        NAMES
1851a43bd     nginx "/docker..."            Up 10 minutes  80->7999     dashboardbeta-nginx-1
e5c00ed78     back-dashboard "bash -..."    Up 10 minutes  8000->8000   dashboardbeta-backend-1
078029b2b     front-dashboard "docker..."   Up 10 minutes  3000->3000   dashboardbeta-frontend-1
3f0949de3     postgres:13.3 "docker..."     Up 10 minutes  15432->5432  dashboardbeta-postgres-1
```

Esses containers estão em execução porque estão descritos dentro do arquivo `docker-compose.yaml` conforme abaixo:

::: code-group

```YAML{3,16,26,35} [docker-compose.yaml]
services:

  backend:
    image: back-nome-projeto
    hostname: back-nome-projeto
    build:
      context: ./
      dockerfile: Dockerfile
    env_file:
      - .env
    command: bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    ports:
      - 8000:8000
...

  postgres:
    image: "postgres:15-alpine"
    ports:
      - 15432:5432
    volumes:
      - postgres_data:/var/lib/postgresql/data
    env_file:
      - .env
...

  frontend:
    build:
      context: ./frontend
    image: front-nome-projeto
    command: npm run dev -- --host
    expose:
      - "3000"
...

  nginx:
    image: nginx
    ports:
      - 80:7999
    volumes:
      - ./docker/nginx/default_local:/etc/nginx/conf.d/default.conf

```
:::


**FEITO!! 🎉🎉** Os containers estão prontos para serem usados

👉 Abra o browser e acesse o frontend com a url `http://localhost`, lembre que temos um servidor web na frente do frontend, então se você acessar `http://localhost:3000` ao invés de `http://localhost` a página será apresentada, porém NÃO FUNCIONARÁ conforme esperado.

::: warning

- ✅ Usar `http://localhost`
- ⛔ Não usar `http://localhost:3000`

:::

Vocè também pode acessar o **backend container** e criar um usuário como fizemos no procedimento sem usar docker.
Então abra um terminal dentro do backend container usando o seguinte comando:

```shell
docker compose exec -it backend bash
```

Uma vez dentro do container, use comandos normal do Django, para criar um super usuário:

```shell
root@back-dashboardtarget:/app# ./manage.py createsuperuser
Usuário: admin
Endereço de email: admin@example.com
Password: **********
Password (again): **********
Superuser created successfully.
```
Use `CTRL+D` ou digite `exit` para fechar o terminal no container e voltar para o terminal local do host.


**Outra coisa que você pode fazer neste momento:**
- Usar `docker compose exec -it [nome-container] [comando]` e executar qualquer comando dentro do container (backend | postgres | frontend | nginx)
- Usar `docker compose down` para finalizar todos os containers
- Usar `docker compose logs -f [nome-container]` para verificar a saída (output) de um dos containers. Nota: Se um dos containers não estiver em execução, é possível usar este comando e ver o erro/causa do container não ficar operacional 


## 📦 Como fazer o gerenciamento do projeto com REQUIREMENTS

::: danger 🚧 TODO

você pode ajudar!
:::

## 📦 Como fazer o gerenciamento do projeto com Poetry

**Requisitos:**
- Verifique os requisitos do capítulo [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue)
- [Poetry](https://python-poetry.org/) instalado


Vamos recriar o projeto **nome-projeto** como fizemos durante [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue) mas agora escolheremos [Poetry](https://python-poetry.org/)

::: info
👉 Nesta etapa teremos menos detalhes devido aos links acima terem mais informações. 
:::

Executar o comando cookiecutter no diretório D-Jà Vue. você terá que fornecer alguns valores. Forneça-os baseado na necessidade do projeto e escolha  **'Poetry'** para o **'package_manager'**:

```
cookiecutter https://github.com/evolutio/djavue3
```
Responda às instruções com valores que satisfaçam a necessidade do seu projeto. Por exemplo: 

```shell
❯ cookiecutter https://github.com/evolutio/djavue3
  [1/27] project_name (My Todo List): <nome-projeto>
  [2/27] project_slug (nome-projeto):
  [3/27] description (The Ultimate Django and Vue Template): Faça uma descrição do seu projeto usando Poetry
  [4/27] app_name (core): <app_name será criada com nome=core>
  [5/27] model (Tasks): <nome do modelo dentro da app core>
  [6/27] model_lower (tasks):
...
  [10/27] Select package_manager
    1 - requirements.txt
    2 - pip-tools
    3 - poetry
    Choose from [1/2/3] (1): 3 <poetry será o gerenciador de pacotes>         👈
...
  [14/27] use_sqlite_local_env (no): yes
...
  [21/27] Select docker_usage
    1 - 🐳 use docker by default
    2 - 📦 use venv npm by default      👈
    Choose from [1/2] (1): 2
...
 [SUCCESS]: 🐍 Your Django API backend is created! (root) ✨ 🍰 ✨
 [SUCCESS]: 🍰 Your Vue 3 frontend is created! (frontend folder) ✨ 🍰 ✨
...
```
**FEITO!! 🎉🎉** A estrutura do projeto está criada! você pode abrir o diretório  `nome-projeto` e conferir! 

```shell
cd nome-projeto/
```
Então vamos pedir ao Poetry para criar o ambiente virtual dentro do projeto:

```shell
poetry config virtualenvs.in-project true
```

Instalando as dependências do projeto usando Poetry:

```shell
poetry install
```

::: info
👉 Diferentemente do virtualenv, Poetry irá criar e instalar as dependências do projeto dentro do ambiente virtual independente se o ambiente estiver ativo ou não. 
:::

Para executar o backend, será necessário ativar o ambiente virtual usando o seguinte comando:

```shell
poetry shell
```
Agora o ambiente está pronto e podemos executar as migrações e rodar o servidor. Verifique mais detalhes seguindo as etapas descritas no capítulo [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue)

**Outra coisa que você pode fazer neste momento:**
- Usar `poetry env info`, `poetry env info -p` and `poetry env list` para verificar com mais detalhes sobre o ambiente virtual criado com o Poetry 
- Usar `poetry add [some-python-lib]` para instalar e adicionar bibliotecas dentro do `pyproject.toml`
- Usar `deactivate` para sair do ambiente virtual ativado com o `poetry shell`
- Usar `poetry run flake8` para executar comandos sem mesmo estar com ambiente virtual ativado
- Usar `poetry show --tree` para mostrar as dependências e também dependências internas de alguma biblioteca
- Usar `poetry show --latest` para mostrar as bibliotecas (libs) que podem ser atualizadas.


## 📦 Como fazer o gerenciamento do projeto com Pip-tools

::: danger 🚧 TODO

você pode ajudar!
:::

## 📂 Estrutura & organização do Backend
::: danger 🚧 TODO

você pode ajudar!
:::

## 📂 Estrutura & organização do Frontend

::: danger 🚧 TODO

você pode ajudar!
:::

## 🤡 Usar API MOCK no Frontend

::: danger 🚧 TODO

você pode ajudar!
:::

## 🚀 Fluxo de trabalho para criação-(Build), Integração Continua-(CI) e implementação-(Deploy) 

::: danger 🚧 TODO

você pode ajudar!
:::

## ✨ Contibuições

::: danger 🚧 TODO

você pode ajudar!
:::
