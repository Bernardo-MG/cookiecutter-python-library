=====
Tests
=====

Projects created from the template come ready to run test suites, which include
not only unit tests, but also documentation validation and coverage reports.

---
tox
---

The new project will come ready to run most of the test suites through `tox`_.
This framework helps isolating and reproducing the test environment and is
completely compatible with `Travis CI`_ service, which is the recommended
way to run said tests.

~~~~~~~~~~~~~~~~
Tox environments
~~~~~~~~~~~~~~~~

If using tox this way there will be a series of Python interpreters ready to
be used, and all the tests will be run with each version, which include not
only various Python 2 and 3 releases, but also Pypy.

It is also possible to run the tests for a concrete release manually, but in
that case the correct Python interpreter should be installed locally.

Int that case the usual command can be used:

.. code-block:: sh

    $ tox -e env_name

Where 'env_name' is the Python version code, such as 'py27' for Python 2.7.

~~~~~~~~
Coverage
~~~~~~~~

The included '.coveragerc' file allows using `Coveralls`_ for generating
coverage reports.

This can be done through tox with the following command:

.. code-block:: sh

    $ tox -e coverage

This will generate and send the coverage information required for the report.
If the job is done with Travis, and the Travis configuration file included in
the project is prepared to create the coverage report, no additional
configuration is required.

Otherwise check the Coveralls page to find instructions in how to set up the
coverage process.

~~~~~~~~~~~~~~~~~~~~~~~~
Documentation validation
~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to validate the project's documentation with tox and the
following command:

.. code-block:: sh

    $ tox -e docs

This will run the Sphinx tests, and it is a good idea running it before
deploying the docs, a thing which the included Travis configuration file
already does.

~~~~~~~~~~~~~~~~
Style validation
~~~~~~~~~~~~~~~~

In a similar way to the documentation, the code's style can be validated. For
this the following tox command can be used:

.. code-block:: sh

    $ tox -e check

By default Travis won't run this environment, as it is too prone to failures.
It will check the readme, the manifest and all the code, making sure they
conform style standards.

---------------------------------------------
Adding tests for other Python implementations
---------------------------------------------

The tests are meant to be run with the help of Travis. But this service does not
offer all the existing Python implementations.

If for some reason one of these needs to be added Pyenv can be used, and an
example using Jython is included.

~~~~~~~~~~~~
Jython tests
~~~~~~~~~~~~

To run tests with the Jython implementation use the '.scripts/test_jython.sh' script.

Jython is installed using Pyenv and the tests will be run with the help of
pytests instead of tox.

.. _Coveralls: https://coveralls.io
.. _tox: https://testrun.org/tox/latest/
.. _Travis CI: travis-ci.org
