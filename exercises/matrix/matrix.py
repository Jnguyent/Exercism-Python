class Matrix:
    def __init__(self, matrix_string):
        # Convert matrix string into a list within a list (a matrix)
        # .splitlines() makes a list of each linebreak
        self.matrix = matrix_string.splitlines()
        for i in range(0, len(self.matrix)):
            # .split() makes a list from each space
            self.matrix[i] = self.matrix[i].split()

    def row(self, index):
        row_list = self.matrix[index-1]
        for i in range(0, len(row_list)):
            # Convert strings into ints
            row_list[i] = int(row_list[i])
        return row_list

    def column(self, index):
        column_list = []
        for i in range(0, len(self.matrix)):
            # Append to column list and turn strings into ints
            column_list.append(int(self.matrix[i][index-1]))
        return column_list

