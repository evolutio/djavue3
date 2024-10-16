# 🐋 D-Jà Vue with Docker

## 🐋 Running all with docker

**Requirements:**

- Docker version >= 24.0.2 (in any S.O. you have)
- Docker Compose version >= v2.18.1
- A shell (it can be a linux terminal, a WSL Terminal on Windows or a PowerShell), ⚠️ PowerShell might have few differences in the commands

The way the application behaves in runtime is based on the settings for a given environment and following the [12 factors](https://12factor.net/), in this way, it can connect to a sqllite db or a postgres, it can be in a debug mode or not. Everything can be changed just by changing one or more environment variables without changing any code.
The file that keeps all variables and can be changed is the `.env` file 

To change from running locally using virtual environment (as we saw before and what was answered in the template prompt) to run everything in containers (docker), we must change some values inside the .env

::: code-group

```shell{13-17} [.env (📦 for virtualenv)]
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

```shell{19-22} [.env (🐋 for docker)]
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
👉 For an existing project, we can change the `.env` OR for a new template, we can answer as below:
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

First, independently which directory you are, type the following command to make sure there is no container running

```shell
docker ps

CONTAINER ID   IMAGE  COMMAND      CREATED       STATUS                PORTS 
``` 

::: info
👉 If you have something running, you'll need to stop everything by using the command `docker stop [CONTAINER ID]`
:::

Then make sure you are inside the project root

```shell
cd twitterclone/
```

If you already run locally the frontend project, probably there are the `node_modules` folder which was created when you installed the dependencies. So you'll need to delete it

```shell
rm -rf frontend/node_modules
```

Enter the following command to build and run everything:

```shell
docker compose up -d
```

After downloading the image layers and building everything, by running again the command `docker ps`, it should list four containers up running:

```shell
docker ps

CONTAINER ID  IMAGE COMMAND                 STATUS         PORTS        NAMES
1851a43bd     nginx "/docker..."            Up 10 minutes  80->7999     dashboardbeta-nginx-1
e5c00ed78     back-dashboard "bash -..."    Up 10 minutes  8000->8000   dashboardbeta-backend-1
078029b2b     front-dashboard "docker..."   Up 10 minutes  3000->3000   dashboardbeta-frontend-1
3f0949de3     postgres:13.3 "docker..."     Up 10 minutes  15432->5432  dashboardbeta-postgres-1
```

Those container are running because they are described inside the `docker-compose.yaml` file as below

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


**DONE!! 🎉🎉** The containers are ready to use

👉 Open your browser and access frontend at `http://localhost`, remember we do have a web server in front of the frontend, so if you access `http://localhost:3000` instead of `http://localhost` it will show the page, however, it WONT WORK as expected.

::: warning

- ✅ Use `http://localhost`
- ⛔ Don't use `http://localhost:3000`

:::


You also can access the **backend container** and create a user as we did without docker. So open a terminal inside the backend container by the following command:

```shell
docker compose exec -it backend bash
```

Once inside the container, use the normal django commands, for example the create super user:

```shell
root@back-dashboardtarget:/app# ./manage.py createsuperuser
Usuário: admin
Endereço de email: admin@example.com
Password: **********
Password (again): **********
Superuser created successfully.
```

Use `CTRL+D` or type `exit`to finish the terminal and go back to host terminal

**Other things that you can do at this point:**
- Use `docker compose exec -it [container-name] [command]` and execute any command inside any container (backend|postgres|frontend|nginx)
- Use `docker compose down` to stop all containers
- Use `docker compose logs -f [container-name]`to check out the output from one of the containers. Note: if one of the containers didn't run, it's possible to use this command and see the error/cause the container didn't get up.