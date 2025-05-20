# 📦 Package Management

## 📦 Package Management with requirements

::: danger 🚧 TODO

You can help here!
:::

## 📦 Package Management with Poetry

**Requirements:**
- Check the requirements for the chapter [📦 Creating my first project using D-Jà Vue](#📦-creating-my-first-project-using-d-ja-vue)
- [Poetry](https://python-poetry.org/) installed

Let's recreate the **twitterclone** like it was done in the [📦 Creating my first project using D-Jà Vue](#📦-creating-my-first-project-using-d-ja-vue) but now choosing [Poetry](https://python-poetry.org/)

::: info
👉 This step has less details due to the links above has more information.
:::

Run the cookiecutter command against the D-Jà Vue repository. You'll be prompted for some values. Provide them based on your needs and choose **'Poetry'** for the **'package_manager'**:

```
cookiecutter https://github.com/evolutio/djavue3
```

Answer the prompts with your own desired flavours. For example:

```shell
❯ cookiecutter https://github.com/evolutio/djavue3
  [1/27] project_name (My Todo List): Twitter Clone
  [2/27] project_slug (twitterclone):
  [3/27] description (The Ultimate Django and Vue Template): My first Djavue template using Poetry
  [4/27] app_name (core): posts
  [5/27] model (Tasks): Tweets
  [6/27] model_lower (tweets):
...
  [10/27] Select package_manager
    1 - requirements.txt
    2 - pip-tools
    3 - poetry
    Choose from [1/2/3] (1): 3          👈
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

**DONE!! 🎉🎉** The project structure is created! You can open the folder `twitterclone` and check it out!

```shell
cd twitterclone/
```

Then let's tell Poetry to create the virtual environment inside de project:

```shell
poetry config virtualenvs.in-project true
```

Then install de project dependencies using Poetry:

```shell
poetry install
```

::: info
👉 Differently from virtualenv, Poetry will create and install the dependencies inside the virtual environment whitout it being active.
:::

To run the backend, it will be necessary to active the environment using the following command:

```shell
poetry shell
```

Now the environment is ready and it's possible to execute the migrations and the run server. Check more details following the steps over the chapter [📦 Creating my first project using D-Jà Vue](#📦-creating-my-first-project-using-d-ja-vue)

**Other things that you can do at this point:**
- Use `poetry env info`, `poetry env info -p` and `poetry env list` to check more details about the virtual environment created by Poetry
- Use `poetry add [some-python-lib]` to install and add it to the `pyproject.toml`
- Use `deactivate` to exit the poetry environment activated by the `poetry shell`
- Use `poetry run flake8` to run something without activating the environment
- Use `poetry show --tree` to show the dependencies and its internal dependencies too
- Use `poetry show --latest` to show libs that can be updated


## 📦 Package Management with Pip-tools

::: danger 🚧 TODO

You can help here!
:::