#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    operations = 0
    copy = 0
    complete = 1

    while complete < n:
        if copy == 0 or (n % complete) == 0:
            copy = complete
            complete += copy
            operations += 2
        elif copy > 0:
            complete += copy
            operations += 1

    return operations
