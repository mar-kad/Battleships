from generators import generate_grid
from set_boats import set_boats
from menu_system import title, menu, how_to_play
from play_game import play_loop
from file_handlers import load_defaults, load_game, check_save_data
from os import environ

replit_env = False
if "REPL_OWNER" in environ:
    from replit import clear
    replit_env = True

rounds = 0
boat_sizes, boat_names = load_defaults()
title()
how_to_play(boat_sizes, boat_names)
while True:
    choice = menu()
    clear()

    if choice == 1:
        p1_boats = set_boats(generate_grid(), boat_sizes)
        p1_attack = generate_grid()
        if replit_env:
            clear()

        p2_boats = set_boats(generate_grid(), boat_sizes)
        p2_attack = generate_grid()
        if replit_env:
            clear()

        play_loop(p1_boats, p1_attack, p2_boats, p2_attack, rounds, boat_sizes)

    elif choice == 2:
        is_saved = check_save_data()
        if is_saved:
            p1_boats, p1_attack, p2_boats, p2_attack, boat_sizes, rounds = load_game()
            play_loop(p1_boats, p1_attack, p2_boats, p2_attack, rounds, boat_sizes)
        else:
            print("No save data found.")

    elif choice == 3:
        quit()
