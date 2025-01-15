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
