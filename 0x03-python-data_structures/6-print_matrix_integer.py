#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return

    for row in matrix:
        row_str = ""
        for item in row:
            row_str += "{:d} ".format(item)
        print(row_str[:-1])

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
