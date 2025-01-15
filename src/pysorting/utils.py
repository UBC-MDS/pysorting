import time


def timer(func):
    """This function is used as a wrapper to time sorting function. It prints the time

    Parameters
    ----------
    func : _type_
        _description_
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
    Returns the time taken to sort a function.

    Parameters:
    - sorting_function: Sorting function to output the time taken to sort.
    - test_data: List to sort (same data will be passed to all functions).

    Returns:
    - A tuple (fastest_function, fastest_time).
    """
    wrapped_func = timer(sorting_function)

    _, elapsed_time = wrapped_func(data[:])

    return elapsed_time


def find_fastest_sorting_function(sorting_functions, data):
    """
    Finds the fastest sorting function based on execution time.

    Parameters:
    - sorting_functions: List of sorting functions to compare.
    - test_data: List to sort (same data will be passed to all functions).

    Returns:
    - A tuple (fastest_function, fastest_time).
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
    return fastest_function, fastest_time


def is_sorted(lst, ascending=True):
    """
    Checks if a list is sorted in ascending or descending order.

    Parameters:
    - lst (list): The list to check.
    - ascending (bool): If True, checks for ascending order; otherwise, descending.

    Returns:
    - bool: True if the list is sorted in the specified order, False otherwise.
    """
    if ascending:
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    else:
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
