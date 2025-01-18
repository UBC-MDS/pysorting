from pysorting.bubble import bubble_sort
from pysorting.quicksort import quick_sort
# read version from installed package
from importlib.metadata import version

__version__ = version("pysorting")

from pysorting.bubblesort import bubble_sort
from pysorting.quicksort import quick_sort


from pysorting.utils import find_fastest_sorting_function, sorting_time
from .shell_sort import shell_sort

__version__ = version("pysorting")

