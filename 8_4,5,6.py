class Warehouse:
    sklad = []

    def work(self):
        deal = input('Введите "+" для добавления устройства, "-" для выдачи в подразделение, "Q" для завершения: ')
        try:
            if deal == '+':
                org = input('Укажите тип устройства: принтер/сканер/ксерокс: ')
                if org == 'принтер':
                    print(Printer.add_other_plus(self))
                    print()
                    return Printer.add_other_plus(self), Warehouse.plus(self)
                if org == 'сканер':
                    print(Scanner.add_other_plus(self))
                    print()
                    return Scanner.add_other_plus(self), Warehouse.plus(self)
                if org == 'ксерокс':
                    print(Xerox.add_other_plus(self))
                    print()
                    return Xerox.add_other_plus(self), Warehouse.plus(self)

            elif deal == "-":
                org = input('Укажите тип устройства: принтер/сканер/ксерокс: ')
                if org == 'принтер':
                    print(Printer.add_other_minus(self))
                    print()
                    return Printer.add_other_minus(self), Warehouse.minus(self)
                if org == 'сканер':
                    print(Scanner.add_other_minus(self))
                    print()
                    return Scanner.add_other_minus(self), Warehouse.minus(self)
                if org == 'ксерокс':
                    print(Xerox.add_other_minus(self)),
                    print()
                    return Xerox.add_other_minus(self), Warehouse.minus(self)
                return Warehouse.minus(self)

            if deal == 'Q':
                print(f'Отчет по складу: {Warehouse.sklad}')

        except AttributeError:
            print('Выбран неверный тип оргтехники')

    def plus(self):
        return Warehouse.sklad.append(Warehouse.work(self))

    def minus(self):
        return Warehouse.sklad.remove(Warehouse.work(self))



class Orgtech():
    other = []

    def __init__(self, type_org, amount, color):
        self.type_org = type_org  # тип оргтехники (принтер/сканер/ксерокс)
        self.amount = amount  # количество
        self.color = color  # цвет
        self.other = []

    def addition(self):
        self.other = []

    def __str__(self):
        print(
            f'тип - {self.type_org}, количество - {self.amount}, цвет - {self.color}, прочие характеристики - {self.other}')


class Printer(Orgtech):
    def __init__(self, type_org, amount, color, print_speed, print_type):
        super().__init__(type_org, amount, color)
        self.print_speed = print_speed  # скорость печати (100, 200, 300)
        self.print_type = print_type  # тип принтера (цветной или чб):

    def add_other_plus(self):
        return f'Возврат на склад: тип - {self.type_org}, ' \
               f'количество - {self.amount}, цвет - {self.color}, скорость печти - {self.print_speed}, ' \
               f'тип принтера - {self.print_type}.'

    def add_other_minus(self):
        return f'Передача со склада следующей оргтехники: тип - {self.type_org}, ' \
               f'количество - {self.amount}, цвет - {self.color}, скорость печти - {self.print_speed}, ' \
               f'тип принтера - {self.print_type}.'


class Scanner(Orgtech):
    def __init__(self, type_org, amount, color, resolution):
        super().__init__(type_org, amount, color)
        self.resolution = resolution  # расширения сканера (100 ppi, 200 ppi, 400 ppi)

    def add_other_plus(self):
        return f'Возврат на склад: тип - {self.type_org}, ' \
               f'количество - {self.amount}, цвет - {self.color}, расширение сканера - {self.resolution}.'

    def add_other_minus(self):
        return f'Передача со склада следующей оргтнхники: тип - {self.type_org}, ' \
               f'количество - {self.amount}, цвет - {self.color}, расширение сканера - {self.resolution}.'


class Xerox(Orgtech):
    def __init__(self, type_org, amount, color, xerox_speed, scaling):
        super().__init__(type_org, amount, type_org)
        self.xerox_speed = xerox_speed  # скорость копирования (10, 20 или 30) изображений в мин
        self.scaling = scaling  # наличие масштабирования (да/нет)

    def add_other_plus(self):
        return f'Возврат на склад: тип - {self.type_org}, количество - {self.amount}, цвет - {self.color}, ' \
               f'скорость печти - {self.xerox_speed}, тип принтера - {self.scaling}.'

    def add_other_minus(self):
        return f'Передача со склада следующей оргтнхники: тип - {self.type_org}, количество - {self.amount}, ' \
               f'цвет - {self.color}, скорость печти - {self.xerox_speed}, тип принтера - {self.scaling}.'


org_1 = Printer('принтер', '2', 'черный', '100', 'чб')
org_2 = Scanner('сканер', '3', 'белый', '200 ppi')
org_3 = Xerox('ксерокс', '1', 'синий', '20', 'да')
org_4 = Printer('принтер', '1', 'серый', '200', 'чб')
org_5 = Scanner('сканер', '1', 'белый', '100 ppi')
org_6 = Xerox('ксерокс', '2', 'черный', '30', 'нет')

Warehouse.work(org_1)
Warehouse.work(org_2)
Warehouse.work(org_3)
Warehouse.work(org_4)
Warehouse.work(org_5)
Warehouse.work(org_6)
