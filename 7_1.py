class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([f'{n}' for n in line]) for line in self.matrix)

    def __add__(self, other):
        return Matrix(map(lambda n, m: map(lambda x, y: x + y, n, m), self.matrix, other.matrix))


matrix_1 = Matrix([[1, 2, 5], [4, 5, 0], [7, 8, -9]])
matrix_2 = Matrix([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_2 + matrix_1)
