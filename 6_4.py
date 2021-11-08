import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} (полицейская машина - {self.is_police}) поехал')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self):
        the_turn = ['направо на 90 градусов', 'направо на 45 градусов', 'направо на 135 градусов',
                    'налево на 90 градусов', 'налево на 45 градусов', 'налево на 135 градусов', 'разворот']
        print(f'{self.name} повернула {random.choice(the_turn)}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(f'Вы превысили скорость') if self.speed > 60 else super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Вы превысили скорость') if self.speed > 40 else super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)


car_1 = Car(60, 'красный', 'Mazda')
car_1.go()
car_1.show_speed()
car_1.turn()
car_1.stop()

print()

car_2 = SportCar(100, 'синий', 'BMW')
car_2.go()
car_2.show_speed()
car_2.turn()
car_2.stop()

print()

car_3 = TownCar(70, 'зеленый', 'Audi')
car_3.go()
car_3.show_speed()
car_3.turn()
car_3.stop()

print()

car_4 = WorkCar(30, 'серый', 'форд')
car_4.go()
car_4.show_speed()
car_4.turn()
car_4.stop()

print()

car_5 = PoliceCar(60, 'белый', 'форд', False)
car_5.go()
car_5.show_speed()
car_5.turn()
car_5.stop()
