""" This module provides an implementation of the Quicksort algorithm, a popular 
sorting technique.
@author: Shashank
"""
def quick_sort(arr, reverse=False):
    """
    Sorts an array using the Quicksort algorithm.

    Quicksort is a divide-and-conquer algorithm that selects a "pivot" element 
    and partitions the array into two sub-arrays: one with elements smaller than 
    the pivot and one with elements greater than the pivot. It recursively sorts 
    the sub-arrays and combines them into a sorted array. The sorting order can 
    be controlled with the `reverse` parameter.

    Parameters:
    ----------
    arr : list
        The list of elements to be sorted. This can contain any comparable types.
    reverse : bool, optional
        If `True`, sorts the array in descending order. If `False` (default), sorts the array in ascending order.

    Returns:
    -------
    list
        The sorted array in ascending order if `reverse=False`, or in descending order if `reverse=True`.

    Notes:
    -----
    - This function operates in-place, modifying the input `arr` directly.
    - The average time complexity is O(n log n), while the worst-case complexity is O(n^2), 
      which occurs when the pivot selection results in highly unbalanced partitions.
    - Sorting in descending order is achieved by reversing the comparison logic during partitioning.

    Examples:
    --------
    Sorting in ascending order (default):
    >>> arr = [4, 2, 7, 1, 3]
    >>> quick_sort(arr)
    [1, 2, 3, 4, 7]

    Sorting in descending order:
    >>> arr = [4, 2, 7, 1, 3]
    >>> quick_sort(arr, reverse=True)
    [7, 4, 3, 2, 1]
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if not isinstance(reverse, bool):
        raise TypeError("'reverse' must be a boolean value.")
    
    # If the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Validate that all elements in the list are comparable
    for i in range(len(arr) - 1):
        try:
            _ = arr[i] < arr[i + 1]  # Check if elements are comparable
        except TypeError:
            raise ValueError("All elements in the list must be comparable.")
        
        pivot = arr[0]
        if reverse:  # Sort in descending order
            left = [x for x in arr[1:] if x > pivot]
            right = [x for x in arr[1:] if x <= pivot]
        else:  # Sort in ascending order
            left = [x for x in arr[1:] if x < pivot]
            right = [x for x in arr[1:] if x >= pivot]

        # Recursively sort left and right partitions
        return quick_sort(left, reverse) + [pivot] + quick_sort(right, reverse)