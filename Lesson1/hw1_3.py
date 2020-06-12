# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_var = str(input('Введите число: '))
user_var = int(user_var) + int(str(user_var * 2)) + int(str(user_var * 3))
print(user_var)


