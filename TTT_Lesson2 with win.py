# Tic Tac Toe

import random
import time

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset and create the board, an array of characters to represent each position
    # For simplicity we're going to ignore index 0
    theBoard = [' '] * 10
    # Set the game state to playing. 
    gameIsPlaying = True
    # Draw the empty game board
    drawBoard(theBoard)
    #Player marker O or X
    playerMarker = ' '

    print('YOUR_NAME - Tic-Tac-Toe Project.')
    print('---------------------------------------------')

    playerMarker = input("Choose your marker X/O")
    if playerMarker != 'X' or 'x' or 'o' or 'O' :
        print("Invalid marker; X or O ")
        playerMarker = input("Choose your marker X/O")

    #Cast out inputs to the correct variable type remember!
    move = int(input('Choose a position (1 - 9)'))

    def CheckMove(pos):
        if theBoard[pos] != ' ':
            print("Can't go here!")
            return False
        else:
            return True

    def CheckWin(GameBoard):
        if GameBoard[7] == 'X' and GameBoard[8] == 'X' and GameBoard[9] == 'X' :#Check top row
            print("YOU WIN!")
            
            
        if GameBoard[4] == 'X' and GameBoard[5] == 'X' and GameBoard[6] == 'X' :#Check middle row
            print("YOU WIN!")
            

        if GameBoard[1] == 'X' and GameBoard[2] == 'X' and GameBoard[3] == 'X' :#Check bottom row
            print("YOU WIN!")
            
    
    while gameIsPlaying:
        # Game Logic here, this is our game loop.
        # Check to make sure the player inputs a valid number between 1- 9

        CheckWin(theBoard)

        if move < 1 or move > 9 :
            print('Value not allowed')
            drawBoard(theBoard)
            move = int(input('Choose a position (1-9)'))
        
        if move == 1 :
                if CheckMove(1) != True:
                    move = int(input('Choose a position (1-9)'))
                    drawBoard(theBoard)
                    CheckWin(theBoard)
                else:
                    theBoard[1] = playerMarker
                    drawBoard(theBoard)
                    move = int(input('Choose a position (1 - 9)'))
        if move == 2:
            theBoard[2] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))
        if move == 3:
            theBoard[3] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))
        if move == 4:
            theBoard[4] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))
        if move == 5:
            theBoard[5] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))
        if move == 6:
            theBoard[6] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))
        if move == 7:
            theBoard[7] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))
        if move == 8:
            theBoard[8] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))
        if move == 9:
            theBoard[9] = playerMarker
            drawBoard(theBoard)
            CheckWin(theBoard)
            move = int(input('Choose a position (1-9)'))

        
            
