# 📦 Gerenciador de Pacotes

## 📦 Com REQUIREMENTS.txt

::: danger 🚧 TODO

você pode ajudar!
:::

## 📦 Com Poetry

**Requisitos:**
- Verifique os requisitos do capítulo [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue)
- [Poetry](https://python-poetry.org/) instalado


Vamos recriar o projeto **twitterclone** como fizemos durante [📦 Criação do primeiro usando D-Jà Vue](#📦-criacao-do-primeiro-projeto-usando-d-ja-vue) mas agora escolheremos [Poetry](https://python-poetry.org/)

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
  [1/27] project_name (My Todo List): twitterclone
  [2/27] project_slug (twitterclone):
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


## 📦 Com Pip-tools

::: danger 🚧 TODO

você pode ajudar!
:::