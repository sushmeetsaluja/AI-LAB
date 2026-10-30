def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def is_valid(grid, row, col, num):

    # Check row
    for j in range(9):
        if j != col and grid[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if i != row and grid[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if (i, j) != (row, col) and grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):

    # Find empty cell
    for row in range(9):
        for col in range(9):

            if grid[row][col] == -1:

                for num in range(1, 10):

                    if is_valid(grid, row, col, num):

                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        # Backtracking
                        grid[row][col] = -1

                return False

    return True


# Take input
print("Enter Sudoku (-1 for empty cells):")

grid = []

for i in range(9):
    while True:
        row = list(map(int, input(f"Row {i+1}: ").split()))

        if len(row) == 9 and all(-1 <= x <= 9 for x in row):
            grid.append(row)
            break

        print("Enter exactly 9 numbers between -1 and 9.")

# Validate original Sudoku
valid = True

for i in range(9):
    for j in range(9):
        num = grid[i][j]

        if num != -1:
            if not is_valid(grid, i, j, num):
                valid = False
                break

    if not valid:
        break

if not valid:
    print("Invalid Sudoku! Duplicate numbers found.")

else:
    if solve_sudoku(grid):
        print("\nSolved Sudoku:")
        print_grid(grid)
    else:
        print("\nNo solution exists!")

# OUTPUT
# Enter Sudoku (-1 for empty cells):
# Row 1: 5 3 -1 -1 7 -1 -1 -1 -1
# Row 2: 6 -1 -1 1 9 5 -1 -1 -1
# Row 3: -1 9 8 -1 -1 -1 -1 6 -1
# Row 4: 8 -1 -1 -1 6 -1 -1 -1 3
# Row 5: 4 -1 -1 8 -1 3 -1 -1 1
# Row 6: 7 -1 -1 -1 2 -1 -1 -1 6
# Row 7: -1 6 -1 -1 -1 -1 2 8 -1
# Row 8: -1 -1 -1 4 1 9 -1 -1 5
# Row 9: -1 -1 -1 -1 8 -1 -1 7 9

# Solved Sudoku:
# 5 3 4 6 7 8 9 1 2
# 6 7 2 1 9 5 3 4 8
# 1 9 8 3 4 2 5 6 7
# 8 5 9 7 6 1 4 2 3
# 4 2 6 8 5 3 7 9 1
# 7 1 3 9 2 4 8 5 6
# 9 6 1 5 3 7 2 8 4
# 2 8 7 4 1 9 6 3 5
# 3 4 5 2 8 6 1 7 9