#!/usr/bin/python3
"""
Pascal's triangle function
"""

def factorial(num):
    """obtaining factorial
    """
    if num == 0:
        return (1)
    else:
        return (num * factorial(num - 1))

def combination(n, k):
    """obtaining the combination formula
    """
    return (factorial(n) // (factorial (k) * factorial(n - k)))

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    new_list = []

    if n <= 0:
        return new_list

    for i in range(n):
        temp = []
        for j in range(i + 1):
            ans = combination(i, j)
            temp.append(ans)

        new_list.append(temp)

    return (new_list)
