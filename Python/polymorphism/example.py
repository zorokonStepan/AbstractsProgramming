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
        if not isinstance(other, Matrix):
            raise TypeError(f"He определено умножение типов {type(other)} и Matrix")

        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Размеры матриц не совпадают")

        rows = [[0 for _ in other.rows[0]] for _ in self.rows]
        for i in range(len(self.rows)):
            for j in range(len(other.rows[0])):
                for k in range(len(other.rows)):
                    rows[i][j] += self.rows[i][k] * other.rows[k][j]
        return Matrix(rows)
