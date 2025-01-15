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
    try:
        # Validate input type
        # if not isinstance(arr, (list,np.ndarray)):
        if not isinstance(arr, list):
            raise TypeError("Input must be a list.")

        # Validate list elements
        if not all(isinstance(x, (int, float, str)) for x in arr):
            raise ValueError("All elements in the list must be numeric or be a string.")

        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                    swapped = True
            if not swapped:
                break
        print("Done sorting the array")
        return arr

    except TypeError as te:
        raise (f"Some or all of the values in the list are not accepted")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def bubble_sort(arr, ascending=True):
    """
    Sorts a list of numbers in ascending or descending order using the Bubble Sort algorithm.

    Parameters
    ----------
    arr : list
        A list of numeric values to be sorted.
    ascending : bool, optional
        The order of sorting: True for "ascending" (default) or False for "descending".

    Returns
    -------
    list
        A sorted list in the specified order.

    Raises
    ------
    TypeError
        If the input is not a list.
    ValueError
        If the list contains non-numeric elements or an invalid order is specified.

    Examples
    --------
    >>> bubble_sort([4, 2, 7, 1, 3])
    [1, 2, 3, 4, 7]

    >>> bubble_sort([10, -3, 0, 5, 9], order="descending")
    [10, 9, 5, 0, -3]
    """
    try:
        # Validate input type
        if not isinstance(arr, list):
            raise TypeError("Input must be a list.")

        # Validate list elements
        if not all(isinstance(x, (int, float, str)) for x in arr):
            raise ValueError("All elements in the list must be numeric or a string.")

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
        raise TypeError(te)
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")