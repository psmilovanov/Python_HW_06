# Задание 2.

class Road:
    _length: float
    _width: float

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_per_sq, depth):
        print(
            f"Необходимая масса асфальта на эту дорогу: {round((self._length * self._width * mass_per_sq * depth), 2)} кг")


firstRoad = Road(1000, 35)

mass_per_sq = float(
    input("Введите массу в кг асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: "))
depth = float(input("Введите толщину покрытия в см: "))

print(f"Первая дорога длиной {firstRoad._length} метров и шириной {firstRoad._width} метров")

firstRoad.calc_mass(mass_per_sq, depth)
