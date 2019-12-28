#!/usr/bin/env python
# -*- coding: utf-8 -*-
# {{ cookiecutter.copyright_notice }}

from setuptools import find_packages, setup
from typing import List

from {{ cookiecutter.pkg_name }} import __author__, __contact__, __homepage__, __version__


def parse_requirements(fname: str) -> List[str]:
    """Extracts a list of dependencies from the given requirements file."""
    with open(fname) as src:
        return [
            line
            for line in (rl.strip() for rl in src)
            if line and not line.startswith("-e") and not line.startswith("#")
        ]


with open("README.rst") as src:
    readme = src.read()

with open("HISTORY.rst") as src:
    history = src.read().replace(".. :changelog:", "").strip()

requirements = parse_requirements("requirements.txt")
dev_requirements = parse_requirements("requirements-dev.txt")


setup(
    name="{{ cookiecutter.pkg_name }}",
    version=__version__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + "\n\n" + history,
    author=__author__,
    author_email=__contact__,
    url=__homepage__,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    include_package_data=True,
    install_requires=requirements,
    tests_require=dev_requirements,
    extras_require={"dev": dev_requirements },
    {%- if not 'no' in cookiecutter.has_cli | lower %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.pkg_name }}={{ cookiecutter.pkg_name }}.cli:main"
        ]
    },
    {%- endif %}
    zip_safe=False,
    keywords="{{ cookiecutter.pkg_name }}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: {{ cookiecutter.python_version.split('.')[:2] | join('.') }}",
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
