from generators import generate_grid, display_grid
from validators import valid_int


def title():
    print("██████╗  █████╗ ████████╗████████╗██╗     ███████╗██████╗  ██████╗  █████╗ ████████╗███████╗██╗")
    print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██║")
    print("██████╔╝███████║   ██║      ██║   ██║     █████╗  ██████╔╝██║   ██║███████║   ██║   ███████╗██║")
    print("██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ██╔══██╗██║   ██║██╔══██║   ██║   ╚════██║╚═╝")
    print("██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗██████╔╝╚██████╔╝██║  ██║   ██║   ███████║██╗")
    print("╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝")


def how_to_play(sizes, name):

    print("\nWelcome to Battleboats!\n")
    display_grid(generate_grid())
    print(
        f"Each player hides ships on a grid containing vertical and horizontal space coordinates. \nPlayers take "
        f"turns typing out row and column coordinates on the other player's grid in an attempt to identify a location "
        f"that contains a ship.\n")
    print("Each player receives a game board and five ships of varying sizes.  The five ships are: \n")
    for i in range(len(sizes)):
        print(f"\t{sizes[i]}: {name[i]}")


def menu():
    options = ["New Game", "Load Game", "Quit"]

    print("\nChoose from the following options\n\t--------")

    for i in range(len(options)):
        print(f"\t{i + 1}: {options[i]}")

    return valid_int("\nEnter Selection: ", [1, 2, 3])
