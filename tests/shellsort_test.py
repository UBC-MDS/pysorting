# tests/shellsort_test.py
import pytest
from pysorting import (shell_sort, 
                       InvalidElementTypeError, 
                       NonUniformTypeError, 
                       InvalidAscendingTypeError)

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

def test_reverse_sorted_list(test_data1):
    """Test if a reverse sorting works properly."""
    expected = [8, 7, 6, 5, 4, 3, 2, 1]
    actual = shell_sort(test_data1, ascending=False)

    assert isinstance(actual, list)
    assert actual == expected


def test_unsorted_list(test_data1):
    """Test if an unsorted list is sorted correctly."""
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    actual = shell_sort(test_data1)

    assert isinstance(actual, list)
    assert actual == expected


def test_single_element_list(test_data_single_element):
    """Test if a single-element list is handled correctly."""
    expected = [5]
    actual = shell_sort(test_data_single_element, ascending=False)

    assert isinstance(actual, list)
    assert len(actual) == 1
    assert actual == expected


def test_empty_list(test_data_empty):
    """Test if an empty list is handled correctly."""

    actual = shell_sort(test_data_empty)

    assert isinstance(actual, list)
    assert len(actual) == 0


def test_type_error(test_data_error2):
    """Test if a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        shell_sort(test_data_error2)


def test_invalid_type_error(test_invalid_error):
    """Test if a TypeError is raised for non-list inputs."""
    with pytest.raises(InvalidElementTypeError):
        shell_sort(test_invalid_error)


def test_non_uniform_error(test_nonuniform_error):
    """Test if a TypeError is raised for non-list inputs."""
    with pytest.raises(NonUniformTypeError):
        shell_sort(test_nonuniform_error)


def test_invalid_ascending_type():
    """Test if InvalidAscendingTypeError is raised when ascending parameter is not a boolean."""
    with pytest.raises(InvalidAscendingTypeError):
        shell_sort([1, 2, 3], ascending="not_a_boolean")