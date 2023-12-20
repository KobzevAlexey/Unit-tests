"""Модуль для генерации случайных чисел."""

import random

def generate_random_sample(lower, upper, size):
    """Генерация случайных чисел в заданном диапазоне и размере."""
    return random.sample(range(lower, upper + 1), size)
