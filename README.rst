===========================
Cookiecutter Python Library
===========================

Cookiecutter template for creating general-purpose Python libraries.

While it mostly follows my personal tastes, it offers a series of good 
practices which include deployment files, makefile, testing, and the use of 
various free services, such as Github, Travis and Pypi.

Features
--------

- Travis configuration file
- Customized setup.py module, using tox for the tests and requiring little additional configuration
- Prepared to run tests through tox
- Prepared to run tests on Python 2.6, 2.7, 3.2, 3.3, 3.4
- Prepared to run tests on pypy and pypy 3
- Prepared to run tests on Jython
- Prepared to run coverage tests and integrate with `Coveralls`_
- Prepared to run tests for the `Sphinx`_ documentation

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

They are generated with the help of `Sphinx`_. The source files for this are
stored in the docs folder.

Building the code
-----------------

The template has been prepared for `Cookiecutter`_, and consists of Python
code and Jinja2 labels.

Prerequisites
~~~~~~~~~~~~~

`Cookiecutter`_ is required to make use of this template. It can be acquired
through pip:

``pip install cookiecutter``

Installing
~~~~~~~~~~

The template can be used from the command line with the following command:

``cookiecutter gh:bernardo-mg/cookiecutter-python-library``

This will download the template and begin to create a new project.

It is only needed to download the template once. After that, it can be reused
with the following command:

``cookiecutter cookiecutter-python-library/``

Collaborate
-----------

The project is still under ongoing development, and any help will be well
received.

There are two ways to help: reporting errors and asking for extensions through
the issues management, or forking the repository and extending the project.

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues page`_.

Everybody is allowed to report bugs or ask for features.

Getting the code
~~~~~~~~~~~~~~~~

The code can be found at the `GitHub project page`_.

Feel free to fork it, and share the changes.

License
-------

The project has been released under the `MIT License`_.

.. _Coveralls: https://coveralls.io
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _project issues page: https://github.com/Bernardo-MG/cookiecutter-python-library/issues
.. _Sphinx: http://sphinx-doc.org/
.. _latest docs: http://bmg-cc-python-lib.readthedocs.org
.. _GitHub project page: https://github.com/Bernardo-MG/cookiecutter-python-library
.. _MIT License: http://www.opensource.org/licenses/mit-license.php