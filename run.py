from random import randint

print("Welcome to Battleshipz")

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

"""
Here, the player places their ships on the board. Type an integer between 0-4
(0 being the first row and column, and 4 being the fifth) to decide which
row and which column to place the ship.
"""
def placePlayerShips():
    for x in range(4):
        row = assertIntegerWithinBounds("Please, enter a number between 0-4:")
        column = assertIntegerWithinBounds("Please, enter a number between 0-4:")
        
        if playerBoard[row][column] == ".":
            playerBoard[row][column] = "@"
            print("Your ship has been placed")

        else:
            print("Error, a ship has already been placed there")
        # Lägg till value error?

def assertIntegerWithinBounds(message):

    while True:
	    userInput = input(message)
	    if userInput.isnumeric():
		    userInput = int(userInput)
		    if userInput >= 0 and userInput <= 4:
			    return userInput
		    else:
			    print("Enter a value between 0 - 4")
	    else :
		    print("Please, enter a numeric value")
    

"""
The computer places 4 ships on the computerboard by picking 4 random spaces
to place their ships on. The integer is randomized between 0-4 (1-5)
"""
def placeComputerShips():
    for x in range(4):
        row = randint(0, 4)
        column = randint(0, 4)
        
        if computerBoard[row][column] == ".":
            computerBoard[row][column] = "@"
        else:
            x = x-1
            
"""
The player makes the first guess by typing in two 
integers to decide which space to attack. If it hits,
the dot turns into a "X", and if it misses, it turns into a "O"
"""
def playerGuess():
    guessRow = assertIntegerWithinBounds("Please, enter a number between 0-4:")
    guessColumn = assertIntegerWithinBounds("Please, enter a number between 0-4:")

    if computerBoard[guessRow][guessColumn] == "@":
        computerBoard[guessRow][guessColumn] = "X"
        print("Congratulations, you hit a ship!")
    elif computerBoard[guessRow][guessColumn] == ".":
        computerBoard[guessRow][guessColumn] = "O"

# Vad händer när spelaren har gjort sitt drag? Det är datorns tur.
# Lösa alla utfall av gissningar.
# Om jag träffar ett skepp (@), byts punkten ut mot ett (X),
# alltså träffat skepp.
def runGame():
    while not gameOver():
        playerGuess()
        computerGuess()
        printBoards()
        

def computerGuess():
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
    # Printing user board
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
        # Don't show the dot unless it has been checked first

        # If there is a ship place on this dot,
        # it shall not be printed.
        
        # Instead of a ship(@) on the computerboard
        # there but be a dot(.) to hide the location for the player.

placePlayerShips()

placeComputerShips()

printBoards()

runGame()

#   . = Empty space
#   @ = Placed ship
#   X = Ship has been hit
#   O = Empty space has been hit

# Datorn ska ej kunna gissa på samma
# 