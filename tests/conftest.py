import pytest


@pytest.fixture
def text_data1():
    return [5, 3, 8, 6, 2, 7, 4, 1]


@pytest.fixture
def text_data_single_element():
    return [5]


@pytest.fixture
def text_data_sorted():
    return [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.fixture
def text_data_empty():
    return []


@pytest.fixture
def text_data_error():
    return [3, "apple", 7, None]


@pytest.fixture
def text_data_error2():
    return "hello"

# Fixture to initialize a small unsorted list
@pytest.fixture
def small_unsorted_list():
    return [3, 1, 4, 2]

# Fixture to initialize a large unsorted list (descending order)
@pytest.fixture
def large_unsorted_list():
    return list(range(100, 0, -1))  # A large descending list

# Fixture to initialize a large sorted list (ascending order)
@pytest.fixture
def large_sorted_list():
    return list(range(1, 101))  # A large sorted list (ascending order)
