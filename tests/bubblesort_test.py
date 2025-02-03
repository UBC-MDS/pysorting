# tests/bubble_sort_test.py
import pytest
from pysorting import (
    bubble_sort,
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

def test_bubble_sort(test_data):
    """Test bubble sort with various inputs"""
    expected = sorted(test_data)
    actual = bubble_sort(test_data)

    assert isinstance(actual, list)
    assert actual == expected

def test_bubble_sort_reverse(test_data):
    """Test bubble sort with reverse sorting"""
    expected = sorted(test_data, reverse=True)
    actual = bubble_sort(test_data, ascending=False)

    assert isinstance(actual, list)
    assert actual == expected

def test_bubble_sort_invalid_element(test_data_invalid_element):
    """Test bubble sort with invalid element type"""
    with pytest.raises(NonUniformTypeError):
        bubble_sort(test_data_invalid_element)

def test_bubble_sort_non_uniform(test_data_non_uniform):
    """Test bubble sort with non-uniform element types"""
    with pytest.raises(NonUniformTypeError):
        bubble_sort(test_data_non_uniform)

def test_bubble_sort_invalid_ascending_type():
    """Test bubble sort with invalid ascending parameter type"""
    with pytest.raises(InvalidAscendingTypeError):
        bubble_sort([1, 2, 3], ascending="not_a_boolean")

def test_bubble_sort_error(test_data_error):
    """Test bubble sort with non-list input"""
    with pytest.raises(TypeError):
        bubble_sort(test_data_error)