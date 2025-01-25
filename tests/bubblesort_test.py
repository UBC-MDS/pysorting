import pytest
from pysorting import (bubble_sort, 
                       InvalidElementTypeError, 
                       NonUniformTypeError, 
                       InvalidAscendingTypeError)


def test_sorted_list(test_data_sorted):
    """Test if a pre-sorted list remains unchanged."""
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    actual = bubble_sort(test_data_sorted)

    assert isinstance(actual, list)
    assert actual == expected


def test_reverse_sorted_list(test_data1):
    """Test if a reverse sorting works properly."""
    expected = [8, 7, 6, 5, 4, 3, 2, 1]
    actual = bubble_sort(test_data1, ascending=False)

    assert isinstance(actual, list)
    assert actual == expected


def test_unsorted_list(test_data1):
    """Test if an unsorted list is sorted correctly."""
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    actual = bubble_sort(test_data1)

    assert isinstance(actual, list)
    assert actual == expected


def test_single_element_list(test_data_single_element):
    """Test if a single-element list is handled correctly."""
    expected = [5]
    actual = bubble_sort(test_data_single_element, ascending=False)

    assert isinstance(actual, list)
    assert len(actual) == 1
    assert actual == expected


def test_empty_list(test_data_empty):
    """Test if an empty list is handled correctly."""

    actual = bubble_sort(test_data_empty)

    assert isinstance(actual, list)
    assert len(actual) == 0


def test_type_error(test_data_error2):
    """Test if a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        bubble_sort(test_data_error2)


def test_invalid_type_error(test_invalid_error):
    """Test if a TypeError is raised for non-list inputs."""
    with pytest.raises(InvalidElementTypeError):
        bubble_sort(test_invalid_error)


def test_non_uniform_error(test_nonuniform_error):
    """Test if a TypeError is raised for non-list inputs."""
    with pytest.raises(NonUniformTypeError):
        bubble_sort(test_nonuniform_error)


def test_invalid_ascending_type():
    """Test if InvalidAscendingTypeError is raised when ascending parameter is not a boolean."""
    with pytest.raises(InvalidAscendingTypeError):
        bubble_sort([1, 2, 3], ascending="not_a_boolean")