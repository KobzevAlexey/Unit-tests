"""Модуль, содержащий класс NumberLists для сравнения списков чисел."""


class NumberLists:
    """Класс, представляющий два списка чисел и их сравнение."""

    def __init__(self, list1, list2):
        """Инициализация NumberLists с двумя списками чисел."""
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, num_list):
        """Вычисление среднего значения заданного списка чисел."""
        if not num_list:
            return 0
        return sum(num_list) / len(num_list)

    def compare_averages(self):
        """Сравнение средних значений двух списков чисел."""
        avg1 = self.calculate_average(self.list1)
        avg2 = self.calculate_average(self.list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"

        return "Средние значения равны"
