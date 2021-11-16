class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num = complex(x, y)
        print(self.num)

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


num_1 = ComplexNumber(3, -2)
num_2 = ComplexNumber(4, 1)

print(f'Сумма комплексных чисел равна: {num_1 + num_2}')
print(f'Произведение комплексных чисел равно: {num_1 * num_2}')
