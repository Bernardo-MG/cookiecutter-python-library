#####
Tests
#####

Tests are run through tox. Both the setup module and the Travis config file
make use of it for this purpose.

All of these tests are run with the help of nosetests.

****************
Tox environments
****************

Several environments are configured for this. Most of them are just for the
various interpreters, and need no additional description, but a few are
special cases.

In all of them, running the tests for a particular environment is done with
the usual command:

.. code-block:: sh
    $ tox -e env_name

Coverage
========

.. code-block:: sh
    $ tox -e coverage

The coverage environment runs the tests and then generates the coverage 
report. This will be set to `Coveralls <https://coveralls.io/>`_.
Luckily it is easy to integrate with Travis, and when running this
environment from there the report will be automatically sent with no
additional complication.

Documentation check
===================

.. code-block:: sh
    $ tox -e docs

This environment will validate the Sphinx tests. It is a good idea
running it before deploying the docs.

Various style checks
====================

.. code-block:: sh
    $ tox -e check

By default Travis won't run this environment, as it is too prone to failures.
It will check the readme, the manifest and all the code, to check they conform
style standards.

********************
Tests outside of Tox
********************

For technical reasons, not all tests could be added to Tox. These are still run
by Travis, but otherwise they have to be run manualle

Jython tests
============

To run tests with the Jython implementation use the '.scripts/test_jython.sh' script.

These tests will be run with the use of pytest.

Jython is installed using Pyenv.

Adding tests for other implementations
======================================

If for some reason tests are needed for other implementations of Python, Pyenv
can be used. Check the Jython script for this.
