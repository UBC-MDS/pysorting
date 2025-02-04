# tests/quick_sort_test.py
import pytest
from pysorting import quick_sort, InvalidElementTypeError, NonUniformTypeError, InvalidAscendingTypeError

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
def test_data_large_sorted():
    return list(range(1, 101))

@pytest.fixture
def test_data_large_unsorted():
    return list(range(1, 101))[::-1]

def test_quick_sort(test_data):
    """Test quick sort with various inputs"""
    expected = sorted(test_data)
    actual = quick_sort(test_data)

    assert isinstance(actual, list)
    assert actual == expected

def test_quick_sort_reverse(test_data):
    """Test quick sort with reverse sorting"""
    expected = sorted(test_data, reverse=True)
    actual = quick_sort(test_data, ascending=False)

    assert isinstance(actual, list)
    assert actual == expected

def test_quick_sort_invalid_element(test_data_invalid_element):
    """Test quick sort with invalid element type"""
    with pytest.raises(NonUniformTypeError):
        quick_sort(test_data_invalid_element)

def test_quick_sort_non_uniform(test_data_non_uniform):
    """Test quick sort with non-uniform element types"""
    with pytest.raises(NonUniformTypeError):
        quick_sort(test_data_non_uniform)

def test_quick_sort_invalid_ascending_type():
    """Test quick sort with invalid ascending parameter type"""
    with pytest.raises(InvalidAscendingTypeError):
        quick_sort([1, 2, 3], ascending="not_a_boolean")

def test_quick_sort_large_sorted(test_data_large_sorted):
    """Test quick sort with large sorted input"""
    expected = test_data_large_sorted
    actual = quick_sort(test_data_large_sorted)

    assert isinstance(actual, list)
    assert actual == expected

def test_quick_sort_large_unsorted(test_data_large_unsorted):
    """Test quick sort with large unsorted input"""
    expected = list(range(1, 101))
    actual = quick_sort(test_data_large_unsorted)

    assert isinstance(actual, list)
    assert actual == expected