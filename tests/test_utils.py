# tests/sorting_utils_test.py
import pytest
from pysorting import (
    bubble_sort,
    insertion_sort,
    shell_sort,
    find_fastest_sorting_function,
    sorting_time,
    is_sorted,
)


def test_sorting_time():
    """Test sorting time calculation"""
    data = [5, 3, 8, 6, 2, 7, 4, 1]
    elapsed_time = sorting_time(bubble_sort, data)

    assert elapsed_time > 0  # Ensure the time taken is positive
    assert isinstance(elapsed_time, float)  # Ensure the returned value is a float


@pytest.mark.parametrize("sorting_functions", [[shell_sort, bubble_sort, insertion_sort]])
def test_find_fastest_sorting_function(sorting_functions):
    """Test finding the fastest sorting function"""
    data = [5, 3, 8, 6, 2, 7, 4, 1]
    fastest_func, fastest_time = find_fastest_sorting_function(data, *sorting_functions)

    assert fastest_func in sorting_functions  # Ensure the fastest function is valid
    assert fastest_time > 0  # Ensure the time taken is positive
    assert isinstance(fastest_time, float)  # Ensure the returned time is a float


@pytest.mark.parametrize(
    "data, ascending, expected",
    [
        ([1, 2, 3, 4, 5], True, True),  # Ascending order
        ([5, 4, 3, 2, 1], True, False),  # Descending order
        ([5, 4, 3, 2, 1], False, True),  # Descending order
        ([1, 2, 3, 4, 5], False, False),  # Ascending order
        ([], True, True),  # Empty list is sorted
        ([42], True, True),  # Single-element list is sorted
    ],
)
def test_is_sorted(data, ascending, expected):
    """Test if a list is sorted"""
    assert is_sorted(data, ascending=ascending) == expected