==================
cookiecutter-pypkg
==================

Opinionated cookiecutter template for a Python package, based on
https://github.com/audreyr/cookiecutter.

* Multiple license to choose from: BSD 3-Clause, MIT, Apache 2.0, or Proprietary
* Testing setup with `pytest`
* Travis-CI: Ready for Travis Continuous Integration testing
* Sphinx docs: Documentation ready for generation with, for example, ReadTheDocs

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/bow/cookiecutter-pypkg.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987
