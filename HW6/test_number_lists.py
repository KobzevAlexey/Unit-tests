import pytest
from number_lists import NumberLists


@pytest.fixture
def example_lists():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    return list1, list2


def test_compare_averages(example_lists):
    list1, list2 = example_lists
    number_lists = NumberLists(list1, list2)
    result = number_lists.compare_averages()
    assert result == "Второй список имеет большее среднее значение"


def test_compare_averages_equal(example_lists):
    list1, list2 = example_lists
    list2 = [1, 2, 3, 4, 5]
    number_lists = NumberLists(list1, list2)
    result = number_lists.compare_averages()
    assert result == "Средние значения равны"


def test_compare_averages_empty():
    list1 = []
    list2 = []
    number_lists = NumberLists(list1, list2)
    result = number_lists.compare_averages()
    assert result == "Средние значения равны"
