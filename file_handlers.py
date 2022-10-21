def save_game(p1_boats, p1_attack, p2_boats, p2_attack, boat_sizes, rounds):
    with open('saves/game_save.csv', 'w') as file:
        str_list = []

        for item in p1_boats:
            str_list.append(str(item))
            p1b = ",".join(str_list)

        file.write(f"{p1b}\n")
        str_list = []

        for item in p1_attack:
            str_list.append(str(item))
            p1a = ",".join(str_list)

        file.write(f"{p1a}\n")
        str_list = []

        for item in p2_boats:
            str_list.append(str(item))
            p2b = ",".join(str_list)

        file.write(f"{p2b}\n")
        str_list = []

        for item in p2_attack:
            str_list.append(str(item))
            p2a = ",".join(str_list)

        file.write(f"{p2a}\n")
        str_list = []

        for item in boat_sizes:
            str_list.append(str(item))
            bs = ",".join(str_list)

        str_list = []
        file.write(f"{bs}\n")
        file.write(f"{str(rounds)}\n")


def load_game():
    with open('saves/game_save.csv') as file:
        data = []

        for line in file:
            line = line.strip()
            line = line.split(",")
            data.append(line)

        rounds = int(data[5][0])
        print(f"DEBUG: {type(rounds)}")

    return data[0], data[1], data[2], data[3], data[4], rounds


def clear_save_data():
    with open('saves/game_save.csv', 'w') as file:
        file.write('-1')


def check_save_data():
    with open('saves/game_save.csv', 'r') as file:
        data = file.readline()
        if int(data) != -1:
            return True

