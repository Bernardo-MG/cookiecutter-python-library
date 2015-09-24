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