class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(y) for y in x]) for x in self.matrix])

    def __add__(self, other):
        matrix_out_2 = []
        for x in range(len(self.matrix)):
            matrix_out_1 = []
            for y in range(len(self.matrix[x])):
                matrix_out_1.append(self.matrix[x][y] + other.matrix[x][y])
            matrix_out_2.append(matrix_out_1)
        return Matrix(matrix_out_2)


m1 = [[1, 2, 2, 4], [4, 3, 54, 4], [56, 3, 23, 23], [23, 123, 3, 4]]
m2 = [[2, 4, 5, 6], [3, 1, 2, 33], [6, 23, 21, 3], [3, 13, 5, 2]]
my_matrix_1 = Matrix(m1)
my_matrix_2 = Matrix(m2)
print(my_matrix_1 + my_matrix_2)

