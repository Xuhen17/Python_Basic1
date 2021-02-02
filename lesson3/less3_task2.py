# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user(last_name, name, birth_year, city, phone, email):
    """Функция выводит данные о пользователе одной строкой.

    Именованные параметры:
    last_name -- фамилия
    name -- имя
    birth_year -- год рождения
    city -- город проживания
    phone -- телефон
    email -- адрес электронной почты

    """
    print(f'имя: {name}, фамилия: {last_name}, год рождения: {birth_year}, город проживания: {city}, '
          f'e-mail: {email}, телефон {phone}')


user(name=input("Имя? "), last_name=input("Фамилия? "), birth_year=(input("Год рождения? ")),
     city=input("Город проживания? "), email=input("e-mail? "), phone=(input("Телефон? ")))