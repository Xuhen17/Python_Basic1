# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_numbers = [numbers[i] for i in range(1, len(numbers)) if numbers[i - 1] < numbers[i]]
print(new_numbers)
