# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def contacts(**kwargs):
    print(kwargs)

contacts(Имя='Иван', Фамилия='Плявин', Год_рождения=1991,
        Город_проживания='Москва', email='plyavini@mail.ru', телефон=89154943337)
