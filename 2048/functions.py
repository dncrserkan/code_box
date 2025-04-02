''' FUNCTIONS - GAME LOGIC '''

import numpy as np



def rotate(grid, dir):
    ''' 
    Rotating the matrix 90 degrees clockwise
    We want to make all actions with same function and rotate it again
    '''
    for _ in range(dir):
        grid = np.rot90(grid, k=1)
    return grid



def move(grid, dir):
    '''
    Slide and Merge Blocks'
    '''

    merged = False
    grid = rotate(grid, dir)

    for i in range(4):
        row = grid[i][grid[i] != 0]                             # Select non-zeros
        row = np.append(row, [0] * (4 - len(row)))              # Add them (zeros) to the end

        # Merging
        for j in range(3):
            if row[j] == row[j + 1] and row[j] != 0:
                merged = True
                row[j] *= 2
                move.score += row[j]
                row[j + 1:] = np.append(row[j + 2:], [0])

        grid[i] = row                                           # Update row

    grid = rotate(grid, 4-dir)
    return grid, merged



def addNumber(grid):
    '''
    Add 2 or 4 to a random empty cell and tell about reamining empty cells
    returns : updated grid
    '''
    empty_cells = np.argwhere(grid == 0)
    empty_count = empty_cells.size // empty_cells.ndim          # .size gives all single x and y but we need the count of (x,y)'s
    
    if empty_count > 0:
        x, y = empty_cells[np.random.choice(empty_count)]     
        grid[x, y] = np.random.choice(np.array([2, 4]))
    return grid                                                 # No Empty Grid Game Over



def create_new_grid():
    grid = np.zeros(shape=(4,4), dtype=int)
    for _ in range(6):
        addNumber(grid)
    return grid



def check_game_over(grid):
    # Check for empty box
    if np.any(grid==0):
        return False

    rows, cols = grid.shape

    # Check for possible moves in rows
    for row in range(rows-1):
        if any(grid[row]==grid[row+1]):
            return False

    # Check for possible moves in columns
    for col in range(cols-1):
        if any(grid[:, col]==grid[:, col+1]):
            return False

    return True

