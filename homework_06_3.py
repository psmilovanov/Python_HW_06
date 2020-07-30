# Задание 3.

salary_dict = {"wage": float, "bonus": float}


class Worker:
    name: str
    surname: str
    position: str
    _income: salary_dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return (f"Полное имя сотрудника: {self.name}, {self.surname}")

    def get_total_income(self):
        return float(self._income.get("wage") + self._income.get("bonus"))


first_emploee = Position("Пол", "Бетани", "актер", {"wage": 200, "bonus": 1000})

print(first_emploee.get_full_name())
print(f"Суммарный доход: {first_emploee.get_total_income()}")
