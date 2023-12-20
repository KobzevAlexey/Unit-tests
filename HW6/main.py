"""Модуль для демонстрации сравнения списков чисел."""

from random_generator import generate_random_sample
from number_lists import NumberLists

list1 = generate_random_sample(1, 100, 10)
list2 = generate_random_sample(1, 100, 10)

number_lists = NumberLists(list1, list2)

result = number_lists.compare_averages()

print(list1)
print(list2)
print(result)
