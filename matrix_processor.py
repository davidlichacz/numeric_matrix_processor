import copy


def float_or_int(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)


def dot_product(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


class Matrix:
    def __init__(self):
        self.dimensions = None
        self.values = None

    def get_dimensions(self):
        self.dimensions = [int(dim) for dim in input().split()]

    def get_values(self):
        self.values = [[float_or_int(num) for num in input().split()] for _ in range(self.dimensions[0])]

    def rows_to_columns(self):
        new = [[self.values[j][i] for j in range(len(self.values))] for i in range(len(self.values[0]))]
        return new

    def add_matrix(self, second_matrix):
        zipped = list(zip(self.values, second_matrix.values))
        pairs = [list(zip(a, b)) for (a, b) in zipped]
        summed = [list(map(sum, pair)) for pair in pairs]
        for row in summed:
            print(*row)

    def multiply_scalar(self, c):
        result = [[c * element for element in row] for row in self.values]
        for row in result:
            print(*row)

    def multiply_matrix(self, second_matrix):
        transpose = second_matrix.rows_to_columns()
        product = [[dot_product(row, col) for col in transpose] for row in self.values]
        for row in product:
            print(*row)

    def transpose(self, kind='main'):
        transpose = []
        if kind == 'main':
            transpose = self.rows_to_columns()
        elif kind == 'side':
            transpose = self.rows_to_columns()
            transpose.reverse()
            for row in transpose:
                row.reverse()
        elif kind == 'vertical':
            for row in self.values:
                row.reverse()
            transpose = self.values
        elif kind == 'horizontal':
            transpose = self.values
            transpose.reverse()
        new_matrix = Matrix()
        new_matrix.dimensions = self.dimensions
        new_matrix.values = transpose
        return new_matrix

    def determinant(self):
        if self.dimensions == [1, 1]:
            return self.values[0][0]
        if self.dimensions == [2, 2]:
            return (self.values[0][0] * self.values[1][1]) - (self.values[0][1] * self.values[1][0])
        else:
            determinant = 0
            first_row = self.values[0]
            del self.values[0]

            for col in range(self.dimensions[0]):
                minor = Matrix()
                minor.dimensions = [self.dimensions[0] - 1, self.dimensions[1] - 1]
                minor.values = copy.deepcopy(self.values)
                for row in minor.values:
                    del row[col]
                cofactor = (-1) ** (2 + col)
                determinant += (cofactor * first_row[col] * minor.determinant())
            return determinant

    def inverse(self):
        copy_matrix = copy.deepcopy(self)
        det = copy_matrix.determinant()
        if det == 0:
            print("This matrix doesn't have an inverse.")
        else:
            coeff = 1 / det
            if self.dimensions == [1, 1]:
                value = self.values[0][0]
                print([[1 / value]])
            else:
                cof_matrix = Matrix()
                cof_matrix.dimensions = self.dimensions
                cof_matrix.values = []
                for row in range(self.dimensions[0]):
                    new_row = []
                    for col in range(self.dimensions[1]):
                        minor = Matrix()
                        minor.dimensions = [self.dimensions[0] - 1, self.dimensions[1] - 1]
                        minor.values = copy.deepcopy(self.values)
                        del minor.values[row]
                        for minor_row in minor.values:
                            del minor_row[col]
                        new_row.append((-1) ** (row + col + 2) * minor.determinant())
                    cof_matrix.values.append(new_row)
                cof_trans = cof_matrix.transpose()
                cof_trans.multiply_scalar(coeff)


def get_matrix(order='', operation=None, previous=None):
    if order:
        order = ' ' + order
    matrix = Matrix()
    print(f'Enter size of{order} matrix')
    matrix.get_dimensions()

    if previous:
        if operation == 'add':
            if matrix.dimensions != previous.dimensions:
                return None
        elif operation == 'multiply':
            if matrix.dimensions[0] != previous.dimensions[1]:
                return None

    print('Enter matrix:')
    matrix.get_values()

    return matrix


options = ['1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices',
           '4. Transpose matrix', '5. Calculate a determinant', '6. Inverse matrix', '0. Exit']

while True:
    print(*options, sep='\n')
    print('Your choice:')
    choice = int(input())
    if choice == 1:
        matrix_a = get_matrix(order='first')
        matrix_b = get_matrix(order='second', operation='add', previous=matrix_a)

        if not matrix_b:
            print('The operation cannot be performed.')
            continue

        print('The result is:')
        matrix_a.add_matrix(matrix_b)

        continue

    elif choice == 2:
        matrix_a = get_matrix()

        print('Enter constant:')
        scalar = float_or_int(input())

        print('The result is:')
        matrix_a.multiply_scalar(scalar)

        continue

    elif choice == 3:
        matrix_a = get_matrix(order='first')
        matrix_b = get_matrix(order='second', operation='multiply', previous=matrix_a)

        if not matrix_b:
            print('The operation cannot be performed.')
            continue

        print('The result is:')
        matrix_a.multiply_matrix(matrix_b)

        continue

    elif choice == 4:
        transpose_options = ['1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line']
        transpose_kinds = {1: 'main', 2: 'side', 3: 'vertical', 4: 'horizontal'}
        print(*transpose_options, sep='\n')
        transpose_choice = int(input())

        matrix_a = get_matrix()
        transposed = matrix_a.transpose(kind=transpose_kinds[transpose_choice])
        for row in transposed.values:
            print(*row)

        continue

    elif choice == 5:
        matrix_a = get_matrix()

        print('The result is:')
        print(matrix_a.determinant())

    elif choice == 6:
        matrix_a = get_matrix()
        matrix_a.inverse()

        continue

    elif choice == 0:
        break
    else:
        break
