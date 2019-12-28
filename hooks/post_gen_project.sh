#!/usr/bin/env sh

# Cookiecutter post_gen_project hook.

set -uexo pipefail

# Setup git repo, if possible.
if command -v git 1>/dev/null 2>&1
then
    git init
    git remote add origin '{{ cookiecutter.repo_url }}'
fi

# Setup pyenv virtualenv and install dependencies, if possible.
if command -v pyenv 1>/dev/null 2>&1
then
    PY_VERSION='{{ cookiecutter.python_version }}'
    ENV_NAME='{{ cookiecutter.repo_name }}'-dev
    pyenv virtualenv -f ${PY_VERSION} ${ENV_NAME}
    echo -e "${ENV_NAME}\n${PY_VERSION}" > .python-version
    pip install --upgrade pip
    pip install -e .[dev]
 fi
