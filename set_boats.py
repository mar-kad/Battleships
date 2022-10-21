from validators import valid_coords, check_sequential


def set_boats(grid, boat_sizes):
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
            for boat in range(size):
                print(f"---\nBoat Placement: {boat + 1}/{size}")
                # store the return values of valid_coords which will be our coords x, y
                x, y = valid_coords()
                # append the current state of that location to our state list
                state.append(grid[x * 10 + y])
                # append the location itself to the pos list
                pos.append(x * 10 + y)

            for i in boat_sizes:
                if i in state:
                    valid = False
                    print("Not valid selections. Select again.")
            if not check_sequential(pos):
                print("Not sequential")
                valid = False
            else:
                for i in pos:
                    grid[i] = boat + 1

    return grid


