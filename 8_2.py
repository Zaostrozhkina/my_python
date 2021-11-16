class OwnError(Exception):
    def __init__(self, text):
        self.text = text


a = input('Введите делимое: ')
b = input('Введите делитель: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise OwnError('Деление на ноль запрещено')
except ValueError:
    print('Вы ввели не число')
except OwnError as err:
    print(err)
else:
    print(round(a / b, 2))
