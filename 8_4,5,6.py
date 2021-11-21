class Orgtech:
    sklad = []

    def __init__(self, type_org, amount, color):
        self.type_org = type_org  # тип оргтехники (принтер/сканер/ксерокс)
        self.amount = amount  # количество
        self.color = color  # цвет

    @staticmethod
    def change(self):
        deal = input('Введите "+" для добавления устройства, "-" для выдачи в подразделение, "Q" для завершения: ')
        if deal == '+':
            try:
                type_org_1 = input('Введите тип техники (принер/сканер/ксерокс): ')
                if type_org_1 == 'принтер':
                    amount_1 = int(input('Введите количество: '))
                    color_1 = input('Введите цвет: ')
                    print_speed_1 = int(input('Введите скорость печати: '))
                    print_type_1 = input('Введите тип принтера (цветной/чб): ')
                    name_org_new = {'Тип оргтехники': type_org_1, 'количество': amount_1, 'цвет': color_1,
                                    'скорость печати': print_speed_1, 'тип принтера': print_type_1}
                elif type_org_1 == 'сканер':
                    amount_1 = int(input('Введите количество: '))
                    color_1 = input('Введите цвет: ')
                    resolution_1 = int(input('Введите расширение сканера (100 ppi, 200 ppi, 400 ppi): '))
                    name_org_new = {'Тип оргтехники': type_org_1, 'количество': amount_1, 'цвет': color_1,
                                    'расширение сканера': resolution_1}
                elif type_org_1 == 'ксерокс':
                    amount_1 = int(input('Введите количество: '))
                    color_1 = input('Введите цвет: ')
                    xerox_speed_1 = int(input('Выберите скорость копирования (10, 20 или 30) изображений в мин: '))
                    scaling_1 = input('Наличие масштабирования (да/нет): ')
                    name_org_new = {'Тип оргтехники': type_org_1, 'количество': amount_1, 'цвет': color_1,
                                    'скорость копирования': xerox_speed_1, 'наличие машстабирования': scaling_1}
                Orgtech.sklad.append(name_org_new)
                print(f'Возврат на склад: {name_org_new}.\n')
                print(f'Сейчас на складе: {Orgtech.sklad} \n')
                return name_org_new
            except UnboundLocalError:
                print('Выбран неверный тип оргтехники!')
            except ValueError:
                print('Неверное значение!')

        elif deal == '-':
            type_org_1 = input('Введите тип техники (принер/сканер/ксерокс): ')
            try:
                if type_org_1 == 'принтер':
                    amount_1 = input('Введите количество: ')
                    color_1 = input('Введите цвет: ')
                    print_speed_1 = input('Введите скорость печати: ')
                    print_type_1 = input('Введите тип принтера (цветной/чб): ')
                    name_org_new = {'Тип оргтехники': type_org_1, 'количество': amount_1, 'цвет': color_1,
                                    'скорость печати': print_speed_1, 'тип принтера': print_type_1}
                elif type_org_1 == 'сканер':
                    amount_1 = input('Введите количество: ')
                    color_1 = input('Введите цвет: ')
                    resolution_1 = input('Введите расширение сканера (100 ppi, 200 ppi, 400 ppi): ')
                    name_org_new = {'Тип оргтехники': type_org_1, 'количество': amount_1, 'цвет': color_1,
                                    'расширение сканера': resolution_1}
                elif type_org_1 == 'ксерокс':
                    amount_1 = input('Введите количество: ')
                    color_1 = input('Введите цвет: ')
                    xerox_speed_1 = input('Выберите скорость копирования (10, 20 или 30) изображений в мин: ')
                    scaling_1 = input('Наличие масштабирования (да/нет): ')
                    name_org_new = {'Тип оргтехники': type_org_1, 'количество': amount_1, 'цвет': color_1,
                                    'скорость копирования': xerox_speed_1, 'наличие машстабирования': scaling_1}
                Orgtech.sklad.remove(name_org_new)
                print(f'Передача со склада следующей оргтехники: {name_org_new}.\n')
                print(f'Сейчас на складе: {Orgtech.sklad} \n')
                return name_org_new
            except UnboundLocalError:
                print('Выбран неверный тип оргтехники!')

        elif deal == 'Q':
            print(f'Отчет по складу: {Orgtech.sklad}')

    def org_add(self):
        if self.type_org == 'принтер':
            Printer.sklad.append(Printer.name(self))
            print(f'Возврат на склад: \n {Printer.name(self)}.')
        elif self.type_org == 'сканер':
            Scanner.sklad.append(Scanner.name(self))
            print(f'Возврат на склад: \n {Scanner.name(self)}.')
        elif self.type_org == 'ксерокс':
            Xerox.sklad.append(Xerox.name(self))
            print(f'Возврат на склад: \n {Xerox.name(self)}.')

    def org_del(self):
        try:
            if self.type_org == 'принтер':
                Printer.sklad.remove(Printer.name(self))
                print(f'Выдано со склада: \n {Printer.name(self)}.')
            elif self.type_org == 'сканер':
                Scanner.sklad.remove(Scanner.name(self))
                print(f'Выдано со склада: \n {Scanner.name(self)}.')
            elif self.type_org == 'ксерокс':
                Xerox.sklad.remove(Xerox.name(self))
                print(f'Выдано со склада: \n {Xerox.name(self)}.')
        except ValueError:
            print('Такой оргтехники нет на складе для выдачи.')


class Printer(Orgtech):
    def __init__(self, type_org, amount, color, print_speed, print_type):
        super().__init__(type_org, amount, color)
        self.print_speed = print_speed  # скорость печати (100, 200, 300)
        self.print_type = print_type  # тип принтера (цветной или чб):
        self.name_org_new = {'Тип оргтехники': type_org, 'количество': amount, 'цвет': color,
                             'скорость печати': print_speed, 'тип принтера': print_type}

    def name(self):
        return self.name_org_new


class Scanner(Orgtech):
    def __init__(self, type_org, amount, color, resolution):
        super().__init__(type_org, amount, color)
        self.resolution = resolution  # расширения сканера (100 ppi, 200 ppi, 400 ppi)
        self.name_org_new = {'Тип оргтехники': type_org, 'количество': amount, 'цвет': color,
                             'расширение сканера': resolution}

    def name(self):
        return self.name_org_new


class Xerox(Orgtech):
    def __init__(self, type_org, amount, color, xerox_speed, scaling):
        super().__init__(type_org, amount, color)
        self.xerox_speed = xerox_speed  # скорость копирования (10, 20 или 30) изображений в мин
        self.scaling = scaling  # наличие масштабирования (да/нет)
        self.name_org_new = {'Тип оргтехники': type_org, 'количество': amount, 'цвет': color,
                             'скорость копирования': xerox_speed, 'наличие машстабирования': scaling}

    def name(self):
        return self.name_org_new


org_2 = Printer('принтер', 2, 'синий', 100, 'чб')
org_3 = Scanner('сканер', 4, 'белый', 100)
org_4 = Xerox('ксерокс', 5, 'черный', 30, 'да')

Orgtech.org_add(org_2)
Orgtech.org_add(org_3)
Orgtech.org_add(org_4)
print(f'Склад: \n {Orgtech.sklad}')
Orgtech.org_del(org_3)
print(f'Склад: \n {Orgtech.sklad}')

org_1 = Orgtech

Orgtech.change(org_1)
Orgtech.change(org_1)
