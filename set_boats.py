from validators import valid_coords, check_sequential
from generators import display_grid


def set_boats(grid, boat_sizes, boat_name):
    # for all boats in list boat_size
    for size in boat_sizes:

        # set valid as flag for checking valid position for boat placement
        valid = False
        while not valid:
            # initialise lists
            state = []  # holds current state of location
            pos = []  # holds to coords put in by the user

            valid = True  # if all the below tests pass, will not alter valid and break loop

            print(f"Enter x, y coordinates of boat size {size}")

            # for each boat section in current boat size
            for boat in range(int(size)):
                display_grid(grid)
                print(f"---\nBoat Placement for {boat_name[boat]} class ({size}). "
                      f"Set location for {boat_name[boat]} piece {boat + 1} of {size}")
                # store the return values of valid_coords which will be our coords x, y
                x, y = valid_coords()
                # append the current state of that location to our state list
                state.append(grid[x * 10 + y])
                # append the location itself to the pos list
                pos.append(x * 10 + y)

            # check if the location already has a boat in it
            for i in boat_sizes:
                if i in state:
                    valid = False
                    print("Not valid selections. Select again.")
                if not check_sequential(pos):
                    print("Not sequential. Boat piece placement must be in a straight line up/down or left/right.")
                    valid = False
                else:
                    # if valid, assign boat piece to that location
                    for i in pos:
                        grid[i] = boat + 1

            return grid


