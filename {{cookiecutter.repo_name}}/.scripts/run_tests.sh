#!/bin/bash
# This script runs the normal tests
# It will only run if none of the other tests environmental variables are set
#
# The Travis Python version is transformed and used to call the correct Tox environment

if [ -z "$DOCS" ] && [ -z "$COVERAGE" ] && [ -z "$JYTHON" ]; then

    tox -e $(echo py$TRAVIS_PYTHON_VERSION | tr -d . | sed -e 's/pypypy/pypy/')

fi
