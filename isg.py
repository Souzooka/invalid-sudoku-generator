# Inspired by Games Explosion! for the Gameboy Advance
import random
from typing import List, Tuple

def check_conflict(grid: List[List[int]], x: int, y: int, n: int) -> bool:
    # check row and column
    if any(i == n for i in grid[x]):
        return True
    
    for i in range(9):
        if n == grid[i][y]:
            return True
        
    # Subcells
    low_x = (x // 3) * 3
    low_y = (y // 3) * 3

    for i in [
        grid[low_x][low_y], grid[low_x][low_y + 1], grid[low_x][low_y + 2],
        grid[low_x + 1][low_y], grid[low_x + 1][low_y + 1], grid[low_x + 1][low_y + 2],
        grid[low_x + 2][low_y], grid[low_x + 2][low_y + 1], grid[low_x + 2][low_y + 2],
    ]:
        if i == n:
            return True
    
    return False

def pick_cell(subgrid: int) -> Tuple[int, int]:
    low_x = subgrid % 3 * 3
    low_y = subgrid // 3 * 3
    return (low_x + random.randint(0, 2), low_y + random.randint(0, 2))

def print_grid(grid: List[List[int]]) -> None:
    for x in range(9):
        if x != 0 and x % 3 == 0:
            print("-----------")

        for y in range(9):
            if y != 0 and y % 3 == 0:
                print("|", end="")

            if grid[x][y] != -1:
                print(f"{grid[x][y]}", end="")
            else:
                print(" ", end="")
        print("\n", end="")

def main():
    difficulty = 0
    while True:
        diff_in = input("Please enter a difficulty (0=Easy, 1=Medium, 2=Hard): ")
        
        try:
            difficulty = int(diff_in)
        except ValueError:
            # User put in non-int
            continue

        if not 0 <= difficulty <= 2:
            print("Invalid difficulty!")
            continue

        break

    numbers_per_cell = 4 - difficulty

    # Initialize Sudoku Grid
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append(-1)

    # Make sure we're putting in unique values
    pool = [*range(1, 9 + 1)]
    
    # Place random numbers in the subgrid
    for subgrid in range(9):
        nums_placed = 0
        picked_cells = set()
        while nums_placed < numbers_per_cell:
            x, y = pick_cell(subgrid)
            while (x, y) in picked_cells:
                x, y = pick_cell(subgrid)

            picked_cells.add((x, y))

            n = random.choice(pool)
            if check_conflict(grid, x, y, n):
                continue
            grid[x][y] = n
            nums_placed += 1

            if len(pool) == 0:
                pool = [*range(1, 9 + 1)]

    print("Your (probably logically insolvable) Sudoku grid is:")
    print_grid(grid)

main()
