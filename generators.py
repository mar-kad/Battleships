import os
import subprocess
import replit


def generate_grid():
    return ["~" for i in range(100)]


def display_grid(grid):
    print("    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ")
    print("    +---------------------------------------+ ")
    for i in range(10):
        print(
            f" {i}  | {grid[i * 10]} | {grid[i * 10 + 1]} | {grid[i * 10 + 2]} | {grid[i * 10 + 3]} | "
            f"{grid[i * 10 + 4]} | {grid[i * 10 + 5]} | {grid[i * 10 + 6]} | "
            f"{grid[i * 10 + 7]} | {grid[i * 10 + 8]} | {grid[i * 10 + 9]} | ")

    print("")


def clear():
    # TODO fix...
    if "REPL_OWNER" in os.environ:
        replit.clear()


    '''elif os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120'''
