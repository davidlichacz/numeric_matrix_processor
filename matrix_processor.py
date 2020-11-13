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
        # Rearrange second matrix into columns.
        columns = [[second_matrix.values[j][i] for j in range(len(second_matrix.values))]
                   for i in range(len(second_matrix.values[0]))]
        product = [[dot_product(row, col) for col in columns] for row in self.values]
        for row in product:
            print(*row)


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
           '0. Exit']

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

    elif choice == 0:
        break
    else:
        break
