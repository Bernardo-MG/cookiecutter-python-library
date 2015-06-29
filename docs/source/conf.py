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
            ('Github', 'https://github.com/Bernardo-MG/cookiecutter-python-library', True),
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
     ','.join(authors), project, 'Cookiecutter template for Python libraries.',
     'Miscellaneous'),
]


# -- Intersphinx links ----------------------------------------------------

# Intersphinx mapping.
intersphinx_mapping = {
    'https://docs.python.org/': None,
}
