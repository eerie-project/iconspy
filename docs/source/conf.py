# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# from importlib.metadata import version, PackageNotFoundError
import importlib
from datetime import datetime

project = 'iconspy'

year = str(datetime.now().year)
copyright = f'{year}, Fraser William Goldsworth'

author = 'Fraser William Goldsworth'

try:
    release = importlib.metadata.version("iconspy")
except importlib.metadata.PackageNotFoundError:
    release = "0.0.0"  # fallback for local/dev usage

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',       # Extracts documentation from docstrings
    'sphinx.ext.napoleon',      # Supports Google- and NumPy-style docstrings
    'sphinx.ext.autosummary',   # Generates summary tables for modules/classes
    'sphinx_autodoc_typehints',  # Shows type hints in documentation
    'sphinx_copybutton',
    'nbsphinx',            # For Jupyter Notebook support
]

# Set the default theme
html_theme = "sphinx_rtd_theme"

# Specify paths for autodoc
import os
import sys
sys.path.insert(0, os.path.abspath(".."))  # Adjust path to include