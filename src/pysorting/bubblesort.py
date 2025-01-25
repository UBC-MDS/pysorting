"""This module implements the bubble sort algorithm in python.Bubble sort is a basic algorithm
that sorts a list of data by comparing adjacent elements and swapping them if they are out of order
@author: Nonso Ebele-Muolokwu
"""

# import numpy as np
from .utils import validate_list_elements, InvalidElementTypeError, NonUniformTypeError


def bubble_sort(arr, ascending=True):
    """
    Sorts a list of numbers in ascending or descending order using the Bubble Sort algorithm.

    Bubble Sort repeatedly compares adjacent elements in the list and swaps them if they are in the wrong order.
    This process is repeated until the list is fully sorted. The sorting order can be controlled using the `ascending` parameter.

    Parameters:
    ----------
    arr : list
        The list of numeric values to be sorted.
    ascending : bool, optional
        If `True` (default), sorts the list in ascending order. If `False`, sorts the list in descending order.

    Returns:
    -------
    list
        The sorted list in ascending order if `ascending=True`, or in descending order if `ascending=False`.

    Raises:
    ------
    TypeError
        If the input is not a list.
    InvalidElementTypeError
        If the list contains non-numeric elementsor string values.
    NonUniformTypeError
        If the list contains more than one form of data type

    Notes:
    -----
    - Bubble Sort is a simple sorting algorithm with a time complexity of O(n^2) for average and worst cases.
    - This algorithm is inefficient for large datasets but can be used for educational purposes or small lists.
    - Sorting in descending order is achieved by reversing the comparison logic during the sorting process.

    Examples:
    --------
    Sorting in ascending order (default):
    >>> bubble_sort([4, 2, 7, 1, 3])
    [1, 2, 3, 4, 7]

    Sorting in descending order:
    >>> bubble_sort([4, 2, 7, 1, 3], ascending=False)
    [7, 4, 3, 2, 1]
    """
    if not all(isinstance(x, (int, float, str)) for x in arr):
        raise InvalidElementTypeError()

    if not validate_list_elements(arr):
        raise NonUniformTypeError()
    try:
        # Validate input type
        # if not isinstance(arr, list):
        #     raise TypeError("Input must be a list.")

        # # Validate list elements

        # Sorting logic
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if (ascending and arr[j] > arr[j + 1]) or (
                    not ascending and arr[j] < arr[j + 1]
                ):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                    swapped = True
            if not swapped:
                break

        print(f"Done sorting the array in order.")
        return arr

    except TypeError as te:
        raise TypeError("Your data should all be of the same type")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
