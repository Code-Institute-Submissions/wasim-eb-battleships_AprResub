from random import randint

print("Welcome to Battleshipz")

username = input("Enter Username:")

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
            print("conflict")
            x = x-1
            



def playerGuess():
    guessRow = int(input("Guess row:"))
    guessColumn = int(input("Guess column:"))
    # Lösa alla utfall av gissningar. 
    # Om jag träffar ett skepp (@), byts punkten ut mot ett (X), alltså träffat skepp.



def runGame():
    print("ellenåtsånt")


def printBoards():

    print(username,"'s board")
    
    for x in range(5):
        print(playerBoard[x])


    print("Computer's board")

    for x in range(5):
        print(computerBoard[x])
        # Skriv inte ut punkten utan att titta på den först

        # Ifall det finns ett skepp på den här punkten, 
        # ska den inte skrivas ut. 
        
        # Istället för skeppet(@) måste vi skriva ut punkter.

placePlayerShips()

placeComputerShips()

printBoards()
# runGame()

#   . = tom ruta
#   @ = placerat skepp
#   X = träffat skepp
#   O = träffa luft