from generators import generate_grid
from set_boats import set_boats
from menu_system import title, menu, how_to_play
from play_game import play_loop
from file_handlers import save_game, load_game, check_save_data

rounds = 0
boat_sizes = [5, 4, 3, 3, 2]

title()
how_to_play()
while True:
    choice = menu()

    if choice == 1:
        p1_boats = set_boats(generate_grid(), boat_sizes)
        p1_attack = generate_grid()

        p2_boats = set_boats(generate_grid(), boat_sizes)
        p2_attack = generate_grid()
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

    elif choice == 4:
        p1_boats = set_boats(generate_grid(), boat_sizes)
        p1_attack = generate_grid()

        p2_boats = set_boats(generate_grid(), boat_sizes)
        p2_attack = generate_grid()
        save_game(p1_boats, p1_attack, p2_boats, p2_attack, boat_sizes, rounds)
