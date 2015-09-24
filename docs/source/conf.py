#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Cookiecutter Python library documentation build configuration file.

import datetime

# -- General configuration ------------------------------------------------

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

# Templates.
templates_path = ['_templates']

# Only accepts reStructuredText
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Cookiecutter Python Library'
project_safe = project.replace(' ', '_')
copyright = u'%s, Bernardo Martínez Garrido' % datetime.datetime.now().year
authors = [u'Bernardo Martínez Garrido']

# The version info for the project.
#
# The short X.Y version.
version = '0.1.0'
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

import sphinx_docs_theme

# Activate the theme.
html_theme = 'sphinx_docs_theme'
html_theme_path = sphinx_docs_theme.get_html_theme_path()

# Removes permalink markers
html_add_permalinks = ''

# Theme options.
html_theme_options = {
    'keywords': 'Sphinx, theme, Bootstrap, documentation',
    'author_name': ','.join(authors),
    'author_url': 'https://github.com/Bernardo-MG',
    'twitter_id': '@wandrell',
    'publish_date': datetime.datetime.now().date(),
    'scm_name': 'Github',
    'scm_url': 'https://github.com/Bernardo-MG/cookiecutter-python-library',
    'ci_name': 'Travis',
    'ci_url': 'https://travis-ci.org/Bernardo-MG/cookiecutter-python-library',
    'issues_name': 'Github',
    'issues_url': 'https://github.com/Bernardo-MG/cookiecutter-python-library/issues',
    'supported_list': ['Python 2.6', 'Python 2.7', 'Python 3.2', 'Python 3.3',
                       'Python 3.4', 'pypy', 'pypy3'],
    'releases_repos': [],
    'general_info_links': [('Acquire', './acquire.html'),
                           ('Usage', './usage.html')],
    'navbar_links': [('Documentation', [('Acquire', './acquire.html'),
                                        ('Usage', './usage.html'),
                                        ('Tests',
                                         './tests.html'),
                                        ('Makefile',
                                         './makefile.html'),
                                        ('Doc site',
                                         './doc_site.html')])],
}

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
     ','.join(authors), project, 'Cookiecutter template for Python libraries.',
     'Miscellaneous'),
]


# -- Intersphinx links ----------------------------------------------------

# Intersphinx mapping.
intersphinx_mapping = {
    'https://docs.python.org/': None,
}
