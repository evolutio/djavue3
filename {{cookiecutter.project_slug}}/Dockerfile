FROM python:{{cookiecutter.python_version}}-slim

WORKDIR /app

{% if cookiecutter.package_manager == 'poetry' %}
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'
{% endif %}

# Install basic SO and Python
RUN apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    wget curl vim locales zip unzip apt-utils \
    && rm -rf /var/lib/apt/lists/* \
    && pip install uwsgi uwsgitop

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    echo "export LS_OPTIONS='--color=auto'" >>~/.bashrc && \
    echo "eval "\`dircolors\`"" >>~/.bashrc && \
    echo "alias ls='ls \$LS_OPTIONS'" >>~/.bashrc && \
    echo "alias ll='ls \$LS_OPTIONS -l'" >>~/.bashrc && \
    echo "alias l='ls \$LS_OPTIONS -lA'" >>~/.bashrc

#### Prepare BACKEND Django API
{% if cookiecutter.package_manager == 'poetry' %}
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry install --no-dev

{% elif cookiecutter.package_manager == 'pip-tools' %}
RUN pip install pip-tools==6.13.0
# RUN pip-compile --generate-hashes requirements-dev.in
# COPY requirements.txt ./
COPY requirements-dev.txt ./
RUN pip-sync requirements-dev.txt

{% else %}
COPY requirements.txt ./
COPY requirements-dev.txt ./

RUN pip install -r requirements-dev.txt
{% endif %}
ENV PYTHONUNBUFFERED=1 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONIOENCODING=UTF-8
ENV SHELL=/bin/bash LANG=en_US.UTF-8

COPY . ./

EXPOSE 8000

{% if cookiecutter.deploy_to == "fly.io" %}
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.wsgi"]
{% endif %}
