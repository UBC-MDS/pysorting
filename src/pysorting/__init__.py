# read version from installed package
from importlib.metadata import version

__version__ = version("pysorting")

from pysorting.bubble import bubble_sort
