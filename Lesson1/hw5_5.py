# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('hw5_5.txt', 'w+', encoding='utf-8') as f:
    f.write('1 2 150 4 5 6 7 8 2 10 15 30')
    f.seek(0)
    num_str = (f.read())
    num_str = num_str.split()
    num_str = [int(el) for el in num_str]
    print('\nСумма числел =', sum(num_str), file=f)
