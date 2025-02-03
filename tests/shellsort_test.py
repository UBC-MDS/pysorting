# tests/shellsort_test.py
import pytest
from pysorting import shell_sort, InvalidElementTypeError, NonUniformTypeError, InvalidAscendingTypeError

# Define test cases as fixtures
@pytest.fixture(params=[
    [],  # empty array
    [1],  # single-element array
    [1, 2, 3, 4, 5],  # already sorted array
    [5, 2, 8, 3, 1],  # unsorted array
    [5, 2, 8, 3, 1, 2, 5],  # array with duplicates
    [5, -2, 8, -3, 1]  # array with negative numbers
])
def test_data(request):
    return request.param

@pytest.fixture
def test_data_reverse_sorted():
    return [8, 7, 6, 5, 4, 3, 2, 1]

@pytest.fixture
def test_data_single_element():
    return [5]

@pytest.fixture
def test_data_empty():
    return []

@pytest.fixture
def test_data_error():
    return "not a list"

@pytest.fixture
def test_invalid_error():
    return [1, "a", 3]

@pytest.fixture
def test_nonuniform_error():
    return [1, 2, "3"]

def test_shell_sort(test_data):
    """Test shell sort with various inputs"""
    assert shell_sort(test_data) == sorted(test_data)

def test_shell_sort_reverse(test_data_reverse_sorted):
    """Test shell sort with reverse sorting"""
    assert shell_sort(test_data_reverse_sorted, ascending=False) == sorted(test_data_reverse_sorted, reverse=True)

def test_shell_sort_single_element(test_data_single_element):
    """Test shell sort with single-element input"""
    assert shell_sort(test_data_single_element) == test_data_single_element

def test_shell_sort_empty(test_data_empty):
    """Test shell sort with empty input"""
    assert shell_sort(test_data_empty) == test_data_empty

def test_shell_sort_error(test_data_error):
    """Test shell sort with non-list input"""
    with pytest.raises(TypeError):
        shell_sort(test_data_error)

def test_shell_sort_invalid_element_error(test_invalid_error):
    """Test shell sort with invalid element type"""
    with pytest.raises(NonUniformTypeError):
        shell_sort(test_invalid_error)

def test_shell_sort_non_uniform_error(test_nonuniform_error):
    """Test shell sort with non-uniform element types"""
    with pytest.raises(NonUniformTypeError):
        shell_sort(test_nonuniform_error)

def test_shell_sort_invalid_ascending_type():
    """Test shell sort with invalid ascending parameter type"""
    with pytest.raises(InvalidAscendingTypeError):
        shell_sort([1, 2, 3], ascending="not a boolean")