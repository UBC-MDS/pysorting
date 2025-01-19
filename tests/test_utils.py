from pysorting import bubble_sort
from pysorting import find_fastest_sorting_function, sorting_time, is_sorted


def test_sorting_time():
    data = [5, 3, 8, 6, 2, 7, 4, 1]
    elapsed_time = sorting_time(bubble_sort, data)
    assert elapsed_time > 0  # Ensure the time taken is positive
    assert isinstance(elapsed_time, float)  # Ensure the returned value is a float


# Test find_fastest_sorting_function
def test_find_fastest_sorting_function():
    data = [5, 3, 8, 6, 2, 7, 4, 1]
    sorting_functions = [bubble_sort]
    fastest_func, fastest_time = find_fastest_sorting_function(sorting_functions, data)

    assert fastest_func in sorting_functions  # Ensure the fastest function is valid
    assert fastest_time > 0  # Ensure the time taken is positive
    assert isinstance(fastest_time, float)  # Ensure the returned time is a float


# Test is_sorted
def test_is_sorted():
    # Ascending order
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([5, 4, 3, 2, 1]) == False

    # Descending order
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True
    assert is_sorted([1, 2, 3, 4, 5], ascending=False) == False

    # Edge cases
    assert is_sorted([]) == True  # Empty list is sorted
    assert is_sorted([42]) == True  # Single-element list is sorted