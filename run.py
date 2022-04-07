from random import randint


def place_player_ships(player_board):
    """
    Here, the player places their ships on the board.
    Type an integer between 0-4
    (0 being the first row and column, and 4 being the fifth)
    to decide which row and which column to place the ship.
    """
    x = 0
    while x < 4:
        row = assert_integer_within_bounds(
            "Place your ship by entering a number between [0, 4]: ")
        column = assert_integer_within_bounds(
            "Place your ship by entering a number between [0, 4]: ")
        if player_board[row][column] == ".":
            player_board[row][column] = "@"
            print("Your ship has been placed")
            x = x + 1
        else:
            print("Error, a ship has already been placed there")


def assert_integer_within_bounds(message):
    """
    Reads an input, converts it into an integer and
    asserts that the integer is within bounds.
    """
    while True:
        user_input = input(message)
        if user_input.isnumeric():
            user_input = int(user_input)
        else:
            print("Please, enter a numeric value")
            continue
        if user_input >= 0 and user_input <= 4:
            return user_input
        else:
            print("Enter a value between 0 - 4")


def place_computer_ships(computer_board):
    """
    The computer places 4 ships on the computerboard by picking 4 random spaces
    to place their ships on. The integer is randomized between 0-4 (1-5)
    """
    for x in range(4):
        row = randint(0, 4)
        column = randint(0, 4)

        if computer_board[row][column] == ".":
            computer_board[row][column] = "@"
        else:
            x = x-1


def player_guess(computer_board):
    """
    The player makes the first guess by typing in two
    integers to decide which space to attack. If it hits,
    the dot turns into a "X", and if it misses, it turns into a "O"
    """
    guess_row = assert_integer_within_bounds("Enter a number between [0, 4]: ")
    guess_column = assert_integer_within_bounds("Enter a number between [0, 4]: ")

    if computer_board[guess_row][guess_column] == "@":
        computer_board[guess_row][guess_column] = "X"
        print("Congratulations, you hit a ship!")
    elif computer_board[guess_row][guess_column] == ".":
        computer_board[guess_row][guess_column] = "O"


def run_game(computer_board, player_board, username):
    """
    This function contains the game-loop,
    which controls the order of actions taken
    and when the game terminates
    """
    while not game_over(computer_board, player_board, username):
        player_guess(computer_board)
        computer_guess(player_board)
        print_boards(computer_board, player_board, username)


def computer_guess(player_board):
    """
    This function controls the
    behaviour of the computer
    """
    while True:
        rand_row = randint(0, 4)
        rand_col = randint(0, 4)

        if player_board[rand_row][rand_col] == "@":
            player_board[rand_row][rand_col] = "X"
            break

        elif player_board[rand_row][rand_col] == ".":
            player_board[rand_row][rand_col] = "O"
            break


def game_over(computer_board, player_board, username):
    """
    Checks if the game is finished and prints
    out the name of the winner
    """
    player_sunken_ship_count = 0
    computer_sunken_ship_count = 0

    for x in range(5):
        for y in range(5):
            if player_board[x][y] == "X":
                player_sunken_ship_count = player_sunken_ship_count + 1
            elif computer_board[x][y] == "X":
                computer_sunken_ship_count = computer_sunken_ship_count + 1

    print("PLAYER SUNKEN SHIP COUNT: ", player_sunken_ship_count)
    print("COMPUTER SUNKEN SHIP COUNT: ", computer_sunken_ship_count)

    if player_sunken_ship_count == 4:
        print("Computer wins")
        return True
    elif computer_sunken_ship_count == 4:
        print(username, " wins!")
        return True

    return False


def print_boards(computer_board, player_board, username):
    """
    Prints the player and computer boards which
    also serves as the battlefield
    """
    print(username, "'s board")

    for x in range(5):
        for y in range(5):
            print(player_board[x][y], end=" ")
        print("")

    print("Computer's board")

    for x in range(5):
        for y in range(5):
            current_pos = computer_board[x][y]
            if current_pos == '@':
                print(".", end=" ")
            else:
                print(current_pos, end=" ")
        print("")


def main():
    """ Main function
    """
    print("Welcome to Battleshipz v2")

    while True:
        username = input("Please enter your name (>5 characters): ")
        if username.strip() != '' and len(username) >= 5:
            break

    """
    Both boards where the game will be played on. The playerboard consists
    of 5x5 dots which are empty spaces on the board and the same applies
    for the computerboard.
    """

    player_board = [[".", ".", ".", ".", "."],
                    [".", ".", ".", ".", "."],
                    [".", ".", ".", ".", "."],
                    [".", ".", ".", ".", "."],
                    [".", ".", ".", ".", "."]]

    computer_board = [[".", ".", ".", ".", "."],
                      [".", ".", ".", ".", "."],
                      [".", ".", ".", ".", "."],
                      [".", ".", ".", ".", "."],
                      [".", ".", ".", ".", "."]]

    place_player_ships(player_board)
    place_computer_ships(computer_board)
    print_boards(computer_board, player_board, username)
    run_game(computer_board, player_board, username)


main()
