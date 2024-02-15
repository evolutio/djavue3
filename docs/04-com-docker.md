# 🐋 D-Jà Vue com Docker

Se quiser saber mais sobre a diferença entre SEM ou COM Docker, [leia mais aqui](./02-iniciando.md#🐋-diferenca-entre-executar-localmente-com-docker-ou-sem-docker-containers)

## 🐋 Executar tudo com Docker

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
cd twitterclone/
```

Se você já executou localmente o projeto frontend, provavelmente existe o diretório `node_modules` que foi criado quando as dependências foram criadas. Então será necessário excluir.


```shell
rm -rf twitterclone/node_modules
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
    image: back-twitterclone
    hostname: back-twitterclone
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
    image: front-twitterclone
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

Você também pode acessar o **backend container** e criar um usuário como fizemos no procedimento sem usar docker.
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