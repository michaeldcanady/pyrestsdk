# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PyRESTSDK"
copyright = "2023, michaeldcanady"
author = "michaeldcanady"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "sphinx.ext.autosummary", 'autoapi.extension']

autosummary_generate = True

autoapi_type = 'python'

autoapi_dirs = ['../pyrestsdk']

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
    # :inherited-members: seems to get applied to all autoXXX directives, not
    # just autoclass? Need to use :no-inherited-members: in all automodule
    # directives, else all module content (classes, functions, ...) end up on a
    # single page. We do that in https://github.com/elcorto/sphinx-autodoc .
    "inherited-members": True,
    "no-special-members": True,
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "press"
html_static_path = ["_static"]
