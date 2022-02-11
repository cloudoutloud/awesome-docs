# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'awesome-docs'
copyright = '2020, cloudoutloud'
author = 'Sean Rigby'

# The full version, including alpha/beta/rc tags
release = os.environ.get('DOCS_VERSION', 'Unknown')
version = 'Version: ' + os.environ.get('DOCS_VERSION', 'Unknown')

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.confluencebuilder',
    'pyquickhelper.sphinxext.sphinx_runpython_extension',
    'sphinx-jsonschema'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/icon.png'

html_theme_options = {
  'logo_only': True,
  'display_version': True,
  'navigation_depth': 6
}

# -- Extensions -------------------------------------------------

# Custom styling
def setup(app):
  app.add_css_file('style.css')
  app.add_js_file("custom.js")
  app.add_js_file("clipboard.js")

# Todos extension
todo_include_todos = True

# Label extension
autosectionlabel_prefix_document = True

# Confluence extension
confluence_publish = True
confluence_master_homepage = False
confluence_purge = False
confluence_max_doc_depth = 5
confluence_page_hierarchy = True
confluence_space_name = 'CNE'
confluence_parent_page = 'SRE'
confluence_publish_postfix = ' [azdo]'

confluence_server_url =  os.environ.get('CONFLUENCE_SERVER_URL')
confluence_server_user = os.environ.get('CONFLUENCE_SERVER_USER')
confluence_server_pass = os.environ.get('CONFLUENCE_SERVER_PASS')

# # https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/configuration.html#confluence-server-auth
# from requests_oauthlib import OAuth1

# client_key = ''
# client_secret = ''
# resource_owner_key = ''
# resource_owner_secret = ''

# confluence_server_auth = OAuth1(client_key,
#     client_secret=client_secret,
#     resource_owner_key=resource_owner_key,
#     resource_owner_secret=resource_owner_secret)
