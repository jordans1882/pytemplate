"""
pytemplate
=====

A simple template Python library. Contains some routings for linear algebra and statistics

Provides:
    - A matrix class

"""

__name__ = "pytemplate"
from ._version import __version__


# __all__ = [
#     '__version__'
#     ]

from .template import Template
from .matrix import Matrix
