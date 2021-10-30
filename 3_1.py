def my_func(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


print(my_func(float(input('Введите переменную a (делимое): ')), float(input('Введите переменную b (делитель): '))))
