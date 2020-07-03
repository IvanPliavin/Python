# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('hw5_2.txt') as f:
    strings = f.readlines()
    print('Колличество строк:', len(strings))
    for i, el in enumerate(strings, 1):
        print(f'Строка {i}, Слов: {len(el.split())}')

