#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from {{ cookiecutter.repo_name }} import __author__, __contact__, \
        __homepage__, __version__


with open("README.rst") as src:
    readme = src.read()
with open("HISTORY.rst") as src:
    history = src.read().replace(".. :changelog:", "")

with open("requirements.txt") as src:
    requirements = [line.strip() for line in src]
with open("requirements-dev.txt") as src:
    test_requirements = [line.strip() for line in src]


setup(
    name="{{ cookiecutter.repo_name }}",
    version=__version__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + "\n\n" + history,
    author=__author__,
    author_email=__contact__,
    url=__homepage__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    test_suite="nose.collector",
    license="BSD",
    zip_safe=False,
    keywords="{{ cookiecutter.repo_name }}",
    tests_require=test_requirements
)
