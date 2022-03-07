from random import randint

print("Welcome to Battleshipz v2")

username = input("Enter Username:")

"""
Both boards where the game will be played on. The playerboard consists
of 5x5 dots which are empty spaces on the board and the same applies
for the computerboard.
"""

playerBoard = [[".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."],
               [".", ".", ".", ".", "."]]

computerBoard = [[".", ".", ".", ".", "."],
                 [".", ".", ".", ".", "."],
                 [".", ".", ".", ".", "."],
                 [".", ".", ".", ".", "."],
                 [".", ".", ".", ".", "."]]


def placePlayerShips():
    """
    Here, the player places their ships on the board.
    Type an integer between 0-4
    (0 being the first row and column, and 4 being the fifth)
    to decide which row and which column to place the ship.
    """
    x = 0
    while x < 4:
        row = assertIntegerWithinBounds("Enter a number between 0-4:")
        column = assertIntegerWithinBounds("Enter a number between 0-4:")
        if playerBoard[row][column] == ".":
            playerBoard[row][column] = "@"
            print("Your ship has been placed")
            x = x+1
        else:
            print("Error, a ship has already been placed there")


def assertIntegerWithinBounds(message):
    """
    Reads an input, converts it into an integer and
    asserts that the integer is within bounds.
    """
    while True:
        userInput = input(message)
        if userInput.isnumeric():
            userInput = int(userInput)

        else:
            print("Please, enter a numeric value")
            continue
        if userInput >= 0 and userInput <= 4:
            return userInput
        else:
            print("Enter a value between 0 - 4")


def placeComputerShips():
    """
    The computer places 4 ships on the computerboard by picking 4 random spaces
    to place their ships on. The integer is randomized between 0-4 (1-5)
    """
    for x in range(4):
        row = randint(0, 4)
        column = randint(0, 4)

        if computerBoard[row][column] == ".":
            computerBoard[row][column] = "@"
        else:
            x = x-1


def playerGuess():
    """
    The player makes the first guess by typing in two
    integers to decide which space to attack. If it hits,
    the dot turns into a "X", and if it misses, it turns into a "O"
    """
    guessRow = assertIntegerWithinBounds("Enter a number between 0-4:")
    guessColumn = assertIntegerWithinBounds("Enter a number between 0-4:")

    if computerBoard[guessRow][guessColumn] == "@":
        computerBoard[guessRow][guessColumn] = "X"
        print("Congratulations, you hit a ship!")
    elif computerBoard[guessRow][guessColumn] == ".":
        computerBoard[guessRow][guessColumn] = "O"


def runGame():
    """
    This function contains the game-loop,
    which controls the order of actions taken
    and when the game terminates
    """
    while not gameOver():
        playerGuess()
        computerGuess()
        printBoards()


def computerGuess():
    """
    This function controls the
    behaviour of the computer
    """
    while True:
        randRow = randint(0, 4)
        randCol = randint(0, 4)

        if playerBoard[randRow][randCol] == "@":
            playerBoard[randRow][randCol] = "X"
            break

        elif playerBoard[randRow][randCol] == ".":
            playerBoard[randRow][randCol] = "O"
            break


def gameOver():
    """
    Checks if the game is finished and prints
    out the name of the winner
    """
    player_sunkenShipCount = 0
    computer_sunkenShipCount = 0

    for x in range(5):
        for y in range(5):
            if playerBoard[x][y] == "X":
                player_sunkenShipCount = player_sunkenShipCount + 1
            elif computerBoard[x][y] == "X":
                computer_sunkenShipCount = computer_sunkenShipCount + 1

    if player_sunkenShipCount == 4:
        print("Computer wins")
        return True
    elif computer_sunkenShipCount == 4:
        print(username, " wins!")
        return True
    print("PLAYER SUNKEN SHIP COUNT: ", player_sunkenShipCount)
    print("COMPUTER SUNKEN SHIP COUNT: ", computer_sunkenShipCount)

    return False


def printBoards():
    """
    Prints the player and computer boards which
    also serves as the battlefield
    """
    print(username, "'s board")

    for x in range(5):
        for y in range(5):
            print(playerBoard[x][y], end=" ")
        print("")
    # --------

    print("Computer's board")

    for x in range(5):
        for y in range(5):
            currentPos = computerBoard[x][y]
            if currentPos == '@':
                print(".", end=" ")  # 5 is replaced by .
            else:
                print(currentPos, end=" ")
        print("")


placePlayerShips()

placeComputerShips()

printBoards()

runGame()

#   . = Empty space
#   @ = Placed ship
#   X = Ship has been hit
#   O = Empty space has been hit
