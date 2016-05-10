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
    
    while gameIsPlaying:
        # Game Logic here, this is our game loop.
        print('YOUR_NAME - Tic-Tac-Toe Project.')
        print('---------------------------------------------')
        #Cast out inputs to the correct variable type remember!
        move = int(input('Choose a position (1 - 9)'))
        if move == 1 :
            #Place an X in the correct position on the board
            theBoard[1] = 'X'
            #Redraw the board with the changes.
            drawBoard(theBoard)

        time.sleep(100)
            
