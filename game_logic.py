from cli import clear_console

ship = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
ship_labels = {
    "carrier": "C",
    "battleship": "B",
    "cruiser": "R",
    "submarine": "S",
    "destroyer": "D"
}

def welcome():
    print("Welcome to the game!")

    def wait_for_input():
        input("Press Enter to start the game...\n")

    wait_for_input()
    clear_console()

def handle_place_ships(matrix, ship_name, direction, row, col):
    ship_length = ship[ship_name]
    if direction == "H":
        if col + ship_length > len(matrix[0]):
            print("Warning: Ship placement is out of horizontal bounds.")
            return matrix
        for i in range(ship_length):
            if matrix[row][col + i] != "~":
                existing_ship = matrix[row][col + i]
                existing_ship_name = dict_find_key_by_value(ship_labels, existing_ship)
                print(f"Warning: Position already occupied by {existing_ship_name}.")
                return matrix
        for i in range(ship_length):
            matrix[row][col + i] = ship_labels[ship_name]
    else:
        if row + ship_length > len(matrix):
            print("Warning: Ship placement is out of vertical bounds.")
            return matrix
        for i in range(ship_length):
            if matrix[row + i][col] != "~":
                existing_ship = matrix[row + i][col]
                existing_ship_name = dict_find_key_by_value(ship_labels, existing_ship)
                print(f"Warning: Position already occupied by {existing_ship_name}.")
                return matrix
        for i in range(ship_length):
            matrix[row + i][col] = ship_labels[ship_name]
    return matrix

def dict_find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None