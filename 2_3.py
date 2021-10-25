month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
list = ['осень', 'зима', 'весна', 'лето']
dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
        10: 'осень', 11: 'осень', 12: 'зима'}

while month < 1 or month > 12:
    month = int(input('Неверное значение. Введите номер месяца от 1 до 12: '))
    if 1 <= month <= 12:
        break

if month >= 9 and month <= 11:
    print(f'Время года месяца {month} - {list[0]}')
elif month <= 2 or month == 12:
    print(f'Время года месяца {month} - {list[1]}')
elif month >= 3 and month <= 5:
    print(f'Время года месяца {month} - {list[2]}')
elif month >= 6 and month <= 8:
    print(f'Время года месяца {month} - {list[3]}')

print(f'Время года месяца {month} - {dict.get(month)}')
