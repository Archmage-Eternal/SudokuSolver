def is_empty(grid, loc):
    '''Functin to find an empty space in the grid.

    Args:
        grid (List): The complete Sucoku.
        loc (List): The coordinated of the empty space.

    Returns:
        Bool: True if the space is empty False if oherwise.
    '''
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                loc[0] = i
                loc[1] = j
            return True
    return False


def in_row(grid, row, num):
    '''Function to check whether the number is persent in the current row.

    Args:
        grid (List): Thw complete Sudoku.
        row (Integer): The row to be checked.
        num (Integer): The number for which we are performing the check.

    Returns:
        Bool: True if the number is present in the row and False otherwise.
    '''
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False


def in_cloumn(grid, column, num):
    '''Function to check whether the number is persent in the current column.

    Args:
        grid (List): Thw complete Sudoku.
        col (Integer): The column to be checked.
        num (Integer): The number for which we are performing the check.

    Returns:
        Bool: True if the number is present in the cloumn and False otherwise.
    '''
    for i in range(9):
        if grid[i][column] == num:
            return True
    return False


def in_box(grid, row, column, num):
    '''Function to check whether the number is persent in the box.

    Args:
        grid (List): The complete Sudoku.
        row (Integer): The row to be checked.
        column (Integer ): The cloumn to be checked.
        num (Integer): The number for which we are performing the check.

    Returns:
        Bool: True if the number is present in the box and False otherwise.
    '''
    for i in range(3):
        for j in range(3):
            if grid[row+i][column+j] == num:
                return True
    return False


def is_safe(grid, row, column, num):
    return not in_row(grid, row, num) and not in_cloumn(grid, column, num) and not in_box(grid, row - row % 3, column - column % 3, num)


def solver(grid):
    loc = [0, 0]
    row = loc[0]
    column = loc[1]
    if not is_empty(grid, loc):
        return True
    for num in range(1, 10):
        if is_safe(grid, row, column, num):
            grid[row][column] = num
            if solver(grid):
                return True
            grid[row][column] = 0
    return False


def print_sudoku(grid):
    for row in grid:
        print(row)


if __name__ == "__main__":
    grid = [[0 for _ in range(9)] for _ in range(9)]
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    if solver(grid):
        print_sudoku(grid)
    else:
        print('There is no valid solution')
