# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.pkg_name }}
    {{ '~' * cookiecutter.pkg_name | length }}

    :copyright: (c) {% now 'local', '%Y' %} {{ cookiecutter.author_full_name }} <{{ cookiecutter.author_email }}>
    :license: {{ cookiecutter.license }}

"""
#  {{ cookiecutter.copyright_notice }}

__author__ = "{{ cookiecutter.author_full_name }}"
__contact__ = "{{ cookiecutter.author_email }}"
__homepage__ = "{{ cookiecutter.project_homepage }}"

from ._version import get_versions
__version__ = get_versions()["version"]
del get_versions
