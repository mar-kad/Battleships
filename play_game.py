from validators import valid_coords, is_hit, is_win
from time import sleep
from generators import display_grid, clear
from file_handlers import save_game, clear_save_data


def play_loop(p1_boats, p1_attack, p2_boats, p2_attack, rounds, boat_sizes, boat_names):
    win = False
    replay = True
    # loop game
    while replay:
        # get current players turn based on rounds
        current_player = player(rounds)
        print(f"------\nPlayer {current_player}'s Turn!")
        print("Enter co-ords to attack")
        # increment round
        rounds += 1
        # save game state
        save_game(p1_boats, p1_attack, p2_boats, p2_attack, boat_sizes, rounds)
        if current_player == 1:
            # display attack grid for P1
            display_grid(p1_attack)
            # get coords for attack and check valididity
            x, y = valid_coords()
            # check if hit
            is_hit(p2_boats, p1_attack, x, y, boat_names)
            # check if win
            win = is_win(boat_sizes, p2_boats)
            sleep(2)
            clear()
        elif current_player == 2:
            # display attack grid for P2
            display_grid(p2_attack)
            # get coords for attack and check valididity
            x, y = valid_coords()
            # check if hit
            is_hit(p1_boats, p2_attack, x, y, boat_names)
            # check if win
            win = is_win(boat_sizes, p1_boats)
            sleep(2)
            clear()

        if win:
            # if win condition is true, output winner, clear save game data and set reply to false to break loop
            replay = False
            print(f"\nPlayer {current_player} is the winner!")
            sleep(2)
            clear_save_data()
            clear()


def player(rounds):
    active_player = -1
    # use modulo to find current player based on rounds played
    if rounds % 2 == 0:
        active_player = 1
    else:
        active_player = 2

    return active_player
