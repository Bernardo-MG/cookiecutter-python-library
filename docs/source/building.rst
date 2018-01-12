====================
Building the project
====================

The new project will make use of `setuptools`_, and comes with a setup.py already set up.

--------
Commands
--------

The setup.py file comes ready for all the usual commands.

A few additional commands are added.

~~~~~
Tests
~~~~~

To run the tests:

.. code-block:: sh

    $ python setup.py test

Or running the tests using a profile:

.. code-block:: sh

    $ python setup.py test -p py36

~~~~
Docs
~~~~

To build the docs:

.. code-block:: sh

    $ python setup.py build_docs

.. _setuptools: https://github.com/pypa/setuptools
