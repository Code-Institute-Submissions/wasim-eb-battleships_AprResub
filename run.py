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
    row = input("Please, enter a row to place your ship on, 0-4:")
    column = input("Please, enter a column to place your ship on, 0-4:")
    playerBoard[row][column] = "@"


placePlayerShips()

placeComputerShips()

runGame()