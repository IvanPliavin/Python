# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


my_list = []

while True:
    user_var = input('Введите значение и нажмите Энтр, для завершения ввода отправьте пустое поле : ')
    if user_var == '':
        print('Ввод окончен')
        break
    else:
        my_list.append(user_var)
print(my_list)
a, b = 0, 1
if len(my_list) % 2 == 0:
    while a != len(my_list):
        my_list[a], my_list[b] = my_list[b], my_list[a]
        a += 2
        b += 2
else:
    while a != len(my_list) - 1:
        my_list[a], my_list[b] = my_list[b], my_list[a]
        a += 2
        b += 2

print(my_list)

