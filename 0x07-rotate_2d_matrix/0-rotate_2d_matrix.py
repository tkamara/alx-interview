#!/usr/bin/python3
"""rotating 2D matrix in-place"""
import copy

def rotate_2d_matrix(matrix):
    """rotating n x n matrix 90 degrees clockwise"""
    n = len(matrix)

    # transpose of matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reversing matrix rows in place
    for i in range(n):
        matrix[i].reverse()
