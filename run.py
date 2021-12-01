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
            x = x-1
            



def playerGuess():
    guessRow = int(input("Guess row:"))
    guessColumn = int(input("Guess column:"))





def runGame()

#Konvertera input till en siffra
#Innan du placerar "@", kolla att det inte redan finns ett "@" där.


placePlayerShips()

placeComputerShips()

runGame()