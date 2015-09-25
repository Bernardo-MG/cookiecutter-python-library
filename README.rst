===========================
Cookiecutter Python Library
===========================

Cookiecutter template for creating general-purpose Python libraries.

While it mostly follows my personal tastes, it offers a series of good 
practices which include deployment files, makefile, testing, and the use of 
various free services, such as Github, Travis and Pypi.

.. image:: https://readthedocs.org/projects/cookiecutter-python-library/badge/?version=latest
    :target: http://cookiecutter-python-library.readthedocs.org/en/latest/
    :alt: Cookiecutter Python Library latest documentation Status
.. image:: https://readthedocs.org/projects/cookiecutter-python-library/badge/?version=develop
    :target: http://cookiecutter-python-library.readthedocs.org/en/develop/
    :alt: Cookiecutter Python Library development documentation Status

Features
--------

Projects created with this template come with the following features:

- Travis configuration file
- Customized setup.py module to minimize configuration, and using tox for the tests
- Docs using `Sphinx`_ and the `Sphinx Docs Theme`_
- Prepared to run tests through tox
- Prepared to run tests on Python 2.6, 2.7, 3.2, 3.3, 3.4
- Prepared to run tests on pypy and pypy 3
- Prepared to run tests on Jython
- Prepared to run coverage tests and integrate with `Coveralls`_
- Prepared to run tests for the `Sphinx`_ documentation

Demo
----

An example of what can be created with this template is found at the
`cookiecutter-python-library-demo`_.

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of Sphinx. For this use the makefile, or the make.bat
file, contained on that folder.

Usage
-----

The template has been prepared for `Cookiecutter`_, and consists of Python
code and Jinja2 labels.

Prerequisites
~~~~~~~~~~~~~

`Cookiecutter`_ is required to make use of this template. It can be acquired
through pip:

``$ pip install cookiecutter``

Of course, a Python interpreter is also required. To find the valid versions
check the Cookiecutter page.

All other dependencies are indicated on the requirements.txt file.
These can be installed with the included makefile by using the following
command:

``$ make requirements``

Installing and creating a new project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The template can be used from the command line with the following command:

``$ cookiecutter gh:bernardo-mg/cookiecutter-python-library``

This will download the template and begin to create a new project. After this
the template has been installed on the local computer, and can be reused with
the following command:

``$ cookiecutter cookiecutter-python-library/``

Collaborate
-----------

Any kind of help with the project will be well received, and there are two main ways to give such help:

- Reporting errors and asking for extensions through the issues management
- or forking the repository and extending the project

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues tracker`_, where any Github
user may report bugs or ask for new features.

Getting the code
~~~~~~~~~~~~~~~~

If you wish to fork or modify the code, visit the `GitHub project page`_, where
the latest versions are always kept. Check the 'master' branch for the latest
release, and the 'develop' for the current, and stable, development version.

License
-------

The project has been released under the `MIT License`_.

.. _Coveralls: https://coveralls.io
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _GitHub project page: https://github.com/Bernardo-MG/cookiecutter-python-library
.. _project issues tracker: https://github.com/Bernardo-MG/cookiecutter-python-library/issues
.. _latest docs: http://cookiecutter-python-library.readthedocs.org/en/latest/
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _Sphinx: http://sphinx-doc.org/
.. _Sphinx Docs Theme: https://github.com/Bernardo-MG/sphinx-docs-theme
.. _cookiecutter-python-library-demo: https://github.com/Bernardo-MG/cookiecutter-python-library-demo
