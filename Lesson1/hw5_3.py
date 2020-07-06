# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('hw5_3.txt', encoding='utf-8') as f:
    workers_list = f.readlines()

worker_dict = {}
for el in workers_list:
    name, salary = el.split()
    worker_dict[name] = int(salary)

for key, val in worker_dict.items():
    if val < 20000:
        print(f'Сотрудник {key}, получает {val} меньше 20000!')

avrg_salary = sum(worker_dict.values()) / len(worker_dict.values())
print('Средний доход на сотрудника:', round(avrg_salary, 1))

