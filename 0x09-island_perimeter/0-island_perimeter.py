#!/usr/bin/python3
"""island perimeter"""
def island_perimeter(grid):
    """return perimeter of grid"""
    if not grid or not grid[0]:
        return 0

    row = len(grid)
    col = len(grid[0])
    perimeter = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == row - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == col - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
