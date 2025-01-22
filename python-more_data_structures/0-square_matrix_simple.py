#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    empty_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j ** 2)
        empty_matrix.append(row)
    return empty_matrix
