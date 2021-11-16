class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def transformation(cls, data):
        list_1 = data.split('-')
        day, month, year = int(list_1[0]), int(list_1[1]), int(list_1[2])
        return f'День - {day}, месяц - {month}, год - {year}'

    @staticmethod
    def test(d, m, y):
        print(f'Число {d} верно') if 1 <= d <= 31 else print('Такого дня нет в месяце')
        print(f'Месяц {m} верный') if 1 <= m <= 12 else print('Такого месяца нет в году')
        print(f'Год {y} верный') if 1000 <= y <= 2021 else print('Такой год еще не наступил или прошел слишком давно')


data_1 = Data('11-10-2021')
print(data_1.transformation('11-10-2021'))
Data.test(11, 10, 2021)
