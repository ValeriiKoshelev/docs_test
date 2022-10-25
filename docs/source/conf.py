import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "backhoe_perception_simulator"
author = "Valerii Koshelev"
copyright = '2022, DeepX, Inc.'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx_tabs.tabs',
    'sphinx.ext.autosummary',
    'sphinx_rtd_theme',
    'sphinx_multiversion',
    'sphinx_mdinclude'
]

html_theme = 'sphinx_rtd_theme'

templates_path = [
    "templates",
]


smv_remote_whitelist = r"^origin$"
smv_branch_whitelist = r"^main"
