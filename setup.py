# -*- coding: utf-8 -*-
import sys
import io
from codecs import open
from os.path import dirname
from os.path import join
from os import path

from setuptools import find_packages, setup
from setuptools.command.test import test as test_command

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Test requirements
_tests_require = ['tox']

# Path to the project's root
here = path.abspath(path.dirname(__file__))

# Gets the long description from the readme
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


class _ToxTester(test_command):
    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox

        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name='cookiecutter-python-library',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version='0.1.0',
    description='Cookiecutter template for Python libraries.',
    author='Bernardo Martínez Garrido',
    author_email='programming@wandrell.com',
    license='MIT',
    url='https://github.com/Bernardo-MG/cookiecutter-python-library',
    download_url='https://github.com/Bernardo-MG/cookiecutter-python-library',
    keywords=['cookiecutter', 'template', 'python'],
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'cookiecutter',
        'setuptools',
        'sphinx_bootstrap_theme',
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={'test': _ToxTester},
)
