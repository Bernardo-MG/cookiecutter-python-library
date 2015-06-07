###############################
{{ cookiecutter.project_name }}
###############################

This is the documentation for the project.

Fill it with all the information you consider may be needed.

*******************
Getting the library
*******************

.. raw:: html

   <p style="height:22px">
     <a href="https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}"
     alt="CWR-API Pypi package page">
       <img src="https://badge.fury.io/py/{{ cookiecutter.distribution_name }}.svg"/>
     </a>

     <a href="https://pypi.python.org/pypi/{{ cookiecutter.distribution_name }}"
     alt="CWR-API Pypi monthly downloads">
       <img src="https://img.shields.io/pypi/dm/{{ cookiecutter.distribution_name }}.svg"/>
     </a>
   </p>

The latest version of the library can always be found at Pypi. Additionally, the
code is on Github.

**************
Infrastructure
**************

Repositories
============

Github
------

.. raw:: html

   <p style="height:22px">
     <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
     alt="Github forks">
       <img src="https://img.shields.io/github/forks/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg"/>
     </a>

     <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
     alt="Github stars">
       <img src="https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg"/>
     </a>

     <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
     alt="Github license">
       <img src="https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg"/>
     </a>
   </p>

The code is being stored at GitHub.

ReadTheDocs
-----------

.. raw:: html

   <p style="height:22px">
     <a href="https://readthedocs.org/projects/{{ cookiecutter.repo_name }}"
     alt="Documentation status">
       <img src="https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest"/>
     </a>
   </p>

The documentation is stored at ReadTheDocs


Continuous integration and tests
================================

A small infrastructure is being used to check all the code being published
into the code repository.

Travis (CI)
-----------

.. raw:: html

   <p style="height:22px">
     <a href="https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
     alt="Travis CI">
       <img src="https://api.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg"/>
     </a>
   </p>

Travis is used for continuous integration. It checks the test after each build.

Coveralls (Coverage)
--------------------

.. raw:: html

   <p style="height:22px">
     <a href="https://coveralls.io/r/weso/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"
     alt="Coveralls coverage reports">
       <img src="https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.svg"/>
     </a>
   </p>

Coveralls generates coverage reports from the tests data received from Travis.

Landscape (Code health)
-----------------------

.. raw:: html

   <p style="height:22px">
     <a href="https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master"
     alt="Landscape code health">
       <img src="https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat"/>
     </a>
   </p>

Landscape checks commits to make code health reports.