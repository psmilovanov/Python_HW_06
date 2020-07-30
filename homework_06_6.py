# Задание 6.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        return (f"Запуск отрисовки")


class Pencil(Stationery):

    def draw(self):
        return (f"Запуск штриховки")


class Pen(Stationery):

    def draw(self):
        return (f"Запуск каллиграфии")


class Handle(Stationery):

    def draw(self):
        return (f"Запуск закраски")


brush = Stationery("Кисть")
print(brush.title + ' ' + brush.draw())

pen_01 = Pen("Ручка")
print(pen_01.title + ' ' + pen_01.draw())

pencil_01 = Pen("Карандаш")
print(pencil_01.title + ' ' + pencil_01.draw())

handle_01 = Handle("Маркер")
print(handle_01.title + ' ' + handle_01.draw())
