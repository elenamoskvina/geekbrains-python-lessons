# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, speed, color, name):
        self.color = color
        self.speed = speed
        self.name = name
        self._is_police = False

    def go(self, speed):
        self.speed = speed
        print(f"Машина поехала со скоростью {speed}км/ч")

    def stop(self):
        self.speed = 0
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")


class SportCar(Car):
    pass


class TownCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self._is_police = True

    def view_type(self):
        return self._is_police


my_car = TownCar(0, "red", "Nissan")
michael_car = SportCar(0, "blue", "Toyota")
government_car = PoliceCar(0, "blue and white", "Lada")

