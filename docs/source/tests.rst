=====
Tests
=====

Projects created from the template come ready to run test suites, which include
not only unit tests, but also documentation validation and coverage reports.

------------
Test command
------------

The project comes ready to run the tests with just a line:

.. code-block:: sh

    $ python setup.py test

Which allows using profiles:

.. code-block:: sh

    $ python setup.py test -p py36

Behind the scenes this will call and use tox.

---
tox
---

The new project will come ready to run most of the test suites through `tox`_.
This framework helps isolating and reproducing the test environment and is
completely compatible with `Travis CI`_ service, which is the recommended
way to run said tests.

~~~~~~~~~~~~~~~~
tox environments
~~~~~~~~~~~~~~~~

Travis offers several Python interpreters, which allow testing using different
test environments. The interpreters it has include not only various Python 2 and
3 releases, but also Pypy.

It is also possible to run the tests for a concrete release manually, but in
that case the correct Python interpreter should have been installed locally.

For that the usual command can be used:

.. code-block:: sh

    $ tox -e env_name

Where 'env_name' is the Python version code, such as 'py36' for Python 3.6.

--------
Coverage
--------

The included '.coveragerc' file allows using `Coveralls`_ for generating
coverage reports.

This can be done through tox with the following command:

.. code-block:: sh

    $ python setup.py test -p coverage

Which will generate and send the coverage information required for the report.
If the job is done with Travis, something the included Travis configuration
file already takes care of, no additional configuration is required.

Otherwise check the Coveralls page to find instructions in how to set up the
coverage process.

------------------------
Documentation validation
------------------------

It is possible to validate the project's documentation with tox and the
following command:

.. code-block:: sh

    $ python setup.py test -p docs

This will run the Sphinx tests, and it is a good idea running it before
deploying the docs, like the included Travis configuration file does.

----------------
Style validation
----------------

In a similar way to the documentation, the code's style can be validated. For
this the following tox command can be used:

.. code-block:: sh

    $ python setup.py test -p check

By default Travis won't run this environment, as it is too prone to failures.
It will check the readme, the manifest and all the code, making sure they
conform style standards.

.. _Coveralls: https://coveralls.io
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Travis CI: travis-ci.org
