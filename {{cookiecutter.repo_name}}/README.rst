===============================
{{ cookiecutter.project_name }}
===============================

Describe the project here.

.. image:: https://badge.fury.io/py/{{ cookiecutter.distribution_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}
    :alt: {{ cookiecutter.project_name }} Pypi package page

.. image:: https://readthedocs.org/projects/{{ cookiecutter.distribution_name }}/badge/?version=latest
    :target: http://{{ cookiecutter.distribution_name }}.readthedocs.org/en/latest/
    :alt: {{ cookiecutter.project_name }} latest documentation Status
.. image:: https://readthedocs.org/projects/{{ cookiecutter.distribution_name }}/badge/?version=develop
    :target: http://{{ cookiecutter.distribution_name }}.readthedocs.org/en/develop/
    :alt: {{ cookiecutter.project_name }} development documentation Status

Features
--------

A list of features

- A feature
- Another feature
- Yet another feature

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of Sphinx. For this use the makefile, or the make.bat
file, contained on that folder.

Usage
-----

The application has been coded in Python, without using any particular
framework.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.6
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4
- Pypy
- Pypy 3
- Jython

All other dependencies are indicated on the requirements.txt file.
The included makefile can install them with the command:

``$ make requirements``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``$ pip install {{ cookiecutter.distribution_name }}``

If manual installation is required, the project includes a setup.py file, along
a makefile allowing direct installation of the library, which can be done with
the following command:

``$ make install``

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

.. _GitHub project page: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. _latest docs: http://{{ cookiecutter.distribution_name }}.readthedocs.org/en/latest/
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _project issues tracker: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
.. _Sphinx: http://sphinx-doc.org/
