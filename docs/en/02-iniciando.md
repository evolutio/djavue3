# 💿 Initializing

## 🛠️ D-Jà Vue template requirements

To use the Djavue **to create** your project, you'll need only:
- 🐍 Python +3.10
- 🍪 Cookiecutter +1.7

To **Run** everything (the project created), you can choose to two ways 🍨:
- Using Docker 🐋: **Docker** and **Docker compose**
- Without Docker 📦: **Python** for the backend and **Node JS** for the frontend


## 📦 Creating my first project using D-Jà Vue

First, get [cookiecutter](https://github.com/cookiecutter/cookiecutter/). It's awesome:

```
pip install "cookiecutter>=1.7.0"
```

::: tip
🌈 TIPS/TRICKS: You can use [pipx ](https://pypa.github.io/pipx/) to install cookiecutter globally or creating a pyenv env and set the envs orders and avoiding installing directly in your machine without environments.
:::

Now run it against the D-Jà Vue repositoty. You'll be prompted for some values. Provide them based on your needs!

::: info
👉 Mainly if you are not using Docker and want to use the same Python you have in your machine, use `python -V` to get your current python version. You also can do the same thing for the the NodeJS version `node --version`.
:::

```
cookiecutter https://github.com/evolutio/djavue3
```

Answer the prompts with your own desired flavours. For example:

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
    2 - pip-tools
    3 - poetry
    Choose from [1/2/3] (1): 1
  [11/27] Select python_linter
    1 - flake8
    2 - pylint
    3 - ruff
    Choose from [1/2/3] (1): 
  [12/27] Select django_api
    1 - 🦄 django_only
    2 - 🥷 django_ninja
    3 - 📄 openapi
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
  [27/27] Select license
    1 - MIT
    2 - agpl-3.0
    Choose from [1/2] (1): 
 
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

**DONE!! 🎉🎉** Your first project structure is created! You can open the folder `twitterclone` and check it out!

**What's next?** The next step is to run it locally and make sure everything is working! Then you can start working on the next important feature to your product or idea!✨

Basically, there are two ways to RUN your project, for the above project we answered to **RUN (initially) WITHOUT DOCKER**, however, by changing the environment variables (.env file) we can change it any time to **RUN USING DOCKER** 🐋

Keep reading to understand the difference!

::: warning
⚠️ This is a **"Twitter Clone"** in terms of UI, the architecture and system design is far way what the real twitter contains. This still a simple frontend and backend API CRUD web app.
:::


## 🐋 Run locally using Docker vs not using Docker (containers)

Using containers (docker) it’s a convenient mode where it aims to have all dependencies as it is in production included and zero configuration, it does not install things in the local machine, by installing just one dependency (docker) you can run as much closer as possible as it runs in production by running one command. It's the best way to run everything locally and give a good developer experience.

::: info
Using 🐋 Docker is the way where you can have a project that have many dependencies internally (libs, frameworks and also SO dependencies) and externally for example database, web mail server, queue manager etc and RUN everything with ONE CLICK. It's quite common developers work on multiple projects, which one uses different Python and Database versions, by managing those matrix of possible each time you swap a project could be a nightmare! The container concept is here to save us!
:::

![local-env-with-docker](../../images/local-env-using-docker.jpg)

Using the D-Jà Vue template, your project will have the container concept from the Day 1, whether you will start without it or not, being ready to run it with docker is a good thing, mainly to make the devops better (a.k.a deploy to production)

📦 **Running without docker** can be pretty handy too, it can be much easier to debug, however, it’s necessary to create a virtual environment, install all dependencies in both the backend and frontend projects and have few extra configurations to make the frontend access the backend (CORS settings). It will depend on the developer using tools such as NVM and Pyenv in order to make the local machine be in the same node and python version as the production will.

![local-env-without-docker](../../images/local-env-without-docker.jpg)

The good thing is that D-Jà Vue template is using a good foundation to make the developer experience as better as possible whether choosing non friction environment with no docker at all, for example, running a SQLite database locally and any python version available or mixing by running just the postgres database inside a container and of course, being as close as possible from what will run in production, for example, having the web server or any other external service that the project might integrate with.