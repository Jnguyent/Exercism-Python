class Matrix:
    def __init__(self, matrix_string):
        # Convert matrix string into a list within a list (a matrix)
        self.matrix = [[int(x) for x in row.split()] for row in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column_list = [row[index-1] for row in self.matrix]
        return column_list

