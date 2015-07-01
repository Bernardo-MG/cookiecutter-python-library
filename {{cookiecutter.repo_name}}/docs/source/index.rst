###############################
{{ cookiecutter.project_name }}
###############################

:Author: {{ cookiecutter.developer_name }}
:Copyright: {{ cookiecutter.developer_name }} {{ cookiecutter.year }}
:License: `MIT <http://www.opensource.org/licenses/mit-license.php>`_
:Interpreters: Python 2.6, 2.7, 3.2, 3.3, 3.4, Pypy, Pypy3, Jython

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

The library can be found at Pypi, making its installation it very easy::

    $ pip install {{ cookiecutter.package_name }}
	
Additionally, the latest version is always stored at `Github 
<https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}>`_

********
Contents
********

Contents:

.. toctree::
   :maxdepth: 2

   usage
