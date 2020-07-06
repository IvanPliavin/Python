# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')

    pass


class Pencil(Stationery):
    def draw(self):
        print('Пишем карандашем')

    pass


class Handle(Stationery):
    def draw(self):
        print('Пишем маркером')

    pass

penc1 = Pencil('Карандаш черный')
han1 = Handle('Маркер красный')
pen1 = Pen('Ручка синяя')
penc1.draw()
pen1.draw()
han1.draw()

