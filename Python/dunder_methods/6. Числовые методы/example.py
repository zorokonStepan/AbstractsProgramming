class Matrix:
    def __init__(self, rows):
        if len(set(len(row) for row in rows)) > 1:
            raise ValueError("Bce строки матрицы должны быть одинаковой длины")
        self.rows = rows

    def __add__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Paзмepы матриц не совпадают")
        return Matrix([[a + b for a, b in zip(a_row, b_row)] for a_row, b_row in zip(self.rows, other.rows)])

    def __sub__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Paзмepы матриц не совпадают")
        return Matrix([[a - b for a, b in zip(a_row, b_row)] for a_row, b_row in zip(self.rows, other.rows)])

    def __mul__(self, other):
        if isinstance(other, Matrix):

            if len(self.rows[0]) != len(other.rows):
                raise ValueError("Размеры матриц не совпадают")

            rows = [[0 for _ in other.rows[0]] for _ in self.rows]

            for i in range(len(self.rows)):
                for j in range(len(other.rows[0])):
                    for k in range(len(other.rows)):
                        rows[i][j] += self.rows[i][k] * other.rows[k][j]

            return Matrix(rows)

        elif isinstance(other, int):
            return Matrix([[item * other for item in row] for row in self.rows])

        else:
            raise TypeError(f"Нельзя умножить {type(other)} на Matrix")

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other


if __name__ == "__main__":
    m1 = Matrix([
        [1, 2],
        [3, 4]
    ])

    m2 = Matrix([
        [11, 22],
        [33, 44]
    ])

    assert (m1 + m2).rows == [[12, 24], [36, 48]]
    assert (m1 - m2).rows == [[-10, -20], [-30, -40]]
    assert (m1 * m2).rows == [[77, 110], [165, 242]]
    assert (m1 * 5).rows == [[5, 10], [15, 20]]
    assert (5 * m1).rows == [[5, 10], [15, 20]]
