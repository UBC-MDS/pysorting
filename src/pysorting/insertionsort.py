"""This module implements the insertion sort algorithm in python. Insertion sort is a basic algorithm
that sorts a list of data by taking each element one by one, comparing it to the element to its left, 
swapping the value if it is larger, until it finds a smaller element. then it increments and begins again for the next element.
@author: Marek Boulerice
"""

from typing import List,Any

from .utils import (validate_list_elements, 
                    InvalidElementTypeError, 
                    NonUniformTypeError, 
                    InvalidAscendingTypeError)


def insertion_sort(arr, ascending = True):
    """
    Sorts a list of numbers in ascending or descending order using the Insertion Sort algorithm.
    
    This function takes in a single list as a parameter. It performs insertion sorting via the following algorithm:
        1. Begin with the second item in the list. 
        2. Compare the value of the item with the value of the item to its immediate left. 
        If the value is smaller than the item to its left, switch the position of the two items
        3. If If the value is larger than the item to its left, or if the item is in the first position of the list, stop. Otherwise repeat step 2.
        4. Repeat steps 2 and 3 for the next unchecked item, until all items have been checked
    After completing insertion sorting, function will return the newly sorted array
    
    Parameters
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
    - Insertion Sort is a simple sorting algorithm with a time complexity of O(n^2) for average and worst cases.
    - This algorithm is inefficient for large datasets but can be used for educational purposes or small lists.
    - Sorting in descending order is achieved by reversing the comparison logic during the sorting process.
    
    Examples:
    --------
    Sorting in ascending order (default):
    >>> insertion_sort([4, 2, 7, 1, 3])
    [1, 2, 3, 4, 7]

    Sorting in descending order:
    >>> insertion_sort([4, 2, 7, 1, 3], ascending=False)
    [7, 4, 3, 2, 1]
    """
    #check that input value is of correct type:
    # if not isinstance(unsorted, list):
    #     raise TypeError("Input value not a list")

    # #check that all values in list are numeric
    # if not all(isinstance(i, (int,float)) for i in unsorted):
    #     raise TypeError("All elements in input must be numeric")

    if not all(isinstance(x, (int, float, str)) for x in arr):
        raise InvalidElementTypeError()

    if not validate_list_elements(arr):
        raise NonUniformTypeError()
    
    if not isinstance(ascending, bool):
        raise InvalidAscendingTypeError()

    try:
        # Validate input type
        # if not isinstance(arr, list):
        #     raise TypeError("Input must be a list.")

        # # Validate list element
        # perform sorting algorthm
        n = len(arr)
        if ascending:
            for i in range(1,n):
                key = arr[i]
                j = i-1
                while j >= 0 and key < arr[j]:
                    arr[j+1] = arr[j]
                    arr[j] = key
                    j -= 1
        else:
            for i in range(1,n):
                key = arr[i]
                j = i-1
                while j >= 0 and key > arr[j]:
                    arr[j+1] = arr[j]
                    arr[j] = key
                    j -= 1

        print("Done sorting the array in order.")        
        return arr

    except TypeError as te:
        raise TypeError("Your data should all be of the same type")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
