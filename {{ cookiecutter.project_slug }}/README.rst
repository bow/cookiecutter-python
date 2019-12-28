{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{% if cookiecutter.use_travis %}
.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.png?branch=master
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
{% endif %}

{% if cookiecutter.use_codecov %}
.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
{% endif %}

{{ cookiecutter.project_short_description}}

Requirements
------------

* Python 3.5


Development Setup
-----------------


