from importlib.metadata import version

__version__ = version("pysorting")

from pysorting.bubblesort import bubble_sort
from pysorting.quicksort import quick_sort
from pysorting.shellsort import shell_sort
from pysorting.insertionsort import insertion_sort

from pysorting.utils import (
    InvalidElementTypeError,
    NonUniformTypeError,
    InvalidAscendingTypeError,
    find_fastest_sorting_function, 
    sorting_time, 
    is_sorted
)

__version__ = version("pysorting")