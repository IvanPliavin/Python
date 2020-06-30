# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go')
        self._show_speed()

    def stop(self):
        print(f'{self.name} stop')
        self.speed = 0
        self._show_speed()

    def turn(self, direction):
        print(f'{self.name} turn {direction}')
        self.speed = self.speed / 2
        self._show_speed()

    def _show_speed(self):
        print(f'{self.name} speed: {self.speed} km/h')


class TownCar(Car):

    def _show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speed: {self.speed} km/h Превышение скорости!')
        else:
            print(f'{self.name} speed: {self.speed} km/h')

    pass


class SportCar(Car):
    pass


class WorkCar(Car):

    def _show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speed: {self.speed} km/h Превышение скорости!')
        else:
            print(f'{self.name} speed: {self.speed} km/h')

    pass


class PoliceCar(Car):
    pass


car1 = TownCar('BMW', 'Black', 100, False)
car2 = SportCar('Ferrari', 'Red', 200, False)
car3 = WorkCar('Renault', 'White', 60, False)
car4 = PoliceCar('Ford', 'White-Blue', 100, True)

car1.go()
car1.turn('left')
car1.stop()

car3.go()
car3.speed = 40
car3.go()