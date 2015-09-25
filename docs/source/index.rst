===========================
Cookiecutter Python Library
===========================

This is the documentation for the Cookiecutter Python Library.

Created to fit my own tastes, this library offers a series of good practices,
and a bunch of configurations I've found useful.

--------
Features
--------

- Travis configuration file
- Customized setup.py module to minimize configuration, and using tox for the tests
- Docs using `Sphinx`_ and the `Sphinx Docs Theme`_
- Prepared to run tests through tox
- Prepared to run tests on Python 2.6, 2.7, 3.2, 3.3, 3.4
- Prepared to run tests on pypy and pypy 3
- Prepared to run tests on Jython
- Prepared to run coverage tests and integrate with `Coveralls`_
- Prepared to run tests for the `Sphinx`_ documentation

.. toctree::
   :hidden:

   acquire
   usage
   doc_site
   makefile
   tests


.. _Coveralls: https://coveralls.io
.. _Sphinx: http://sphinx-doc.org/
.. _Sphinx Docs Theme: https://github.com/Bernardo-MG/sphinx-docs-theme