def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def is_valid(grid, row, col, num):

    # Check the row
    for j in range(9):
        if grid[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Find the top-left corner of the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Check the 3x3 subgrid
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):

    # Find an empty cell
    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                # Try digits 1 through 9
                for num in range(1, 10):

                    if is_valid(grid, row, col, num):

                        # Place the number
                        grid[row][col] = num

                        # Solve the remaining puzzle
                        if solve_sudoku(grid):
                            return True

                        # Backtrack if the choice fails
                        grid[row][col] = 0

                # No number works in this cell
                return False

    # No empty cells remain
    return True


# Take input from the user
print("Enter the Sudoku grid row by row.")
print("Use 0 for empty cells.")

grid = []

for i in range(9):
    while True:
        row = list(map(
            int,
            input(f"Enter row {i + 1} (9 digits separated by spaces): ").split()
        ))

        if len(row) == 9 and all(0 <= x <= 9 for x in row):
            grid.append(row)
            break

        print("Invalid input. Enter exactly 9 digits from 0 to 9.")

print("\nOriginal Sudoku:")
print_grid(grid)

if solve_sudoku(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
else:
    print("\nNo solution exists for this Sudoku.")