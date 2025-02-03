import time
from tabulate import tabulate


class InvalidElementTypeError(Exception):
    """Custom exception raised when elements are not strings or lists of strings."""

    def __init__(
        self, message="All elements must be either a string or a list of strings."
    ):
        self.message = message
        super().__init__(self.message)


class NonUniformTypeError(Exception):
    """Custom exception raised when elements are not strings or lists of strings."""

    def __init__(self, message="Elements are not of the same type."):
        self.message = message
        super().__init__(self.message)


class InvalidAscendingTypeError(Exception):
    """Custom exception raised when 'ascending' is not a boolean."""

    def __init__(self, message="The parameter 'ascending' must be a boolean value."):
        self.message = message
        super().__init__(self.message)


def timer(func):
    """
    A decorator function that measures and prints the execution time of a given function.

    This decorator records the start and end time of the function execution, calculates the elapsed time,
    and prints the time taken in seconds. The result of the wrapped function along with the execution time
    is returned.

    Parameters:
    ----------
    func : function
        The function whose execution time is to be measured.

    Returns:
    -------
    function
        A wrapper function that executes the given function and measures its execution time.

    Notes:
    -----
    - The execution time is measured using the `time` module.
    - The function returns both the result of the original function and the time taken for execution.
    - This decorator can be used to evaluate the performance of sorting algorithms and other time-sensitive functions.

    Examples:
    --------
    Using the `timer` decorator on a sorting function:

    >>> @timer
    ... def sample_sort(arr):
    ...     return sorted(arr)

    >>> sample_sort([5, 2, 8, 1, 3])
    Function 'sample_sort' executed in 0.000002 seconds.
    ([1, 2, 3, 5, 8], 2e-06)
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds.")
        return result, elapsed_time  # Return the result and the time taken

    return wrapper


def sorting_time(sorting_function, data):
    """
    Measures the execution time of a given sorting function.

    This function wraps the specified sorting function using the `timer` decorator
    to measure how long it takes to sort the provided dataset.

    Parameters:
    ----------
    sorting_function : function
        The sorting function whose execution time needs to be measured. It should accept a list as input
        and return a sorted list.
    data : list
        The list of values to be sorted. A copy of this list is passed to the sorting function
        to prevent modification of the original data.

    Returns:
    -------
    float
        The execution time (in seconds) of the sorting function.

    Notes:
    -----
    - The function uses the `timer` decorator to record execution time.
    - A copy of the input data is passed to the sorting function to avoid side effects.
    - Useful for benchmarking different sorting algorithms.

    Examples:
    --------
    Measuring the execution time of a sorting function:

    >>> test_data = [5, 2, 8, 1, 3]
    >>> sorting_time(quick_sort, test_data)
    Function 'quick_sort' executed in 0.000002 seconds.
    0.0000024567
    """
    wrapped_func = timer(sorting_function)

    _, elapsed_time = wrapped_func(data[:])

    return elapsed_time


def find_fastest_sorting_function(data, *sorting_functions):
    """
    Determines the fastest sorting function by measuring execution time.

    This function tests multiple sorting functions on the same dataset, measures their execution times,
    and identifies the fastest one. The execution times for all sorting functions are displayed in a formatted table.

    Parameters:
    ----------
    data : list
        The list of values to be sorted. A copy of this list is passed to each sorting function
        to ensure that the original data remains unmodified.
    sorting_functions : tuple of functions
        A variable number of sorting functions to be tested. Each function should accept a list as input
        and return a sorted list.

    Returns:
    -------
    tuple
        A tuple containing:
        - `fastest_function` (function): The sorting function with the shortest execution time.
        - `fastest_time` (float): The execution time (in seconds) of the fastest function.

    Notes:
    -----
    - Each sorting function is wrapped using the `timer` decorator to measure execution time.
    - The execution times of all tested functions are displayed in a table format using `tabulate`.
    - The function automatically selects the sorting function with the minimum execution time.

    Examples:
    --------
    Comparing multiple sorting functions:

    >>> test_data = [5, 2, 8, 1, 3]
    >>> fastest_function, fastest_time = find_fastest_sorting_function(test_data, bubble_sort, quick_sort)
    ┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
    ┃ Function      ┃ Time taken (s)  ┃
    ┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
    ├ bubble_sort   │ 0.0000253456    │
    ├ quick_sort    │ 0.0000024567    │
    └───────────────┴────────────────┘
    >>> print(f"The fastest function is {fastest_function.__name__} with a time of {fastest_time:.6f} seconds.")
    The fastest function is quick_sort with a time of 0.000002 seconds.
    """
    results = []

    for func in sorting_functions:
        # Wrap the function with the timer
        wrapped_func = timer(func)
        _, elapsed_time = wrapped_func(
            data[:]
        )  # Pass a copy of the data to avoid side effects
        results.append((func, elapsed_time))

    # Find the function with the minimum elapsed time
    fastest_function, fastest_time = min(results, key=lambda x: x[1])

    list_dict = {
        "Function": [x[0].__name__ for x in results],
        "Time take": [f"{x[1]:.10f}" for x in results],
    }
    print(tabulate(list_dict, headers="keys", tablefmt="fancy_grid"))

    return fastest_function, fastest_time


def is_sorted(lst, ascending=True):
    """
    Determines whether a list is sorted in ascending or descending order.

    This function checks if the elements in the list are in non-decreasing (ascending)
    or non-increasing (descending) order, based on the `ascending` parameter.

    Parameters:
    ----------
    lst : list
        The list of elements to check. The function assumes the elements are comparable.
    ascending : bool, optional
        If `True` (default), checks whether the list is sorted in ascending order.
        If `False`, checks whether the list is sorted in descending order.

    Returns:
    -------
    bool
        `True` if the list is sorted in the specified order, `False` otherwise.

    Raises:
    ------
    TypeError
        If the list contains elements that cannot be compared.

    Notes:
    -----
    - An empty list or a list with a single element is considered sorted.
    - The function performs a pairwise comparison to verify sorting order.

    Examples:
    --------
    Checking if a list is sorted in ascending order (default):

    >>> is_sorted([1, 2, 3, 4, 5])
    True

    Checking if a list is sorted in descending order:

    >>> is_sorted([5, 4, 3, 2, 1], ascending=False)
    True

    Checking an unsorted list:

    >>> is_sorted([1, 3, 2, 4, 5])
    False
    """
    if ascending:
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    else:
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


def validate_list_elements(elements):
    """
    Validates whether all elements in a list are of the same type: either all numerical (int or float)
    or all strings.

    This function checks if a given list contains only numeric values (`int` or `float`)
    or only string values. If the list contains mixed data types, it is considered invalid.

    Parameters:
    ----------
    elements : list
        The list of elements to validate.

    Returns:
    -------
    bool
        `True` if all elements in the list are either numerical (integers or floats) or all strings.
        `False` if the list contains mixed data types.

    Raises:
    ------
    TypeError
        If the input is not a list.

    Notes:
    -----
    - An empty list is considered valid.
    - The function does not check for `None` values explicitly.
    - Useful for data validation in sorting, filtering, or numerical operations.

    Examples:
    --------
    Checking a valid list with numbers:

    >>> validate_list_elements([1, 2, 3, 4.5])
    True

    Checking a valid list with strings:

    >>> validate_list_elements(["apple", "banana", "cherry"])
    True

    Checking an invalid list with mixed types:

    >>> validate_list_elements([1, "banana", 3.5])
    False

    Checking an empty list:

    >>> validate_list_elements([])
    True
    """
    if all(isinstance(e, (int, float)) for e in elements):
        return True  # All elements are numerical
    elif all(isinstance(e, str) for e in elements):
        return True  # All elements are strings
    else:
        return False
