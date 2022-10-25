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

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}
# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^v\d+\.\d+$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^main$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False