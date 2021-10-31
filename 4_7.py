def fact(num):
    f = 1
    for el in range(0, num + 1):
        yield f'{el}! = {f}'
        f *= el + 1


for el in fact(int(input('Введите целое число: '))):
    print(el)
