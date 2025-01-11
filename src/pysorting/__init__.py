# read version from installed package
from importlib.metadata import version
__version__ = version("pysorting")

from pysorting.quicksort import quick_sort