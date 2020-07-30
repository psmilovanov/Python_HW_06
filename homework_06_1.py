# Задание 1. Светофор

import time
from random import randint

colour_set = ["Красный", "Желтый", "Зеленый"]
x_sec = [7, 2, 6]  # набор секунд задержки


class TrafficLight:
    __colour: colour_set

    def runnig(self):

        i = 0
        while (i < 9):  # Светофор работает 3 цикла
            self.__colour = colour_set[i % 3]
            print(self.__colour)
            time.sleep(x_sec[i % 3])
            i += 1

    def running_check(self):
        prev_i = 0
        prev_colour = colour_set[0]
        print(prev_colour)
        while True:
            i = randint(0, 2)
            self.__colour = colour_set[i]
            print(self.__colour)
            time.sleep(x_sec[i])
            if (i - prev_i) % 3 != 1:
                print("Неправильный порядок цветов. Работа завершена")
                break
            else:
                prev_i = i


first_tl = TrafficLight()

first_tl.runnig()
print("Корректная работа завершена. Второй вариант.")
first_tl.running_check()
