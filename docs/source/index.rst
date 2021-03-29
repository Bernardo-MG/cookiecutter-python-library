===========================
Cookiecutter Python Library
===========================

This is the documentation for the Cookiecutter Python Library.

Created to fit my own tastes, this library offers a series of good practices,
and a bunch of configurations I've found useful.

--------
Features
--------

- Github Workflow configuration file
- Customized setup.py module to minimize configuration, and using tox for the tests
- Run tests with a command
- Docs using `Sphinx`_ and the `Sphinx Docs Theme`_
- Build the docs with a command
- Prepared to run tests through tox
- Prepared to run tests on Python 3
- Prepared to run tests on pypy 3
- Prepared to run coverage tests and integrate with `Coveralls`_
- Prepared to run tests for the `Sphinx`_ documentation

.. toctree::
   :hidden:

   acquire
   usage
   building
   doc_site
   tests


.. _Coveralls: https://coveralls.io
.. _Sphinx: http://sphinx-doc.org/
.. _Sphinx Docs Theme: https://github.com/Bernardo-MG/sphinx-docs-theme