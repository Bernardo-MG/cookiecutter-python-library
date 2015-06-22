===========================
Cookiecutter Python Library
===========================


.. image:: https://readthedocs.org/projects/cookiecutter-python-library/badge/?version=latest
    :target: http://cookiecutter-python-library.readthedocs.org/en/latest/
    :alt: Cookiecutter Python Library latest documentation Status

Cookiecutter template for creating general-purpose Python libraries.

While it mostly follows my personal tastes, it offers a series of good 
practices which include deployment files, makefile, testing, and the use of 
various free services, such as Github, Travis and Pypi.

Features
--------

- Travis configuration file
- Customized setup.py module to minimize configuration, and using tox for the tests
- Prepared to run tests through tox
- Prepared to run tests on Python 2.6, 2.7, 3.2, 3.3, 3.4
- Prepared to run tests on pypy and pypy 3
- Prepared to run tests on Jython
- Prepared to run coverage tests and integrate with `Coveralls`_
- Prepared to run tests for the `Sphinx`_ documentation

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of Sphinx. For this use the makefile, or the make.bat
file, contained on that folder.

Building the code
-----------------

The template has been prepared for `Cookiecutter`_, and consists of Python
code and Jinja2 labels.

Prerequisites
~~~~~~~~~~~~~

Cookiecutter is required to make use of this template. It can be acquired
through pip:

``$ pip install cookiecutter``

Installing
~~~~~~~~~~

The template can be used from the command line with the following command:

``$ cookiecutter gh:bernardo-mg/cookiecutter-python-library``

This will download the template and begin to create a new project.

It is only needed to download the template once. After that, it can be reused
with the following command:

``$ cookiecutter cookiecutter-python-library/``

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
.. _latest docs: http://cookiecutter-python-library.readthedocs.org/en/latest/
.. _GitHub project page: https://github.com/Bernardo-MG/cookiecutter-python-library
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
