def my_f():
    s = 0
    while True:
        list = input('Введите числа через пробел или введите Q для завершения: ').split()
        for i in list:
            if i == "Q":
                print(s)
                return s
            else:
                try:
                    s += int(i)
                except ValueError:
                    print('Для завершения нажмите Q')
        print(f'Сумма значений равна {s}')


my_f()
