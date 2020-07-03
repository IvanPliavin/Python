# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('hw5_7.txt') as f:
    lines = f.readlines()
    splited_lines = [line.split() for line in lines]
    companies_result = {el[0]: int(el[2]) - int(el[3]) for el in splited_lines}

    profit_companies = {name: value for name, value in companies_result.items() if value > 0}
    unprofit_companies = {name: value for name, value in companies_result.items() if value < 0}
    avrg_revenue = {'Avrg_proffit': int(sum(profit_companies.values()) / len(profit_companies.values()))}

    json_result = [companies_result, avrg_revenue]

with open('hw5_7.json', 'w') as f_json:
    json.dump(json_result, f_json)





