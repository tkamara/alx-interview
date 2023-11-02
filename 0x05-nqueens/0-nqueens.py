#!/usr/bin/python3

import sys


def safe_queen(row, col, b):
    """checking rows and left and right diagonals"""
    for x in range(row):
        if b[x][1] == col or b[x][1] - x == col - row \
                or b[x][1] + x == col + row:
            return False
    return True

def det_nqueens(n):
    """determining the possible positions"""
    possible = []

    def backtrack(row, board):
        """using backtracking algorithm"""
        if row == n:
            possible.append(board[:])
            return

        for col in range(n):
            if safe_queen(row, col, board):
                board.append([row, col])
                backtrack(row + 1, board)
                board.pop()

    board = []
    backtrack(0, board)

    return possible

def printer(possible):
    """displaying the lists"""
    for y in possible:
        print(y)
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
        
    ans = det_nqueens(N)
    printer(ans)
