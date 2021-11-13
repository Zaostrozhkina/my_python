class Cell:
    def __init__(self, n):
        self.n = round(n)

    def __add__(self, other):
        print('Cумма клеток: ')
        return self.n + other.n

    def __sub__(self, other):
        print('Разность клеток: ')
        return self.n - other.n if self.n > other.n else print('Первая клетка меньше второй. Вычитание невозможно.')

    def __mul__(self, other):
        print('Произведение клеток: ')
        return self.n * other.n

    def __truediv__(self, other):
        print('Частное от деления клеток: ')
        return self.n // other.n

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.n // row)]) + '\n' + '*' * (self.n % row)


cell_1 = Cell(15)
cell_2 = Cell(7)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(4))
