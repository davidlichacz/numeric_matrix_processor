class Matrix():
    def __init__(self):
        self.dimensions = None
        self.values = None

    def get_dimensions(self):
        self.dimensions = [int(dim) for dim in input().split()]

    def get_values(self):
        self.values = [[int(num) for num in input().split()] for i in range(self.dimensions[0])]

    def add_matrix(self, second_matrix):
        if self.dimensions != second_matrix.dimensions:
            print('ERROR')
        else:
            zipped = list(zip(self.values, second_matrix.values))
            pairs = [list(zip(a, b)) for (a, b) in zipped]
            summed = [list(map(sum, pair)) for pair in pairs]
            for row in summed:
                print(*row)

