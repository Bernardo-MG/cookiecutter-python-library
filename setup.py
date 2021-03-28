# -*- coding: utf-8 -*-
import io
from os.path import dirname
from os.path import join

from setuptools import find_packages, setup
from sphinx.setup_command import BuildDoc
from tox_test_command import ToxTestCommand

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='cookiecutter-python-library',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version='0.2.0',
    description='Cookiecutter template for Python libraries.',
    author='Bernardo Martínez Garrido',
    author_email='programming@bernardomg.com',
    license='MIT',
    url='https://github.com/Bernardo-MG/cookiecutter-python-library',
    download_url='https://github.com/Bernardo-MG/cookiecutter-python-library',
    keywords=['cookiecutter', 'template', 'python'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'cookiecutter'
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={
        'build_docs': BuildDoc,
        'test': ToxTestCommand
    },
)
