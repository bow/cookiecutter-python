# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.pkg_name }}
    {{ '~' * cookiecutter.pkg_name | length }}

    :copyright: (c) {% now 'local', '%Y' %} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
    :license: {{ cookiecutter.license }}

"""

RELEASE = False

__version_info__ = ("0", "1", "0")
__version__ = ".".join(__version_info__)
__version__ += "-dev" if not RELEASE else ""

__author__ = "{{ cookiecutter.full_name }}"
__contact__ = "{{ cookiecutter.email }}"
__homepage__ = "{{ cookiecutter.homepage }}"
