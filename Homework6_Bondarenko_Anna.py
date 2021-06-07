# Задание 1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time

class TrafficLight:
    _trafficlight_color = "Красный"

    def running(self):
        self.trafficlight_color = "Красный"
        print('Сигнал светофора: "Красный"')
        time.sleep(7)
        self._trafficlight_color = "Желтый"
        print('Сигнал светофора: "Желтый"')
        time.sleep(2)
        self.trafficlight_color = "Зеленый"
        print('Сигнал светофора: "Зеленый"')
        time.sleep(4)

tl1 = TrafficLight()
while True:
    tl1.running()

# Звдание 2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 0.05м = 125т

class Road:
    _road_lenght = 5000
    _road_wight = 20
    def massa(self, mass, depth):
        print(self._road_lenght * self._road_wight * mass * depth)
road1 = Road()
road1.massa(25, 0.05)

# Задание 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Pavel', 'Durov', 'Programmer', 1000000, 300000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# Задание 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = ''
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, ):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print('Скорость машины:', self.speed)

    def pol_car(self):
        if self.is_police:
            print('Это полицейская машина!')
        else:
            print('Это машина жителя.')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Название модели:', self.name, '\nСкорость машины:', self.speed)
        if self.speed > 60:
            print('Внимание! Превышение скорости!')


town_car = TownCar(70, "Black", "Volkswagen")
town_car.show_speed()
town_car.pol_car()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Название модели:', self.name, '\nСкорость машины:', self.speed)
        if self.speed > 60:
            print("Превышение скорости!")


Sport_car = SportCar(100, "Red", "Bugatti")
Sport_car.show_speed()
Sport_car.pol_car()


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Название модели:', self.name, '\nСкорость машины:', self.speed)
        if self.speed > 60:
            print("Превышение скорости!")


Work_car = WorkCar(40, "White", "Ford")
Work_car.show_speed()
Work_car.pol_car()


class PoliceCar(Car):
    is_police = True

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


Police_car = PoliceCar(50, "Kia", "White")
Police_car.show_speed()
Police_car.pol_car()

# Задание 5
#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Вы взяли:', self.title, '\nЗапуск отрисовки ручкой')

pen = Pen('Ручка')
pen.draw()


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Вы взяли:', self.title, '\nЗапуск отрисовки карандашом')

pencil = Pencil('Карандаш')
pencil.draw()

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Вы взяли:', self.title, '\nЗапуск отрисовки маркером')

handle = Handle('Маркер')
handle.draw()