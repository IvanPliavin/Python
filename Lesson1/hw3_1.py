# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = 'Ошибка: на 0 делить нельзя'
    return result

print(division(float(input('Введите число 1: ')), float(input('Введите число 2: '))))

