def generate_grid():
    return ["~" for i in range(100)]


def display_grid(grid):
    print("    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ")
    print("    +---------------------------------------+ ")
    for i in range(10):
        print(
            f" {i}  | {grid[i * 10]} | {grid[i * 10 + 1]} | {grid[i * 10 + 2]} | {grid[i * 10 + 3]} | {grid[i * 10 + 4]} | {grid[i * 10 + 5]} | {grid[i * 10 + 6]} | {grid[i * 10 + 7]} | {grid[i * 10 + 8]} | {grid[i * 10 + 9]} | ")

    print("")
