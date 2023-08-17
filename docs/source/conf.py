# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
# other statements
this_dir = os.path.dirname(os.path.abspath(__file__)) 
matlab_src_dir = os.path.abspath(os.path.join(this_dir, '..')) 
project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinxcontrib.matlab',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- primary domain
primary_domain = "mat"

this_dir = os.path.dirname(os.path.abspath(__file__)) matlab_src_dir = os.path.abspath(os.path.join(this_dir, '..')) 
