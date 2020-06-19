# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
goods_dict = {}
goods_list = []
result_list = []
while True:
    start_stop = input('Добавить товар? да/нет : ')
    if start_stop == 'нет':
        print('Ввод окончен')
        break
    goods_dict['название'] = input('Название : ')
    goods_dict['цена'] = int(input('Цена в руб. : '))
    goods_dict['колличество'] = int(input('Колличество : '))
    goods_dict['ед'] = input('Ед. измерения (шт/кг): ')
    goods_list.append(goods_dict)
for element in enumerate(goods_list[:], 1):
    result_list.append(element)
print(result_list)

