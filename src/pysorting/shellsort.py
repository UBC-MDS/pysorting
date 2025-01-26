"""
This module implements the Shell Sort algorithm in Python.

Shell Sort is a comparison-based sorting algorithm that generalizes the Shell Sort algorithm. 
It starts by sorting pairs of elements far apart from each other and then progressively reduces the gap 
between elements to be compared, ultimately achieving a sorted list.

@author: Siddarth Subrahmanian
"""

from .utils import (validate_list_elements, 
                    InvalidElementTypeError, 
                    NonUniformTypeError, 
                    InvalidAscendingTypeError)

def shell_sort(arr: list[float], ascending: bool = True) -> list[float]:
    """
    Sorts an array using the Shell Sort algorithm.

    Shell Sort repeatedly compares elements separated by a specific gap and rearranges them in the correct order.
    The gap is reduced over iterations until it becomes 1, at which point the list is fully sorted.
    The sorting order can be controlled using the `ascending` parameter.

    Parameters
    ----------
    arr : list[float]
        The array of numeric values to be sorted.
    ascending : bool, optional
        If `True` (default), sorts the array in ascending order. If `False`, sorts the array in descending order.

    Returns
    -------
    list[float]
        A sorted array in ascending order if `ascending=True`, or in descending order if `ascending=False`.

    Raises
    ------
    TypeError
        If the input is not a list.
    InvalidElementTypeError
        If the list contains non-numeric elements or string values.
    NonUniformTypeError
        If the list contains more than one form of data type.
    InvalidAscendingTypeError
        If the `ascending` parameter is not a boolean.

    Notes
    -----
    - Shell Sort is an improvement over Bubble Sort and Insertion Sort, with a time complexity of O(n^2) in the worst case.
    - This algorithm is more efficient than Bubble Sort for larger datasets.

    Examples
    --------
    Sorting in ascending order (default):
    >>> shell_sort([5, 2, 8, 3, 1])
    [1, 2, 3, 5, 8]

    Sorting in descending order:
    >>> shell_sort([3.5, 1.2, 2.8, 0.5], ascending=False)
    [3.5, 2.8, 1.2, 0.5]

    >>> shell_sort([1, 2, 3, 4, 5], ascending=True)
    [1, 2, 3, 4, 5]
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, (int, float, str)) for x in arr):
        raise InvalidElementTypeError()
    if not validate_list_elements(arr):
        raise NonUniformTypeError()
    if not isinstance(ascending, bool):
        raise InvalidAscendingTypeError()

    # Implementation of the Shell Sort algorithm
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and (
                (ascending and arr[j - gap] > temp) or (not ascending and arr[j - gap] < temp)
            ):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    print(f"Done sorting the array in {'ascending' if ascending else 'descending'} order.")
    return arr
