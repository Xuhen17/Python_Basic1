# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ["белка", ["синий", "белый", "голубой"], 17, 3.14, (7 + 8j), {'множество', 1, 5},
           {"Зенит": "Чемпион", "ЦСКА": "Кони"}, (17, 18, 19), None, True, bytes(5)]

for num, item in enumerate(my_list, 1):
    print(f'{num}-й элемент: {item} - {type(item)}')
