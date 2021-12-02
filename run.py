from random import randint

print("Welcome to Battleshipz")

username = input("Enter Username:")

"""
Both boards where the game will be played on. The playerboard consists
of 5x5 dots which are empty spaces on the board and the same applies
for the computerboard.
"""

playerBoard = [[".", ".", ".",".","."], 
               [".", ".", ".",".","."], 
               [".", ".", ".",".","."], 
               [".", ".", ".",".","."], 
               [".", ".", ".",".","."]]

computerBoard = [[".", ".", ".", ".", ".",], 
                 [".", ".", ".", ".", "."], 
                 [".", ".", ".", ".", "."], 
                 [".", ".", ".", ".", "."], 
                 [".", ".", ".", ".", "."]]


def placePlayerShips():
    for x in range(4):
        row = int(input("Please, enter a row to place your ship on, 0-4:"))
        column = int(input("Please, enter a column to place your ship on, 0-4:"))
    

        if playerBoard[row][column] == ".":
            playerBoard[row][column] = "@"
            print("Your ship has been placed")

        else:
            print("Error, a ship has already been placed there")
        #Lägg till value error?
def placeComputerShips():
    for x in range(4):
        row = randint(0, 4)
        column = randint(0, 4)

        if computerBoard[row][column] == ".":
            computerBoard[row][column] = "@"
        else:
            x = x-1
            

def playerGuess():
    guessRow = int(input("Guess row:"))
    guessColumn = int(input("Guess column:"))

    if computerBoard[guessRow][guessColumn] == "@":
        computerBoard[guessRow][guessColumn] = "X"
        print("Congratulations, you hit a ship!")
    elif computerBoard[guessRow][guessColumn] == ".":
        computerBoard[guessRow][guessColumn] = "O"

    # Vad händer när spelaren har gjort sitt drag? Det är datorns tur.
    # Lösa alla utfall av gissningar.
    # Om jag träffar ett skepp (@), byts punkten ut mot ett (X), alltså träffat skepp.



def runGame():
    while not gameOver():
        playerGuess()
        computerGuess()
        printBoards()
        

def computerGuess():
    randRow = randint(0, 4)
    randColumn = randint(0, 4)

    if playerBoard[randRow][randColumn] == "@" or playerBoard[randRow][randColumn] == "X":
        playerBoard[randRow][randColumn] = "X"
        
    else:
        playerBoard[randRow][randColumn] = "O"

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
        print(username," wins!")
        return True
    print("PLAYER SUNKEN SHIP COUNT: ",player_sunkenShipCount)
    print("COMPUTER SUNKEN SHIP COUNT: ",computer_sunkenShipCount)

    return False
   

def printBoards():
    #Printing user board
    print(username,"'s board")
    
    for x in range(5):
        for y in range (5):
            print(playerBoard[x][y], end = " ")
        print("")
    #--------

    print("Computer's board")

    for x in range(5):
        for y in range(5):
            currentPos = computerBoard[x][y]
            if currentPos == '@':
                print(".", end = " ") #5 ska ersättas med .
            else:
                print(currentPos, end = " ")
        print("")
        # Skriv inte ut punkten utan att titta på den först

        # Ifall det finns ett skepp på den här punkten,
        # ska den inte skrivas ut.
        
        # Istället för skeppet(@) måste vi skriva ut punkter.

placePlayerShips()

placeComputerShips()

printBoards()

runGame()

#   . = Empty space
#   @ = Placed ship
#   X = Ship has been hit
#   O = Empty space has been hit