============
The makefile
============

A makefile, and an equivalent make.bat file for windows, is offered as an easy
way to control the project's flow.

It is possible to get all the available tasks with the command:

.. code-block:: sh

    $ make help

But there is a small summary:

============  ===========
Command       Description
============  ===========
clean         Removes all the generated and distribution files
build         Creates the source distribution
install       Installs the project in the local repository
requirements  Installs the project requirements
register      Registers the project into Pypi
deploy        Deploys the project into Pypi
test          Runs the tox tests suite
============  ===========

-------------
Pypi commands
-------------

`Pypi`_ requires access information. Otherwise the commands making use of this
service won't work.

For this a '.pypirc' file should be on the user folder, with the following data:

.. code-block:: text

    [distutils]
    index-servers =
        pypi
        pypitest

    [pypi]
    username: username_pypi
    password: password_pypi

    [pypitest]
    repository: https://testpypi.python.org/pypi
    username: username_pypitest
    password: password_pypitest

Where the usernames and passwords should be changed for the correct ones.

----------
Deployment
----------

Deployment is made with `Twine`_, to make sure old versions of Python use HTTPS
when deploying.

.. _Pypi: https://pypi.python.org
.. _Twine: https://pypi.python.org/pypi/twine
