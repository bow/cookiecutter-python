#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from {{ cookiecutter.pkg_name }} import __author__, __contact__, \
        __homepage__, __version__


with open("README.rst") as src:
    readme = src.read()

with open("HISTORY.rst") as src:
    history = src.read().replace(".. :changelog:", "").strip()

with open("requirements.txt") as src:
    requirements = [line.strip() for line in src]

with open("requirements-dev.txt") as src:
    test_requirements = [line.strip() for line in src]


setup(
    name="{{ cookiecutter.pkg_name }}",
    version=__version__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + "\n\n" + history,
    author=__author__,
    author_email=__contact__,
    url=__homepage__,
    packages=find_packages(exclude=["*.tests", "*.tests.*",
                                    "tests.*", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    {%- if not 'no' in cookiecutter.has_cli | lower %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.pkg_name }}={{ cookiecutter.pkg_name }}.cli:main"
        ]
    },
    {%- endif %}
    zip_safe=False,
    keywords="{{ cookiecutter.pkg_name }}",
    tests_require=test_requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        {%- if cookiecutter.license == "BSD 3-Clause" %}
        "License :: OSI Approved :: BSD License",
        {%- elif cookiecutter.license == "MIT" %}
        "License :: OSI Approved :: Apache Software License",
        {%- elif cookiecutter.license == "Apache 2.0" %}
        "License :: OSI Approved :: MIT License",
        {%- else %}
        "License :: Other/Proprietary License",
        {%- endif %}
    ],
)
