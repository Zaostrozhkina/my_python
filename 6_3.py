class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии равен {sum(self._income.values())}')


worker_1 = Position('Иван', 'Иванов', 'Manager', 40000, 50000)
worker_1.get_full_name()
worker_1.get_total_income()

print()

worker_2 = Position('Василий', 'Васильев', 'Руководитель отдела', 60000, 45000)
worker_2.get_full_name()
worker_2.get_total_income()
