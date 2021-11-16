class MyOwnError(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
numbers = '1234567890-,.'

while True:
    try:
        num = input('Введите число для продолжения работы или "stop" для завершения: ')
        if num == 'stop':
            print(f'Финальный список: {my_list}')
            break
        else:
            if not set(num).difference(numbers):
                my_list.append(num)
            else:
                raise MyOwnError('Неверное значение! Требуется ввести число.')
    except MyOwnError as err:
        print(err)
