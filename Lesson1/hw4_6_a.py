# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

import sys
from itertools import count
"""a)"""

try:
    for el in count(int(sys.argv[1])):
        if el > int(sys.argv[2]):
            print('Расчет окончен')
            break
        print(el)
except ValueError and IndexError:
    print('Это генератор числел. Введите через пробел число с которого начать и число до которого считать')
