#!/usr/bin/python3
""" Making change"""


def makeChange(coins, total):
    """using greedy algorithm to solve
    minimum number of coins
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coins_needed = 0
    remainder = total

    for c in coins:
        if c <= remainder:
            coins_needed += remainder // c
            remainder %= c

    if remainder == 0:
        return coins_needed
    else:
        return -1
