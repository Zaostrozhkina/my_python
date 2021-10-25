spec = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
list = []
n = 0
while True:
    check = input('Введите "да", если хотите ввести товар или любую букву для показа аналитики: ')
    if check == 'да':
        n += 1
        spec['название'] = input('Введите название товара: ')
        spec['цена'] = input('Введите цену товара: ')
        spec['количество'] = input('Введите количество товара: ')
        spec['единица измерения'] = input('Введите единицу измерения: ')
        list_copy = spec.copy()
        goods = (n, list_copy)
        list.append(goods)
        # print(goods)
        for f in spec:
            analytics[f].append(spec[f])
    else:
        break
print('-' * 20)
print('Товары: ')
print(list)
print('-' * 20)
print('Аналитика: ')
print(analytics)
