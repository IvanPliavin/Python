# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('hw5_4.txt', encoding='utf-8') as f:
    word_list = f.readlines()
result_list = []
for el in word_list:
    if 'One' in el:
        result_list.append(el.replace('One', 'Один'))
    elif 'Two' in el:
        result_list.append(el.replace('Two', 'Два'))
    elif 'Three' in el:
        result_list.append(el.replace('Three', 'Три'))
    elif 'Four'in el:
        result_list.append(el.replace('Four', 'Четыре'))

with open('hw5_4_result.txt', 'w', encoding='utf-8') as f:
    f.writelines(result_list)

