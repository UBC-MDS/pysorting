import pytest
from pysorting import quick_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert quick_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element."""
    assert quick_sort([1]) == [1]

def test_sorted_list():
    """Test sorting an already sorted list."""
    assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_reverse_sorted_list():
    """Test sorting a reverse-sorted list."""
    assert quick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_unsorted_list():
    """Test sorting an unsorted list."""
    assert quick_sort([3, 1, 4, 2]) == [1, 2, 3, 4]

def test_duplicates():
    """Test sorting a list with duplicate elements."""
    assert quick_sort([4, 2, 4, 1]) == [1, 2, 4, 4]

def test_reverse_sorting():
    """Test sorting a list in descending order."""
    assert quick_sort([3, 1, 4, 2], reverse=True) == [4, 3, 2, 1]
