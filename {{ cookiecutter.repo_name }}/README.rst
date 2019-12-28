{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{% if cookiecutter.use_travis %}
.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png?branch=master
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}

{% if cookiecutter.use_codecov %}
.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
{% endif %}

{{ cookiecutter.project_short_description}}

Requirements
------------

* Python {{ cookiecutter.python_version.split('.')[:2] | join('.') }}


Development Setup
-----------------


