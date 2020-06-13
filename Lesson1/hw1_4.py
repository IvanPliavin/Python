# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_var = int(input('Введите число: '))
tmp = 0
max_number = 0
while tmp != 100:
    number = (user_var // 10 ** tmp) % 10
    if number > max_number:
        max_number = number
    tmp += 1
print(max_number)







