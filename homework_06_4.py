# Задание 4 и 5.

colour_set = {"Красный", "Зеленый", "Оранжевый", "Мокрый асфальт"}


class Car:
    speed: int
    colour: colour_set
    name: str
    is_police: bool

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f"Автомобиль {self.name} едет!")

    def stop(self):
        if self.speed == 0:
            print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        return (f"Автомобиль {self.name} повернул {direction}")

    def show_speed(self):
        return (f"Скорость автомобиля {self.name} равна {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return (f"Скорость автомобиля {self.name} равна {self.speed}. Внимание это превышение!")
        else:
            return (f"Скорость автомобиля {self.name} равна {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):

        if self.speed > 40:
            return (f"Скорость автомобиля {self.name} равна {self.speed}. Внимание это превышение!")
        else:
            return (f"Скорость автомобиля {self.name} равна {self.speed}")


class PoliceCar(Car):
    pass


lada_01 = TownCar(50, "Зеленый", "Лада", False)

print(lada_01.colour)
lada_01.go()
lada_01.stop()
print(lada_01.turn("налево"))
print(lada_01.show_speed())

tractor = WorkCar(60, "Оранжевый", "Беларусь", False)

print(tractor.name)
tractor.go()
print(tractor.turn("на юго-запад"))
print(tractor.show_speed())

ferrari = SportCar(130, "Красный", "Феррари", False)
ferrari.go()
print(ferrari.colour)
print(ferrari.turn("на 55 градусов"))
print(ferrari.show_speed())
