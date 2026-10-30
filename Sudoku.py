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

        print("Enter exactly 9 numbers between 0 and 9.")

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
    print("\nOriginal Sudoku:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSolved Sudoku:")
        print_grid(grid)
    else:
        print("\nNo solution exists!")