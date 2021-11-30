from random import randint

print("Welcome to Battleshipz")

username = input("Enter Username:")

playerBoard = [[".", ".", ".",".","."], 
               [".", ".", ".",".","."], 
               [".", ".", ".",".","."], 
               [".", ".", ".",".","."], 
               [".", ".", ".",".","."]]

computerBoard = [[".", ".", ".",".","."], 
                 [".", ".", ".",".","."], 
                 [".", ".", ".",".","."], 
                 [".", ".", ".",".","."], 
                 [".", ".", ".",".","."]]


def placePlayerShips():
    row = int(input("Please, enter a row to place your ship on, 0-4:"))
    column = int(input("Please, enter a column to place your ship on, 0-4:"))
    playerBoard[row][column] = "@"
    if playerBoard = "."
        print("Your ship has been placed")
    else playerBoard = "@"
        print("Error, a ship has already been placed there")
    

#Konvertera input till en siffra
#Innan du placerar "@", kolla att det inte redan finns ett "@" där.


placePlayerShips()

placeComputerShips()

runGame()