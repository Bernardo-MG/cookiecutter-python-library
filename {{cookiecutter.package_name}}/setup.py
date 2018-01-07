# -*- coding: utf-8 -*-
import ast
import re
import sys
import io
from os.path import dirname
from os.path import join
from codecs import open

from setuptools import find_packages, setup
from setuptools.command.test import test as test_command

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Source package
_source_package = '{{ cookiecutter.package_name }}'

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


# Gets the version for the source folder __init__.py file
with open(_source_package + '/__init__.py', 'rb',
          encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))


class _ToxTester(test_command):
    """
    Tox test command.

    Calls tox for running the tests.
    """
    user_options = [
        ('test-module=', 'm', "Run 'test_suite' in specified module"),
        ('test-suite=', 's',
         "Run single test, case or suite (e.g. 'module.test_suite')"),
        ('test-runner=', 'r', "Test runner to use"),
        ('profile=', 'p', 'Test profile to use')
    ]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.profile = None

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []

        if self.profile is not None:
            # Adds the profile argument
            # For example: '-e=py36'
            self.test_args.append('-e=' + self.profile)

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox

        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name='{{ cookiecutter.package_name }}',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=version_lib,
    description={{'{0!r}'.format(cookiecutter.project_short_description).lstrip('ub')}},
    author={{'{0!r}'.format(cookiecutter.developer_name).lstrip('ub')}},
    author_email={{'{0!r}'.format(cookiecutter.developer_email).lstrip('ub')}},
    license='MIT',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}',
    download_url='https://pypi.python.org/pypi/{{ cookiecutter.package_name }}',
    keywords=[],
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    long_description=read('README.rst'),
    install_requires=[
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={'test': _ToxTester},
)
