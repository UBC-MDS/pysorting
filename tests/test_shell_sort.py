# tests/test_shell_sort.py

from pysorting.shell_sort import shell_sort
import pytest

# tests/test_shell_sort.py

def test_empty_array():
    """Test shell sort with an empty array"""
    assert shell_sort([]) == []

def test_single_element_array():
    """Test shell sort with a single-element array"""
    assert shell_sort([1]) == [1]

def test_already_sorted_array():
    """Test shell sort with an already sorted array"""
    assert shell_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unsorted_array():
    """Test shell sort with an unsorted array"""
    assert shell_sort([5, 2, 8, 3, 1]) == [1, 2, 3, 5, 8]

def test_array_with_duplicates():
    """Test shell sort with an array containing duplicates"""
    assert shell_sort([5, 2, 8, 3, 1, 2, 5]) == [1, 2, 2, 3, 5, 5, 8]

def test_array_with_negative_numbers():
    """Test shell sort with an array containing negative numbers"""
    assert shell_sort([5, -2, 8, -3, 1]) == [-3, -2, 1, 5, 8]