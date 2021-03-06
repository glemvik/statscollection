# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config
# http://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import statscollection
import datetime

YEAR = datetime.datetime.utcnow().year

# -- Project information -----------------------------------------------------

project = "statscollection"
copyright = "2019 - {}, tommyod".format(YEAR)
author = "tommyod"

# The short X.Y version
version = statscollection.__version__

# The full version, including alpha/beta/rc tags
release = statscollection.__version__

# If true, the Docutils Smart Quotes transform will be used to convert quotes
# and dashes to typographically correct entities.  Default is True.
smartquotes = True

# A boolean that decides whether module names are prepended to all object names
# e.g. for py:function directives. Default is True.
add_module_names = True

# html_logo = "images/statscollection_logo.png"

html_favicon = "_static/favicon.ico"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx_gallery.gen_gallery",
]


# https://sphinx-gallery.readthedocs.io/en/latest/getting_started.html
sphinx_gallery_conf = {
    # Path to your examples scripts
    "examples_dirs": "../examples",
    # Path where to save gallery generated examples
    "gallery_dirs": "gallery_generated_examples",
    # Modules for which function level galleries are created
    # "doc_module": "statscollection",
    # Directory where function granular galleries are stored
    # "backreferences_dir": os.path.join("modules", "generated"),
    "reference_url": {"statscollection": None},
    "download_all_examples": False,
}


# http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#generating-stub-pages-automatically
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

html_show_sphinx = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_sidebars = {
    "**": [
        "globaltoc.html",
        #'sourcelink.html',
        # "searchbox.html",
    ],
    "using/windows": [
        # "windowssidebar.html",
        # "searchbox.html"
    ],
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "statscollectiondoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "statscollection.tex",
        "statscollection Documentation",
        "tommyod",
        "manual",
    )
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "statscollection", "statscollection Documentation", [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "statscollection",
        "statscollection Documentation",
        author,
        "statscollection",
        "One line description of project.",
        "Miscellaneous",
    )
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
# epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

html_theme_path = [os.path.join(os.path.abspath("."), "theme")]

html_theme = "guzzle_sphinx_theme"


# Register the theme as an extension to generate a sitemap.xml

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the left sidebar.
    "project_nav_name": "statscollection",
    # Path to a touch icon
    "touch_icon": "images/logos/statscollection_logo.png",
    #'extra_scripts': ['_static/css/gallery.css']
}


def setup(app):
    # to hide/show the prompt in code examples:
    app.add_javascript("js/copybutton.js")

    # This stylesheet overrides sphinx-gallery default styles
    app.add_stylesheet("css/gallery.css")
