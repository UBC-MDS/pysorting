# tests/insertion_sort_test.py
import pytest
from pysorting import (
    insertion_sort,
    InvalidElementTypeError,
    NonUniformTypeError,
    InvalidAscendingTypeError,
)

# Define test cases as fixtures
@pytest.fixture(params=[
    [],  # empty array
    [1],  # single-element array
    [1, 2, 3, 4, 5, 6, 7, 8],  # already sorted array
    [8, 7, 6, 5, 4, 3, 2, 1],  # reverse-sorted array
    [5, 2, 8, 3, 1],  # unsorted array
    [1, 2, 3.0, 4, 5],  # array with floats
])
def test_data(request):
    return request.param

@pytest.fixture
def test_data_invalid_element():
    return [1, "a", 3]

@pytest.fixture
def test_data_non_uniform():
    return [1, 2, "3"]

@pytest.fixture
def test_data_error():
    return "not a list"

def test_insertion_sort(test_data):
    """Test insertion sort with various inputs"""
    expected = sorted(test_data)
    actual = insertion_sort(test_data)

    assert isinstance(actual, list)
    assert actual == expected

def test_insertion_sort_reverse(test_data):
    """Test insertion sort with reverse sorting"""
    expected = sorted(test_data, reverse=True)
    actual = insertion_sort(test_data, ascending=False)

    assert isinstance(actual, list)
    assert actual == expected

def test_insertion_sort_invalid_element(test_data_invalid_element):
    """Test insertion sort with invalid element type"""
    with pytest.raises(NonUniformTypeError):
        insertion_sort(test_data_invalid_element)

def test_insertion_sort_non_uniform(test_data_non_uniform):
    """Test insertion sort with non-uniform element types"""
    with pytest.raises(NonUniformTypeError):
        insertion_sort(test_data_non_uniform)

def test_insertion_sort_invalid_ascending_type():
    """Test insertion sort with invalid ascending parameter type"""
    with pytest.raises(InvalidAscendingTypeError):
        insertion_sort([1, 2, 3], ascending="not_a_boolean")

def test_insertion_sort_error(test_data_error):
    """Test insertion sort with non-list input"""
    with pytest.raises(TypeError):
        insertion_sort(test_data_error)