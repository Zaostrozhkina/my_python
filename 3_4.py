def my_func(x, y):
    if x >= 0 and y < 0:
        a = x ** y
        return a
    else:
        print("Неверные значения параметров")


print(my_func(2, -3))


def my_function(x, y):
    """Возведение в отрицательную степень с помощью цикла"""
    if x >= 0 and y < 0:
        n = 1
        for i in range(1, abs(y)):
            n *= x
            a = 1 / n
        return a
    else:
        return "Неверные значения параметров"


x = float(input('Введите действительное положительное число (x): '))
y = int(input('Введите целое отрицательно число (y): '))
print(my_func(x, y))
