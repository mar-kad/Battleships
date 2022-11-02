def valid_coords():
    valid_xy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid_input = False

    while not valid_input:
        try:
            x_coord = int(input("Enter X coord: "))
            y_coord = int(input("Enter Y coord: "))
            # check if the player input is NOT in our valid list. If TRUE, ask for another input
            if x_coord in valid_xy and y_coord in valid_xy:
                valid_input = True
            else:
                print("Not valid")
        except ValueError:
            print("ERROR: Must be a number.")

    return x_coord, y_coord


def check_sequential(coords):
    coords.sort()
    # print(f"\n---\nDEBUG: cords are  {coords}\n---\n")
    valid = True
    size = len(coords)  # get size of boat from length of coords list
    start_co = coords[0]
    valid_check = []
    # starting from the 2nd position in the list, check if the boat size is next or below it, iteratively
    for i in range(1, size):
        if coords[i] == (start_co + i) or start_co + (10 * i) % 100 == coords[i]:
            valid_check.append(True)
        else:
            valid_check.append(False)

    if False in valid_check:
        valid = False

    return valid


def is_hit(boats, attack_map, x, y, boat_names):
    # TODO breakdown options so stop overwriting already hit boats
    options = ['X', 'O', '~']
    if boats[y * 10 + x] not in options:
        print(f"-------\nHIT at {x}/{y}: {boat_names[int(boats[y*10+x])]}: {boats[y * 10 + x]}")
        hit = True
        attack_map[y * 10 + x] = 'X'
        boats[y * 10 + x] = 'X'
    else:
        print(f"-------\nMISS at {x}/{y}: {boats[y * 10 + x]}")
        hit = False
    attack_map[y * 10 + x] = 'O'
    boats[y * 10 + x] = 'O'

    return hit


def is_win(boat_types, grid):
    # check if a boat piece if in the list. if not, then win condition is met as all boats have been destroyed
    win = True

    for boat in boat_types:
        for j in grid:
            if j == boat:
                win = False
    return win


def valid_int(text, options):
    # general valid int type check
    not_valid = True

    while not_valid:
        try:
            sel = input(text)
            if int(sel) in options:
                return int(sel)
            else:
                print("Number must be within the options give")
        except ValueError:
            print("Error: Must be a number. Try again")
