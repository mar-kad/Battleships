from validators import valid_coords, is_hit, is_win
from time import sleep
from generators import display_grid
from file_handlers import save_game, clear_save_data


def play_loop(p1_boats, p1_attack, p2_boats, p2_attack, rounds, boat_sizes):
    win = False
    replay = True
    while replay:

        current_player = player(rounds)
        print(f"Player {current_player}'s Turn!")
        print("Enter co-ords to attack")
        if current_player == 1:
            display_grid(p1_attack)
            x, y = valid_coords()
            is_hit(p2_boats, p1_attack, x, y)
            win = is_win(boat_sizes, p2_boats)
        elif current_player == 2:
            display_grid(p2_attack)
            x, y = valid_coords()
            is_hit(p1_boats, p2_attack, x, y)
            win = is_win(boat_sizes, p1_boats)

        rounds += 1
        save_game(p1_boats, p1_attack, p2_boats, p2_attack, boat_sizes, rounds)

        sleep(2)

        if win:
            replay = False
            print(f"Player {current_player} is the winner!")
            clear_save_data()


def player(rounds):
    active_player = -1
    # use modulo to find current player based on rounds played
    if rounds % 2 == 0:
        active_player = 1
    else:
        active_player = 2

    return active_player
