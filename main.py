from generators import generate_grid, clear
from set_boats import set_boats
from menu_system import title, menu, how_to_play
from play_game import play_loop
from file_handlers import load_defaults, load_game, check_save_data

rounds = 0
boat_sizes, boat_names = load_defaults()
title()
how_to_play(boat_sizes, boat_names)

while True:
    choice = menu()

    if choice == 1:
        clear()
        p1_boats = set_boats(generate_grid(), boat_sizes, boat_names)
        p1_attack = generate_grid()

        clear()
        p2_boats = set_boats(generate_grid(), boat_sizes, boat_names)
        p2_attack = generate_grid()

        clear()
        play_loop(p1_boats, p1_attack, p2_boats, p2_attack, rounds, boat_sizes, boat_names)

    elif choice == 2:
        if check_save_data():
            p1_boats, p1_attack, p2_boats, p2_attack, boat_sizes, rounds = load_game()
            play_loop(p1_boats, p1_attack, p2_boats, p2_attack, rounds, boat_sizes, boat_names)
        else:
            print("No save data found.")

    elif choice == 3:
        print("\n-----\nGoodbye!")
        quit()
