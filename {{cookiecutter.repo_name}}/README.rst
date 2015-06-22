===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.distribution_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}
    :alt: {{ cookiecutter.project_name }} Pypi package page

.. image:: https://readthedocs.org/projects/{{ cookiecutter.distribution_name }}/badge/?version=latest
    :target: http://{{ cookiecutter.distribution_name }}.readthedocs.org/en/latest/
    :alt: {{ cookiecutter.project_name }} latest documentation Status

Describe the project here.

Features
--------

A list of features

- A feature
- Another feature
- Yet another feature

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

They are generated with the help of `Sphinx`_. The source files for this are
stored in the docs folder.

Building the code
-----------------

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

The project includes a setup.py file, along a makefile allowing direct
installation of the library.

This can be done with the following command:

``$ make install``

Additionally, the project is offered as a `Pypi package`_, and can be installed through pip:

``$ pip install {{ cookiecutter.distribution_name }}``

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

.. _project issues page: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
.. _Sphinx: http://sphinx-doc.org/
.. _latest docs: http://{{ cookiecutter.distribution_name }}.readthedocs.org/en/latest/
.. _GitHub project page: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
