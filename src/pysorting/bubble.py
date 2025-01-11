"""This module implements the bubble sort algorithm in python.Bubble sort is a basic algorithm
that sorts a list of data by comparing adjacent elements and swapping them if they are out of order
@author: Nonso Ebele-Muolokwu
"""

# import numpy as np


def bubble_sort(arr):
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    Parameters
    ----------
    arr : list
        A list of numeric values to be sorted.

    Returns
    -------
    list
        A sorted list in ascending order.

    Raises
    ------
    TypeError
        If the input is not a list.
    ValueError
        If the list contains non-numeric elements.

    Examples
    --------
    >>> bubble_sort([4, 2, 7, 1, 3])
    [1, 2, 3, 4, 7]

    >>> bubble_sort([10, -3, 0, 5, 9])
    [-3, 0, 5, 9, 10]
    """
