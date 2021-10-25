list = [77, 44.5, 'name', True, (3, False, 'девять'), None, [1, 4, 'семь'], 174.3, (3 + 7j), {4, 3}]
a = 1
for i in list:
    print(f'Тип данных элемента {a} - ', type(i))
    a += 1
