# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
     num_list = [num1, num2, num3]
     num_list.remove(min(num_list))
     return sum(num_list)

print(my_func(-58, -20, 20))