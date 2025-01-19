import pytest

from pysorting.insertion_sort import insertion_sort


def test_insertion_sort(test_data1):
    expected = [1,2,3,4,5,6,7,8]
    actual = insertion_sort(test_data1)
    assert actual == expected

def test_empty(test_data_empty):
    actual = insertion_sort(test_data_empty)
    assert isinstance(actual,list)
    assert len(actual) == 0

def test_sorted(test_data_sorted):
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    actual = insertion_sort(test_data_sorted)
    assert actual == expected

def test_string_error(test_data_error2):
    with pytest.raises(TypeError):
        insertion_sort(test_data_error2)

def test_wrong_values(test_data_error):
    with pytest.raises(TypeError):
        insertion_sort(test_data_error)

def test_ascending_false(test_data1):
    expected = [8,7,6,5,4,3,2,1]
    actual = insertion_sort(test_data1, ascending = False)
    assert actual == expected

def test_one_float(test_data_float):
    expected = [1,2,3.0,4,5]
    actual = insertion_sort(test_data_float)
    assert actual == expected