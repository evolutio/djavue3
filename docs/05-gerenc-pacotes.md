# 📦 Gerenciador de Pacotes

## 📦 Com REQUIREMENTS.txt

**Requisitos:**
- Verifique os requisitos do capítulo [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue)
- [pip](https://pypi.org/project/pip/) instalado


Vamos recriar o projeto **twitterclone** como fizemos durante [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue) mas agora escolheremos o gerenciador de pacotes python `requirements.txt` 

::: info
👉 Nesta etapa iremos dar enface na parametrização de como gerenciar o pacote python com `requirement.txt` (guardam as dependências do projeto) e o `requirement-dev.txt` (guardam as dependências de desenvolvimento). 
:::

Executar o comando cookiecutter no repositório D-Jà Vue. Você terá que fornecer alguns valores, e você deve fornece-los baseado na necessidade do projeto e escolha  **'requirements.txt'** para o **'package_manager'**:

```
cookiecutter https://github.com/evolutio/djavue3
```
Responda às instruções com valores que satisfaçam a necessidade do seu projeto. Por exemplo: 

```shell
❯ cookiecutter https://github.com/evolutio/djavue3
  [1/27] project_name (My Todo List): Twitter Clone
  [2/27] project_slug (twitterclone):
  [3/27] description (The Ultimate Django and Vue Template): Djavue template com reqirements.txt
  [4/27] app_name (core): posts
  [5/27] model (Tasks): Tweets
  [6/27] model_lower (tweeks):
...
  [10/27] Select package_manager
    1 - requirements.txt
    2 - poetry
    Choose from [1/2] (1): 1 <requirements.txt -> gerenciador de pacotes>         👈
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
**FEITO!! 🎉🎉** A estrutura do projeto está criada! você pode abrir o diretório  `twitterclone` e conferir. 

Então vamos criar o ambiente virtual dentro do projeto:

```shell
python -m venv .venv
```

::: info
👉 Caso você seja iniciante com Python, pode ocorrer um erro quando executar o comando `python -m venv .venv`, então voce pode executar `python3 -m venv .venv`
:::

Depois de criado o ambiente virtual é necessário ativá-lo com o seguinte comando:

```shell
source .venv/bin/activate
```

Continuando, será necessário instalar as dependências do projeto usando os arquivos `requirements.txt` e o `requirements-dev.txt`:

```shell
pip install -r requirements-dev.txt
```

::: code-group

```shell[(📦 requirements.txt)]
# Django
Django==4.1.7
asgiref==3.6.0
sqlparse==0.4.3
tzdata==2023.3

# 3rd
# django-sql-explorer==2.4.2
django-extensions==3.2.1

# DB
psycopg2==2.9.5
dj-database-url==1.3.0

# ENV
python-decouple==3.8


# PROD
#uWSGI==2.0.21
```

```shell[(📦  requirements-dev.txt)]
-r requirements.txt

# Code style / formatting
black==23.3.0
isort==5.12.0
flake8==5.0.4

#Testes
pytest==7.2.2
pytest-django==4.5.2
mock==5.1.0

# Better Dev Experience
ipython==8.16.1

# CORS (para quando o frontend está em domínio diferente)
django-cors-headers==4.3.0
```
:::


::: info
👉 Na instalação das dependências, foi usado o arquivo `requirements-dev.txt`, pois este arquivo contêm as dependências de desenvolvimento e tambem uma referência do arquivo `requirements.txt`. 
:::


Agora o ambiente está pronto e podemos executar as migrações e rodar o servidor. Verifique mais detalhes seguindo as etapas descritas no capítulo [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue)

**Outros comandos uteis que você pode fazer neste momento:**
- Usar `pip install --upgrade pip`, para atualizar a versão do pip 
- Usar `pip install [some-python-lib]` para instalar e adicionar bibliotecas dentro do projeto
- Usar `deactivate` para sair do ambiente virtual ativado com o `source .venv/bin/activate`
- Usar `flake8 .` para verificar possíveis erros de sintaxes no código, e fornece instruções para corrigir.
- Usar `pip list -o` para mostrar as dependências do projeto que estão desatualizadas.


## 📦 Com Poetry

**Requisitos:**
- Verifique os requisitos do capítulo [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue)
- [Poetry](https://python-poetry.org/) instalado


Vamos recriar o projeto **twitterclone** como fizemos durante [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue) mas agora escolheremos [Poetry](https://python-poetry.org/)

::: info
👉 Nesta etapa teremos menos detalhes devido aos links acima terem mais informações. 
:::

Executar o comando cookiecutter no repositório D-Jà Vue. você terá que fornecer alguns valores. Forneça-os baseado na necessidade do projeto e escolha  **'Poetry'** para o **'package_manager'**:

```
cookiecutter https://github.com/evolutio/djavue3
```
Responda às instruções com valores que satisfaçam a necessidade do seu projeto. Por exemplo: 

```shell
❯ cookiecutter https://github.com/evolutio/djavue3
  [1/27] project_name (My Todo List): twitterclone
  [2/27] project_slug (twitterclone):
  [3/27] description (The Ultimate Django and Vue Template): Faça uma descrição do seu projeto usando Poetry
  [4/27] app_name (core): <app_name será criada com nome=core>
  [5/27] model (Tasks): <nome do modelo dentro da app core>
  [6/27] model_lower (tasks):
...
  [10/27] Select package_manager
    1 - requirements.txt
    3 - poetry
    Choose from [1/2] (1): 3 <poetry será o gerenciador de pacotes>         👈
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
**FEITO!! 🎉🎉** A estrutura do projeto está criada! você pode abrir o diretório  `twitterclone` e conferir! 

```shell
cd twitterclone/
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
