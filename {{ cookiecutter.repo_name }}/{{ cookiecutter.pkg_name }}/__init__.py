# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.pkg_name }}
    {{ '~' * cookiecutter.pkg_name | length }}

    :copyright: (c) {% now 'local', '%Y' %} {{ cookiecutter.author_full_name }} <{{ cookiecutter.author_email }}>
    :license: {{ cookiecutter.license }}

"""
#  {{ cookiecutter.copyright_notice }}

RELEASE = False

__version_info__ = ("0", "1", "0")
__version__ = ".".join(__version_info__)
__version__ += "-dev" if not RELEASE else ""

__author__ = "{{ cookiecutter.author_full_name }}"
__contact__ = "{{ cookiecutter.author_email }}"
__homepage__ = "{{ cookiecutter.homepage }}"
