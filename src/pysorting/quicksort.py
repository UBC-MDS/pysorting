""" This module provides an implementation of the Quicksort algorithm, a popular 
sorting technique.
@author: Shashank
"""
from .utils import (validate_list_elements, 
                    InvalidElementTypeError, 
                    NonUniformTypeError, 
                    InvalidAscendingTypeError)

def quick_sort(arr, ascending=True):
    """
    Sorts a list of numbers in ascending or descending order using the Quick Sort algorithm.

    Quicksort is a divide-and-conquer algorithm that selects a "pivot" element 
    and partitions the array into two sub-arrays: one with elements smaller than 
    the pivot and one with elements greater than the pivot. It recursively sorts 
    the sub-arrays and combines them into a sorted array. The sorting order can 
    be controlled with the ascending parameter.

    Parameters:
    ----------
    arr : list
        The list of numeric values to be sorted.
    ascending : bool, optional
        If `True` (default), sorts the list in ascending order. If `False`, sorts the list in descending order.

    Returns:
    -------
    list
        The sorted array in ascending order if `reverse=False`, or in descending order if `reverse=True`.

    Raises:
    ------
    TypeError
        If the input is not a list.
    InvalidElementTypeError
        If the list contains non-comparable elements.
    NonUniformTypeError
        If the list contains more than one form of data type.

    Notes:
    -----
    - This function operates in-place, modifying the input `arr` directly.
    - The average time complexity is O(n log n), while the worst-case complexity is O(n^2), 
      which occurs when the pivot selection results in highly unbalanced partitions.
    - Sorting in descending order is achieved by reversing the comparison logic during partitioning.

    Examples:
    --------
    Sorting in ascending order (default):
    >>> quick_sort([4, 2, 7, 1, 3])
    [1, 2, 3, 4, 7]

    Sorting in descending order:
    >>> quick_sort([4, 2, 7, 1, 3], reverse=True)
    [7, 4, 3, 2, 1]
    """
    # Validate input type
    if not all(isinstance(x, (int, float, str)) for x in arr):
        raise InvalidElementTypeError()
    
    if not validate_list_elements(arr):
        raise NonUniformTypeError()
    
    if not isinstance(ascending, bool):
        raise InvalidAscendingTypeError()
    
    # If the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    if not ascending:  # Sort in descending order
        left = [x for x in arr[1:] if x > pivot]
        right = [x for x in arr[1:] if x <= pivot]
    else:  # Sort in ascending order
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]

    # Recursively sort left and right partitions
    return quick_sort(left, ascending) + [pivot] + quick_sort(right, ascending)