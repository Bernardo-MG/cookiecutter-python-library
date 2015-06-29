#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# {{ cookiecutter.project_name }} documentation build configuration file.

import ast
import re
import sys
import os
from codecs import open
from os import path

# -- Version --------------------------------------------------------------

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Path to the project's root
here = path.abspath(path.dirname(__file__))

# Gets the version for the source folder __init__.py file
with open('../../{{ cookiecutter.package_name }}/__init__.py', 'rb', encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))

# -- Code location --------------------------------------------------------

sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('../../{{ cookiecutter.package_name }}'))


# -- General configuration ------------------------------------------------

# Sphinx extensions
#
# autodoc: generates documentation from docstrings
# intersphinx: generates links to other Sphinx-created docs
# viewcode: generates HTML from code sources
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# Templates.
templates_path = ['_templates']

# Only reStructuredText is accepted
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Sort members by type
autodoc_member_order = 'groupwise'

# General information about the project.
project = '{{ cookiecutter.project_name }}'
project_safe = project.replace(' ', '_')
copyright = u'{{ cookiecutter.year }}, {{ cookiecutter.developer_name }}'
authors = [u'{{ cookiecutter.developer_name }}']

# The version info for the project.
#
# Semantic version value.
version = version_lib
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

try:
    import sphinx_bootstrap_theme
except:
    from warnings import warn

    warn("I would like to use the sphinx bootstrap theme, but can't find it.\n"
         "'pip install sphinx_bootstrap_theme' to fix.")
else:
    # Activate the theme.
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

    # Theme options.
    html_theme_options = {
        'navbar_fixed_top': 'true',
        'navbar_site_name': 'Contents',
        'bootstrap_version': '3',
        'source_link_position': 'footer',
        'bootswatch_theme': 'yeti',
        'navbar_links': [
            ('Github', 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}', True),
        ],
    }

# Custom sidebars
html_sidebars = {'index': ['status.html']}

# Output file base name for HTML help builder.
htmlhelp_basename = '%s doc' % project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# List of LaTeX documents.
latex_documents = [
    (master_doc, '%s.tex' % project_safe, '%s Documentation' % project,
     ','.join(authors), 'manual'),
]


# -- Options for manual page output ---------------------------------------

# List of manual pages.
man_pages = [
    (master_doc, project, '%s Documentation' % project,
     [','.join(authors)], 1)
]


# -- Options for Texinfo output -------------------------------------------

# List of Texinfo documents.
texinfo_documents = [
    (master_doc, project, '%s Documentation' % project,
     ','.join(authors), project, '{{ cookiecutter.project_short_description }}',
     'Miscellaneous'),
]


# -- Intersphinx links ----------------------------------------------------

# Intersphinx mapping.
intersphinx_mapping = {
    'https://docs.python.org/': None,
}
