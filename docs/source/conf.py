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
master_doc = 'contents'

# General information about the project.
project = '{{ cookiecutter.project_name }}'
copyright = u'%s, {{ cookiecutter.developer_name }}' % datetime.datetime.now().year
authors = ['{{ cookiecutter.developer_name }}']

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
        "navbar_fixed_top": "true",
        "navbar_site_name": "Contents",
        'bootstrap_version': '3',
        'source_link_position': 'footer',
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = '{{ cookiecutter.project_name }} doc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '{{ cookiecutter.project_name }}.tex',
     '{{ cookiecutter.project_name }} Documentation',
     ','.join(authors), 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, '{{ cookiecutter.distribution_name }}',
     '{{ cookiecutter.project_name }} Documentation',
     [','.join(authors)], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, '{{ cookiecutter.project_name }}',
     '{{ cookiecutter.project_name }} Documentation',
     ','.join(authors), '{{ cookiecutter.project_name }}',
     '{{ cookiecutter.project_short_description }}',
     'Miscellaneous'),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
