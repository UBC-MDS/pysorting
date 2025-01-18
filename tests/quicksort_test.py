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

def test_strings():
    """Test sorting a list of strings."""
    assert quick_sort(["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]
    assert quick_sort(["apple", "banana", "cherry"], reverse=True) == ["cherry", "banana", "apple"]

def test_mixed_types():
    """Test sorting a list with mixed comparable types."""
    assert quick_sort([3, 1.5, 2, 4.2]) == [1.5, 2, 3, 4.2]

def test_none_in_list():
    """Test sorting a list containing None values."""
    with pytest.raises(ValueError, match="All elements in the list must be comparable."):
        quick_sort([1, None, 3])

def test_non_list_input():
    """Test passing a non-list input."""
    with pytest.raises(TypeError, match="Input must be a list."):
        quick_sort("not a list")

def test_invalid_reverse_param():
    """Test passing an invalid reverse parameter."""
    with pytest.raises(TypeError, match="'reverse' must be a boolean value."):
        quick_sort([1, 2, 3], reverse="yes")